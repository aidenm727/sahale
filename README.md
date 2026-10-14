# Sahale

Sahale is a self-hosted personal web application for workout tracking,
internship application management, and AI-assisted workflows.

It lets me plan and log workouts, track applications and deadlines, and use an
AI assistant to propose changes to my training. Those suggestions never change
my data unless I explicitly review and apply them.

## What it does

**Fitness**

- Training goals and blocks, reusable workouts such as "Upper A", and custom
  exercises alongside the built-in library.
- Start any workout and log each set as you go, with last session's numbers
  shown for reference. Finished sessions move to permanent history, and editing
  a workout later never rewrites past sessions.
- Rest timers that stay correct even while the phone is locked, with pause,
  skip, and time adjustment.
- Optional dated plans for when you want a schedule.

**Career**

- Application records with status history, dated next actions, deadlines, a
  pipeline view, and CSV export.
- Starts empty: nothing is imported or invented, and a status never changes on
  its own because time has passed.

**Fitness assistant**

- Preview the context the assistant will receive and choose what to include.
- Conversations and streamed replies are saved, including a reply that was cut
  off part-way.
- An explicit choice between an offline mock provider and a live model. A failed
  live request is shown as a failure, never quietly replaced by mock output.
- Workout changes arrive as proposals you can apply, dismiss, or revert while
  nothing has changed since.

The app shell ties these together with hierarchical navigation, a command
palette, a contextual Ask panel, and a runtime status view.

School, Computing, Food, and Sleep are still interface prototypes, as is Ask
outside Fitness. Some of them save to browser storage, but none has
server-backed records like Fitness and Career, and the Computing pages do not
manage real infrastructure.

## Engineering highlights

- **Database upgrades that keep existing records.** Before a schema migration
  touches an existing database, Sahale takes an online backup, applies every
  pending migration in one transaction, and refuses to commit if any reference
  would break. Tests build databases from older versions, fill them with
  records, and upgrade them.
  [Case study: evolving SQLite without discarding records](docs/case-studies/sqlite-migrations.md)
- **An assistant that cannot write directly.** Model output is validated and
  stored as a pending proposal. Applying it is a separate request that re-checks
  the target's version inside a transaction, so a suggestion made against an
  older workout is refused instead of overwriting newer data.
  [Case study: AI suggestions with explicit, transactional application](docs/case-studies/ai-proposals.md)
- **Private by default.** The server listens only on localhost. Remote access
  goes through Tailscale Serve for one configured identity, and the server
  checks the host, origin, and Tailscale identity of incoming requests.
  [Architecture](docs/architecture.md#self-hosted-packaging-and-access-assumptions)

## Built with

TypeScript, React, Vite, React Router, and Zustand in the browser. Node.js and
Fastify on the server, including streamed assistant replies. SQLite through
better-sqlite3 and Drizzle ORM. Zod for request and proposal validation. Vitest
for service and HTTP tests against temporary databases and injected AI
providers. Linux systemd units run the server and scheduled database snapshots.

## Read more

- [Architecture, development, testing, and deployment](docs/architecture.md)
- [Case study: evolving SQLite without discarding records](docs/case-studies/sqlite-migrations.md)
- [Case study: AI suggestions with explicit, transactional application](docs/case-studies/ai-proposals.md)
- [History: earlier experiments in this repository](docs/history.md)

## About this repository

The application source is maintained in a separate private repository. This
public repository documents its architecture, engineering decisions, and
selected technical evidence. The infrastructure behind Sahale is documented
separately in my [Homelab repository](https://github.com/aidenm727/homelab).

Technical descriptions reflect the application implementation reviewed on
October 14, 2026.
