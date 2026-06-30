# [VENTURE NAME] — Goal Scorecard

> **The whole game, to [horizon date].** This is the first artefact every routine reads and writes back to. If a task doesn't move O1, O2, or O3, it waits.
> **Owner:** the routines (auto-refresh the standing lines) + you (curate the targets).
> **Derived view** — the *standing/status* lines are derived from `_crm/`. *Targets* are canonical here; *standing* is not. On any conflict about a customer/investor/advisor fact, the `_crm/` source wins. See `SOURCES_OF_TRUTH.md`.

**Last updated:** [date] · **Keystone:** O1 (the goal that unlocks the others).

---

## 🎯 The three objectives

### O1 — [keystone objective]  ·  [🟢 on track / 🟡 firming / ⛔ off track]
**KR:** [measurable result, e.g. ≥3 signed], **by [date].**

| | |
|---|---|
| **Target** | [target] · **Stretch** [stretch] |
| **Now** | [current standing — derived from the CRM] |
| **Days left** | [n] |
| **The one move now** | [the single highest-leverage next action] |

### O2 — [objective]  ·  [status]
**KR:** [measurable result], by [date].

| | |
|---|---|
| **Target** | [target] |
| **Now** | [current standing] |
| **Days left** | [n] |
| **The one move now** | [...] |

### O3 — [objective]  ·  [status]
**KR:** [measurable result], by [date].

**Now:** [current standing]. **The one move now:** [...]

---

## 🔗 The keystone chain

```
[O1 first proof] ──► [what it unlocks] ──► [the gate that trips] ──► [O2 opens]
```

**Everything gates on O1.** The OS biases attention to the keystone accordingly.

---

## How this file is maintained

- Each routine sweep updates its objective's "Now / status" line and appends a digest to `_routines/runs/`.
- The weekly Heartbeat re-derives on/off-track and the "one move now" per objective, and refreshes the top of `CONTROL_CENTRE.md`.
- On any outcome (deal won/lost, commitment landed, seat closed) a short entry goes to `_memory/patterns/` so the next conversation starts ahead.
- Targets are yours to curate; **the routines never invent a target.**

---

*Worked example (delete once you've filled in your own):*
> ### O1 — Land 3 paying design partners · 🟡 firming
> **KR:** ≥3 signed by end of Q3.
> **Now:** 1 signed (Bramble Health), 2 in trial. **The one move now:** convert the next trial to annual.

*Your O1 will look different depending on the business — same shape, different keystone:*
> - **Agency:** "Land 2 retainer clients" · **Creator:** "Hit 10k subscribers" · **E-commerce:** "Reach profitable CAC at scale."
