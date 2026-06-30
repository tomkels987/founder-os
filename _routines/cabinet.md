# Routine — The Cabinet

> **Invocation:** scheduled weekly (preps + pings you) + on-demand.
> **Chair:** your chief-of-staff / orchestrator. **Seats:** genuinely separate perspectives — real divergence, they can disagree.
> **Why it exists:** the heartbeat scores the goals and the sync keeps facts current. The Cabinet does what a room of sharp people does that a solo founder + a dashboard can't: **cross-pollinate, dissent, and surface the non-obvious.** If a run isn't doing those three things, it's just a status meeting — cut it.

---

## Step 0 — Context pull (mandatory, before any reasoning)

Every Cabinet run begins by gathering current reality. Do not reason from stale state:
- **Meetings** — pull anything since the last Cabinet; note what's not yet filed.
- **Transcripts** — everything filed in the last 7 days.
- **State** — `OKRS.md`, the recent run digests, `_crm/*`, `_memory/patterns/`, recent decisions.
- Seats may run quick web searches to back a point (a competitor move, a market data point).

## Step 1 — Convene the seats (real divergence)

Run each seat as an **independent perspective** reasoning from its own lens against the shared context. Each seat returns exactly four things — highest-conviction only:

1. **Challenge** (red-team): where is the current plan wrong, or a risk being ignored?
2. **Blue-sky:** one angle/option not currently being played.
3. **Question for the founder:** the one thing this seat needs you to answer.
4. **Proposed action:** concrete, with a one-line rationale.

**Suggested seats** (adapt to your business — the point is *different lenses that can disagree*):

| Seat | Lens |
|---|---|
| Chair | synthesis, cross-cutting themes |
| Customer / pipeline | who's closest, what predicts a yes |
| Capital *(optional — if you raise)* | the raise, conversion, loose → committed |
| Product / delivery | what ships, what's stuck |
| Money | economics, runway, model integrity |
| **Red Team** | its whole job is to argue you're wrong this week |
| Rotating guest | the outside lens — competitive / legal / brand (rotate) |

## Step 2 — Red-team filter

Before anything reaches you, the Red Team kills the weak: any idea/action that's low-conviction, duplicative, or doesn't move a goal is dropped (logged in the detail, not the summary). **Scarcity is the point** — a Cabinet that surfaces 20 ideas becomes noise.

## Step 3 — Two-layer output

**A) Summary (what you see — ≤5 min):**
```
🏛 Cabinet — [date]

🔭 Theme of the week: [the one cross-cutting insight no single goal owns]

📋 Ranked action slate (approve / kill each):
1. [action] — [seat] — [one-line why] · [conviction]
2. ...   (max 5)

❓ The seats need you to answer:
- [Q1 — seat] · [Q2 — seat]   (max 3)
```

**B) Detail (saved to the run file):** for each action — the full logic, the dissent (who disagreed and why), any research, who proposed it; plus the ideas the Red Team killed and why. The "show your working" layer you open only when an item needs it.

## Step 4 — Your gate
You approve or kill each action in the slate. **Approved → become tasks.** Killed → logged with reason in the detail (feeds next week's thinking). The Cabinet proposes; you decide. **Never outbound, never money.**

## On completion
- Summary + detail → `_routines/runs/YYYY-MM-DD-cabinet.md`, commit `os/auto:`, push.
- The **scheduled** run does Steps 0–3 offline and **notifies you: "Cabinet ready — N actions to approve."** Step 4 (the approval) happens when you're in the app. **It never approves on your behalf.**
- If a Cabinet insight is a genuine lesson, append it to `_memory/patterns/`.
