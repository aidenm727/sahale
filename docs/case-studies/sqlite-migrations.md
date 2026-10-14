# Evolving SQLite without discarding records

[Architecture](../architecture.md) · [Project overview](../../README.md)

Sahale's Fitness workflow evolved from dated workouts to reusable templates
and durable active sessions, then gained persisted rest timers and a Career
tracker. Those additions change an existing database, not just a fresh schema.
The engineering problem is keeping prior records usable while refusing schema
states the running application cannot safely interpret.

## Implementation decision

The runtime applies ordered Drizzle-generated SQL migrations and records their
hashes. Before changing an existing database, it takes a full SQLite online
backup. All pending migration statements and their migration records run in a
single transaction. A failure rolls back the attempted schema changes rather
than leaving a partially upgraded database.

SQLite table rebuilds require special care. Foreign keys are disabled at the
connection level before the migration transaction so a parent-table rebuild
does not trigger cascading deletion of child rows. Before commit, the runtime
runs `foreign_key_check`; broken references cause rollback. It restores foreign
key enforcement after the attempt.

The runner also compares already-applied migration hashes with the checked-in
migration set. A changed migration or a database from a newer, unknown schema
stops normal database use. Database-dependent routes report an unavailable
state; the application does not guess how to downgrade existing records.

## Concrete upgrade evidence

The tests construct older schema fixtures, write synthetic records,
then open them with the current migration runner:

| Upgrade/failure | Asserted behavior |
| --- | --- |
| Reusable workouts | Existing goals and blocks survive; old dated workouts are mapped without inventing reusable templates |
| Rest timers | New columns are added after backup without changing existing rows |
| Career tables | Existing Fitness rows and the Fitness snapshot remain unchanged; Career starts empty |
| Broken pending SQL | Previously existing tables remain intact and the incomplete new table does not survive |
| Parent-table rebuild | Child rows survive the rebuild |
| Changed or unknown applied migration | Startup refuses normal database use |

These assertions are in the application's `test/db.test.ts`,
`test/workouts.test.ts`, `test/rest.test.ts`, and `test/career.test.ts`; the
runner is `server/db/index.ts`.

## Tradeoffs and limits

A single SQLite database and synchronous access keep the persistence boundary
small for a single-user application. Migration hashing favors refusal over
attempted repair when history disagrees. An upgrade therefore needs both a
compatible application version and available backup storage.

An online backup and transaction rollback address different failures: the
transaction avoids partial application, while the backup preserves the prior
database for recovery. Neither proves that a restore procedure has been
successfully rehearsed. The deployment snapshot helper adds integrity-checked
copies, but off-host retention, recovery from host failure, and live upgrade
results have not been verified.

The design illustrates a broader lesson: preserving records includes refusing
an interpretation the application cannot support, and testing old-to-new
transitions rather than only checking initialization of a fresh database.
