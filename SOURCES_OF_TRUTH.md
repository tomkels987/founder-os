# Sources of truth — the canonical map

> **In one line:** the same fact should live in ONE file only, so your AI never trusts two versions.

> **The rule that stops the system contradicting itself.** Every fact lives in **exactly one** *canonical* file — its one official home. Other files may *restate* it for convenience, but they **point, they never own** — and on any conflict, the canonical source wins. When two files disagree, the OS does not pick a winner silently; it flags both and hands you the call.
>
> Why this exists: the moment two files each "own" the same number, copy-and-resync drifts. You end up with the scorecard saying one thing and the CRM saying another, and no way to know which is true. This file is the precedence law that prevents it.

**Last updated:** [date] · **Owner:** you (you set the law) + the brain-health routine (enforces it) + the sync routine (surfaces conflicts).

---

## Canonical source per fact-type

Adjust the rows to your org. The pattern is what matters: **one owner per fact-type, and the derived views that may only restate it.**

| Fact-type | Canonical source (owns it) | Derived views (restate, never own) |
|---|---|---|
| Customer / pipeline — stage, status, won/lost | `_crm/customers.md` | `OKRS.md`, `CONTROL_CENTRE.md`, dashboard |
| Investor commitments — loose / soft / hard *(if you raise — otherwise delete this row)* | `_crm/investors.md` | `OKRS.md`, `CONTROL_CENTRE.md` |
| Advisors / board | `_crm/advisors.md` | `OKRS.md`, `CONTROL_CENTRE.md` |
| Intros / people owed to you | `_crm/people-to-meet.md` | `CONTROL_CENTRE.md` |
| Deal terms / per-deal economics | `_crm/deals/<name>/` | `_crm/customers.md` (summary only) |
| Decisions made + why | `decisions/DECISIONS.md` | anywhere referencing a decision |
| Open questions / bets | `decisions/BETS.md` | — |
| Goal **targets** (the OKRs) | `CLAUDE.md` → `OKRS.md` header | dashboard, `CONTROL_CENTRE.md` |
| Goal **standing** (where you are) | derived from the CRM by the routines | `OKRS.md` standing lines, `CONTROL_CENTRE.md` |
| Your identity / voice | `CLAUDE.md` "how I work" | content/outreach drafts |
| Lessons / patterns | `_memory/patterns/` | meeting prep, tutorials |
| Research findings | `research/` + `RESEARCH_TRACKER.md` | decks, FAQ, objection notes |
| What fires when | `SCHEDULE.md` | — |

**Every derived view carries a header:** `> Derived view — canonical source is X. On conflict, X wins.` Add this line to `OKRS.md` and `CONTROL_CENTRE.md` so it's impossible to forget which file is the original and which is the echo.

---

## Precedence ladder — when sources disagree about the same fact

From most to least authoritative:

1. **Signed / legal document** — contract, signed order, term sheet. Highest.
2. **First-party statement from the customer / counterparty** — their email, their call, what *they* said about *their* situation.
3. **CRM entry** — what you typed from memory. Trustworthy, but yields to 1–2.
4. **Outward-facing positioning** — the deck, the pitch, numbers said *to* investors, customers, partners, or your audience. **Lowest for "what's true."** It's aspiration, not fact.

**The flattering-number rule:** any number that rounds in your favour — revenue, traction, growth, committed capital, valuation, follower count — must be validated against a tier-1/2 source before it enters a canonical file as fact. Numbers said to investors, customers, partners, or your audience are positioning, not fact (investors are just one common example). Aspiration must never wear the costume of fact.

*Worked example (keep your real version honest like this):*
> A number you *say* — a raise target, a "we're at [X] revenue", a "[Y]k audience" — is positioning, the ambition you put in the room. The *actual signed/measured* number might be a fraction of that. The brain keeps those two in **different columns on purpose**: one is the ambition, one is the fact. Never let the ambition quietly overwrite the fact.

See `INGESTION_GATE.md` for how new inputs are tiered before they're allowed in, and the brain-health routine's conflict + provenance audit that enforces all of this.
