# Founder OS

**An operating system for running a company with an AI — organised around your goals, and built to argue with you.**

Most AI setups are reactive: you ask, it answers, and the answer is only as good as whatever you remembered to paste. A Founder OS is the opposite. It's a small set of plain-text files that hold what your company is *trying to do* and the real state of play — plus a set of routines that move the work forward on a schedule while you sleep, drafting and reconciling and pressure-testing, surfacing only the decisions that need you.

It is **not** a note-taking app or a "second brain." Those store what you know. This runs what you're *doing*: it points at a handful of objectives, does work between your sessions, and is deliberately designed to tell you when you're wrong.

Forkable, plain Markdown, MIT-licensed. No app, no database, no lock-in — text an AI and a human read equally well.

New to any of the words below (rail, cabinet, heartbeat, fork, cron…)? Keep `GLOSSARY.md` open — one plain line each.

---

## How this maps to YOUR business

The OS is business-agnostic. Wherever a file says "customer" or "deal" or "raise", read it as whatever your business actually has. A rough Rosetta Stone:

| Concept | SaaS | Agency | E-commerce | Creator |
|---|---|---|---|---|
| Customer / pipeline | Accounts in trial → paid | Leads → retainer clients | Shoppers → repeat buyers | Audience → subscribers/members |
| A "deal" | A signed subscription | A signed retainer / SOW | A wholesale or B2B order | A sponsorship / brand deal |
| The money goal *(optional)* | Raise a round | Hit retainer revenue | Hit profitable scale | Hit a membership target |
| Ship / product | A feature release | A delivered engagement | A product / drop launch | A piece of content / a launch |
| The key metric | MRR / runway | Utilisation / margin | CAC / ROAS | Subscribers / engagement |

For transactional businesses (e-commerce, creator), the canonical "truth" for live numbers is often an **external dashboard** — Shopify, Stripe, your analytics — that you reconcile *against*, not a `_crm/` file you type by hand. Point the OS at "what the dashboard says" as the tier-1 source for those numbers.

---

## How it's built

**Goals at the centre.**
The system is organised around what you're trying to *achieve*, not just what you *know*. A short list of objectives sits at the core, and a "rail" tracks each one — answering, on its own each week: are we on track, what's slipping, what's the single highest-leverage move. If a routine doesn't move an objective, it gets cut.

**It produces, then presents.**
The OS runs on a schedule — ideally on an always-on machine — and does real work between your sessions: re-scoring progress, drafting the next move, preparing decisions. When you sit down, one routine (your morning brief) shows you what it produced and what's waiting. The machine works overnight; you arrive to a desk that's already been laid out.

**It's built to disagree with you.**
Once a week it convenes a *cabinet* — a set of AI agents reasoning from different angles, including one whose entire job is to argue you're wrong. They hand you a ranked set of moves and the uncomfortable questions you've been avoiding. A separate loop interrogates you on a cadence — *what changed that I can't see?* — because the system only knows what it's been told. It's designed to surface dissent, not to flatter you.

**You stay the judgment.**
The OS drafts, proposes, reconciles, and files — it never sends an email, moves money, or takes an irreversible action on its own. You send every send, approve every action, make every real call. It removes the busywork and the excuses; it never removes you from the decisions.

**Trust underneath.**
None of that is safe unless the facts under it are. So the foundation is the discipline most setups skip: every fact has one canonical home (other files point to it, they don't copy it); a gate tiers every new input before it's allowed in — first-party fact, unverified, or positioning — and anything that flatters you is held until it's checked; and when two facts disagree, the system never picks a winner quietly — it shows you both and you decide. See `SOURCES_OF_TRUTH.md` and `INGESTION_GATE.md`.

---

## Quickstart

1. **Copy** this folder to where you keep your company's files, and rename it to your company. *(Technical users: fork it.)*
2. **Fill in `CLAUDE.md`** (from the template): the venture, the team, the model, and above all your handful of current objectives. This is what the AI reads first.
3. **Drop your real material** over the worked example ("Alex / Northwind").
4. **Wire one routine** from `SCHEDULE.md` and watch it for a week before adding the next.
5. **Keep the app open** — that's what lets it run between your sessions.

> These folders (`_crm/`, `_memory/`, `decisions/`, `research/`, `CONTROL_CENTRE.md`) ship as empty stubs — the AI fills them in as you go.

Start with your goals and one routine. Everything else compounds from there. Once it's running, **`ONGOING.md`** is the habit that keeps it valuable — what to connect, what context is worth keeping, and the weekly rhythm.

---

## What's in the box

| File | What it is |
|---|---|
| `00-START-HERE.md` | Orientation + Step 0 setup. Read first. |
| `GLOSSARY.md` | Every term in one plain line. Keep it open while you learn the system. |
| `ONGOING.md` | How to live with it — what to connect, what context to keep, the weekly rhythm. |
| `CLAUDE.md.template` | The root context the AI reads first. Fill in, save as `CLAUDE.md`. |
| `OKRS.md` | Your objectives — the thing the whole system points at. |
| `SOURCES_OF_TRUTH.md` | Which file owns which fact, and what wins on a conflict. |
| `INGESTION_GATE.md` | The tier on everything new before it's allowed in. |
| `SCHEDULE.md` | The routine roster — what runs, when, on which machine. |
| `_routines/` | The routine prompts (heartbeat, reconciliation, cabinet, brain-health…). |
| `tools/dashboard.py` | A no-dependency, read-only dashboard of your system. |

---

*MIT-licensed. Use it, fork it, share it, sell what you build on it. No warranty.*
