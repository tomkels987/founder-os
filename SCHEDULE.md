# SCHEDULE.md — the wired cadence (source of truth)

> **This file is the single source of truth for what actually fires.** If a routine isn't listed here as registered, it does not run automatically — it's a manual command only.
> **Start small.** A handful of routines you read beats fifty you ignore. Roll out one, prove it for a week, then add the next.

**Last updated:** [date]

---

## Execution model — produce vs. present

> **Optional — power users / multiple machines.** If you run a single machine (most people), ignore this whole section: run every routine on your one machine and you're done. The two-machine split below is an optimisation for people who want routines running while their laptop is closed — it is **not** required.

The OS works best split across two machines. If you only have one, run everything there — but understand the intended shape:

| Machine | Role | Runs |
|---|---|---|
| 🖥 **Always-on machine** (a spare laptop / mini desktop, app always open) | **Produces** | The autonomous routines — heartbeat, sync prep, the cabinet, brain-health, reviews. Runs whether you're at your desk or not. |
| 💻 **Your laptop** | **Presents** | The morning brief (shows you what the always-on machine produced overnight) and the end-of-day sync (pushes your day's work so the other machine wakes up current). |

**The contract:** the always-on machine does the work and pushes it; your laptop's morning brief pulls it down and shows you what's waiting. Run each autonomous routine on **one** machine only — never both, or they double-fire. If you've only got one machine, just run it all there; the split is an optimisation, not a requirement.

---

## The cadence

| Routine | When | Reads | Writes / output | Escalate? |
|---|---|---|---|---|
| **Heartbeat** | weekly (e.g. Mon AM) | `OKRS.md`, CRM, recent transcripts | Refresh `OKRS.md` + top of `CONTROL_CENTRE.md`; digest → `_routines/runs/` | only if a goal goes off-target |
| **Reconciliation / sync** | 1–2×/week | the CRM + the OKRs | asks you what changed it can't see; writes confirmed deltas back | the unmade decision; the aging thread |
| **The Cabinet** | weekly | whole brain + recent transcripts | a ranked action slate you approve/kill | the questions the "seats" need answered |
| **Weekly review** | weekly (e.g. Fri PM) | the week's runs | what moved per goal + a draft update | — |
| **Brain-health** | weekly | whole brain | a rot report → `_memory/brain-health/` | any 🔴 finding (drift, conflict) |
| **Morning brief** | weekdays AM | calendar, inbox, tasks, OKRs, queue | a 60-second cockpit | — |
| **End-of-day sync** | daily PM | the working tree | pushes the day's work to the always-on machine | — |

On-demand (you invoke, not scheduled): any of the above, plus one-off prep before a meeting.

---

## Hard rules (every routine)

1. **Never outbound.** No routine sends an email or moves money. Email = a **draft** only. State mutations = git commits prefixed `os/auto:` (so `git revert` is the undo). **It drafts; you fire send.**
2. **Every sweep ends in a drafted next move**, not a bare flag. An alarm with no proposed action is noise.
3. **Escalate only two classes to you:** the *unmade decision* and the *aging keystone thread*. Everything else is filed silently — don't make the founder the router for trivia.
4. **Keep it to 30 seconds.** Any digest over ~250 words is failing. The Cabinet's detail layer is the one exception — but its *summary* obeys the rule.
5. **Context-pull first.** Every routine begins by gathering current reality — recent meetings, transcripts filed since last run, latest state — *before* it reasons. No routine reasons from stale state.
6. **Git-pull first (always-on machine).** *Optional — power users / multiple machines only.* Every routine on the always-on machine begins with `git pull --rebase --autostash` so it acts on your latest laptop work, then commits + pushes its own output. Single-machine users can ignore git entirely.

---

## Rollout order (don't over-schedule)

- **Wave A (prove the loop, ~1 week):** Heartbeat · Weekly review · Brain-health.
- **Wave B (after A sticks):** Reconciliation/sync · Morning brief · End-of-day sync.
- **Wave C:** the Cabinet · monthly/quarterly reviews.

**Register a routine here only after you've dry-run its prompt by hand once** and it produced a sane digest and a clean `os/auto:` commit. If the dry run is noisy, fix the prompt before you automate it — you're automating a thing that works, not hoping automation makes it work.

---

## How to register

Most AI desktop apps support **scheduled tasks** (a built-in timer that runs a prompt for you while the app is open — **you don't need to know cron, just pick a day and time**). The click-path is roughly the same in every app:

> **In your AI app: Scheduled Tasks → New → choose weekly + a day/time → paste:**
> *"Run the routine in `_routines/<file>.md` and follow it exactly."*

(Swap `<file>` for the routine you're registering, e.g. `heartbeat.md`.) Use off-the-:00 times (e.g. 08:23, 17:17) so multiple routines don't all fire at once. Track what's live here:

| Routine | When | Registered? | Prompt fires from |
|---|---|---|---|
| Heartbeat | weekly, Mon AM | ☐ | `_routines/heartbeat.md` |
| Weekly review | weekly, Fri PM | ☐ | `_routines/weekly-review.md` |
| Reconciliation / sync | 1–2× / week | ☐ | `_routines/reconciliation-sync.md` |
| The Cabinet | weekly | ☐ | `_routines/cabinet.md` |
| Brain-health | weekly | ☐ | `_routines/brain-health.md` |
| Morning brief | weekdays AM | ☐ | `_routines/morning-brief.md` |
| End-of-day sync | daily PM | ☐ | `_routines/eod-sync.md` |

First-run note: routines that touch your calendar / inbox / meeting tools will ask for permission the first time. Run each once by hand ("Run now") to pre-approve those tools, so unattended runs don't stall on a prompt.
