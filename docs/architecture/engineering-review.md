# Engineering Review

Workflow v1.2 defines independent review requirements in
`docs/standards/engineering-collaboration.md`; the lifecycle and correction
sequence is in `docs/architecture/engineering-lifecycle.md`. Atlas has no
review command and cannot accept a candidate.

A review examines the exact final local candidate after tier-appropriate
verification. The reviewer receives the bounded brief, candidate identity,
complete diff, test results, protected and external boundaries, and known
uncertainty. It reports concrete findings with severity and evidence. The
implementer corrects in-scope findings, reruns affected checks and final broad
verification after the last mutation, and seeks a fresh review when required.

The owner accepts or rejects the exact verified candidate. Acceptance does not
authorize staging, commit, publication, deployment, or another external write.
A handoff reports the outcome, verification, unresolved risk, candidate
fingerprint, and next owner decision in plain language.
