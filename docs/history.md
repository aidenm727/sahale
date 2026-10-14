# History

[Current Sahale application](../README.md)

From February to September 2026 this repository presented an engineering
process rather than an application: a shared record of architecture, work
selection, and AI collaboration, supported by local Python tools. By September
it held 43 review records, 22 opportunity records, mission state, and generated
context documents, but none of the Sahale application itself. In October 2026
that model was retired. The application is now built as ordinary software, with
its tests beside its code, and this repository documents that application.

The earlier work stays in Git history; no commits were rewritten. Neither the
application nor the [homelab](https://github.com/aidenm727/homelab) repository
references any of the tools below. The links point to `e32e650`, the last
commit before the change. They show historical code, not current dependencies
or instructions.

## Atlas

Atlas was a small command-line tool meant to start each working session from
the same checkable picture of the repository instead of from conversation
memory. Its `bootstrap`, `validate`, and `sync` commands reported local Git
state, validated a typed record of active work and its evidence, and checked
that three generated documents matched their sources byte for byte.

[CLI](https://github.com/aidenm727/sahale/blob/e32e650d8370d76511a6b3c33b3c183f1f0bf743/tools/atlas/cli.py),
[active-state validation](https://github.com/aidenm727/sahale/blob/e32e650d8370d76511a6b3c33b3c183f1f0bf743/tools/atlas/platform/active_state.py),
and [context generator](https://github.com/aidenm727/sahale/blob/e32e650d8370d76511a6b3c33b3c183f1f0bf743/tools/generate-context.py).

Deterministic checks are good at proving consistency within what they check.
They cannot tell you whether the process they enforce is still worth its cost.
Keeping mission state, generated documents, and a large body of policy current
no longer fit a repository whose job is to present the application, so Atlas
and everything that depended on it were removed.

## School Learning

School Learning was a local study tool built around semester and course
records, source materials, topics, and study sessions. Its Python command-line
implementation validated JSON records, limited how much material it took in,
generated HTML and Markdown views, packaged structured handoffs for AI-assisted
study, and applied only reviewed updates back to the records.

The lesson worth keeping is to hold source observations, AI-assisted
interpretation, and accepted record changes apart, so that nothing becomes a
record without review. The application's School section is a separate
prototype that never used this tool.

School Learning was removed from the current tree. Its final implementation is
at [`tools/school_learning`](https://github.com/aidenm727/sahale/tree/e32e650d8370d76511a6b3c33b3c183f1f0bf743/tools/school_learning)
with its [tests](https://github.com/aidenm727/sahale/blob/e32e650d8370d76511a6b3c33b3c183f1f0bf743/tests/test_school_learning.py).

## Task-context compilation

This experiment aimed to give AI tools reproducible, task-specific inputs. The
Python library took immutable Git snapshots, selected sources through explicit
selectors, validated its output against schemas, produced deterministic JSON
with digests, enforced a size budget, and recorded what it left out.

[Compilation library](https://github.com/aidenm727/sahale/tree/e32e650d8370d76511a6b3c33b3c183f1f0bf743/tools/atlas/platform/context_compilation)
and [tests](https://github.com/aidenm727/sahale/blob/e32e650d8370d76511a6b3c33b3c183f1f0bf743/tests/test_context_compilation.py).

Its lasting lesson is to make provenance, exclusions, and budget trade-offs
visible. The application's Fitness context preview follows a similar idea but
is a separate implementation that does not reuse this code.

## Storage orientation

Two collectors, one in Python and one in Windows PowerShell, gathered bounded
storage metadata and produced sanitized reports. Neither was part of the
application, and both were removed from the current tree:
[Python collector](https://github.com/aidenm727/sahale/blob/e32e650d8370d76511a6b3c33b3c183f1f0bf743/tools/storage_orientation.py)
and [Windows collector](https://github.com/aidenm727/sahale/blob/e32e650d8370d76511a6b3c33b3c183f1f0bf743/tools/storage_orientation_windows.ps1).
