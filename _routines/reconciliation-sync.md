# Routine — Reconciliation & sync

> **Invocation:** scheduled 1–2×/week (preps the questions, pings you) + on-demand.
> **Why it exists:** the OS only knows what's been filed. Reality moves in WhatsApp, calls, and in-person — the system *cannot* see those. This routine closes the gap by **asking you**, locking your answers into state, and driving accountability. It is the human-in-the-loop heartbeat.

---

## The principle

**Pull, don't assume.** Every other routine reads files and reports. This one interrogates you and *writes truth back*. It also reverses the accountability arrow — it asks what the OS is waiting on *you* for, and forces each item to closed or parked.

**Make confirming cheap.** Always pre-state the OS's current belief so you can one-tap confirm or correct, never compose from scratch. Offer the current belief as the recommended option.

---

## The five reconciliation passes

Run in order. Keep each tight — this should take you under five minutes.

### 1. Per-goal delta sweep
For each objective, state the OS's current belief and ask: **"Since the last sync, what changed here that I can't see?"** Apply confirmed deltas to `_crm/` + `OKRS.md`, commit `os/auto:`.

### 2. Waiting-on-you (reverse accountability)
List **everything the OS is currently blocked on you for** — drafts awaiting send, decisions unmade, intros to make. For each, force a disposition:
- ✅ **Done** (you did it → log + clear)
- ⏳ **Still open** (keep, with a re-ask date)
- 🅿️ **Park** (deprioritised → move to a parked list, stop surfacing it)

Nothing stays in limbo.

### 3. Loose commitments
Walk the relevant CRM file: "Who's loosely said yes since we last spoke? Any loose → firmer, or loose → cold?" Capture amount / conviction / next step per person.

### 4. Context holes + conflicts ("confirm these")
- **Holes:** name where state looks thin or stale (a contact with no next action, a deal folder with no recent file). Ask you to fill the 2–3 most material gaps, or confirm "leave it."
- **Conflicts:** surface any place two files disagree about the same fact (per `SOURCES_OF_TRUTH.md`) — show **both sides**, never pick a winner; ask you which is true, then propagate to the canonical source.
- **Unverified flatter:** list any number that rounds in your favour and hasn't been validated against a tier-1/2 source (`INGESTION_GATE.md`) — ask you to confirm or correct before it's promoted from `[unverified]` to fact.
- **Won't invent:** anything the OS couldn't stand up against a source goes here as a question, not a guess.

### 5. Agent / routine governance
List the active routines and any spawned background tasks and their last output. Ask: "Which are still live, which are done, which should be killed?" A dormant routine is silent rot.

---

## Output
- A short **sync digest** to `_routines/runs/YYYY-MM-DD-sync.md`: deltas applied, items closed/parked, holes filled.
- Mutations committed `os/auto:`. **Never outbound** — drafts only; sends stay yours.
- If a delta carries a lesson (a deal lost, a commit landed), append an entry to `_memory/patterns/`.

## Scheduled behaviour
The scheduled run **prepares** the five passes from current state and **notifies you: "Sync ready — N questions."** The actual back-and-forth happens when you open the app — it needs you. **It never answers on your behalf.**
