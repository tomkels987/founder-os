#!/usr/bin/env python3
"""
Founder OS — control-centre dashboard generator.

READ-ONLY. Parses the brain's canonical markdown and renders a single
self-contained control-centre.html you can open in any browser.
No external dependencies, no mutation of the brain.

Reads (all optional — degrades gracefully if a file is missing):
  OKRS.md            - the three goals (header status + the "Now" row)
  CONTROL_CENTRE.md  - the blockers / "what needs you" list
  _routines/runs/    - recent routine run digests
  SCHEDULE.md        - (the routine roster; mirrored below for rendering)

Usage:  python3 tools/dashboard.py   ->   tools/control-centre.html
"""
from __future__ import annotations
import re
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "control-centre.html"


def read(rel: str) -> str:
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


def okrs() -> list[dict]:
    """Pull the three OKR blocks (header status + the 'Now' row) from OKRS.md.

    Handles both layouts: a markdown table with a `**Now** | ...` row, and an
    inline `**Now:** ...` line. Falls back gracefully if neither is present.
    """
    txt = read("OKRS.md")
    out = []
    for n in ("1", "2", "3"):
        m = re.search(rf"^###\s*O{n}\s*[—-]\s*(.+)$", txt, re.M)
        if not m:
            continue
        header = m.group(1).strip()
        status = header.split("·")[-1].strip() if "·" in header else ""
        title = header.split("·")[0].strip()
        block = txt[m.end():m.end() + 1200]
        now_m = re.search(r"\*\*Now\*\*\s*\|\s*(.+?)\s*\|", block)   # table form
        if not now_m:
            now_m = re.search(r"\*\*Now:?\*\*:?\s*(.+)", block)       # inline form
        now = re.sub(r"\*\*|`", "", now_m.group(1)).strip()[:110] if now_m else "—"
        out.append({"id": f"O{n}", "title": title, "status": status, "now": now})
    return out


# The routine roster is the source of truth in SCHEDULE.md; mirrored here for
# rendering. Tuple = (display name, when, machine, run-file token to find last run).
ROUTINES = [
    ("Morning brief",     "weekdays AM",  "Laptop", "morning"),
    ("End-of-day sync",   "daily PM",     "Laptop", None),
    ("Heartbeat",         "weekly",       "Always-on", "heartbeat"),
    ("Reconciliation",    "1-2x / week",  "Always-on", "sync"),
    ("The Cabinet",       "weekly",       "Always-on", "cabinet"),
    ("Weekly review",     "weekly",       "Always-on", "review"),
    ("Brain-health",      "weekly",       "Always-on", "brain-health"),
]


def last_run(token: str | None) -> str:
    if not token:
        return ""
    d = ROOT / "_routines" / "runs"
    runs = sorted(d.glob(f"*{token}*.md")) if d.exists() else []
    if not runs:
        return ""
    m = re.match(r"(\d{4}-\d{2}-\d{2})", runs[-1].name)
    return m.group(1) if m else ""


def recent_runs(limit: int = 8) -> list[str]:
    d = ROOT / "_routines" / "runs"
    if not d.exists():
        return []
    files = [f for f in d.glob("*.md") if f.name != "README.md"]
    files.sort(reverse=True)
    return [f.stem for f in files[:limit]]


def blockers() -> list[str]:
    """Pull the blocker rows from CONTROL_CENTRE.md (what needs you)."""
    txt = read("CONTROL_CENTRE.md")
    m = re.search(r"^##[^\n]*Blockers[^\n]*\n(.*?)^##", txt, re.S | re.M)
    if not m:
        return []
    rows = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith("|") and "Blocker" not in line and "---" not in line:
            cell = re.sub(r"\*\*|`", "", line.split("|")[1]).strip()
            if cell:
                rows.append(cell)
    return rows[:6]


def html() -> str:
    today = datetime.date.today().isoformat()
    okr_cards = "".join(
        f"""<div class="tile"><div class="k">{o['id']} · {o['title']}</div>
        <div class="st">{o['status']}</div><div class="v">{o['now']}</div></div>"""
        for o in okrs()
    ) or "<p class='muted'>OKRS.md not found — add it to see your goals here.</p>"

    rrows = ""
    for name, when, home, token in ROUTINES:
        lr = last_run(token)
        lr_txt = f"last run {lr}" if lr else ""
        chip = "mini" if home == "Always-on" else "laptop"
        rrows += f"""<div class="r"><span class="dot"></span>
        <span class="rn">{name}<small>{lr_txt}</small></span>
        <span class="home {chip}">{home}</span><span class="when">{when}</span></div>"""

    desk = "".join(f"<li>{b}</li>" for b in blockers()) or "<li class='muted'>none parsed</li>"
    runs = "".join(f"<li>{r}</li>" for r in recent_runs()) or "<li class='muted'>no runs yet</li>"

    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Founder OS — control centre</title>
<style>
:root{{--bg:#fff;--card:#fff;--bg2:#f5f5f4;--bd:#e7e5e4;--tx:#1c1917;--mut:#78716c;--inf:#2563eb;--infbg:#eff6ff}}
@media(prefers-color-scheme:dark){{:root{{--bg:#0c0a09;--card:#1c1917;--bg2:#1c1917;--bd:#292524;--tx:#fafaf9;--mut:#a8a29e;--inf:#60a5fa;--infbg:#172554}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--tx);font:15px/1.5 -apple-system,Inter,Arial,sans-serif;padding:28px;max-width:820px;margin:0 auto}}
h1{{font-size:18px;font-weight:500;margin:0 0 4px}}.sub{{color:var(--mut);font-size:13px;margin:0 0 22px}}
.cap{{font-size:12px;color:var(--mut);text-transform:uppercase;letter-spacing:.04em;margin:24px 0 10px}}
.okr{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}}
.tile{{background:var(--bg2);border-radius:10px;padding:13px 15px}}
.tile .k{{font-size:12px;color:var(--mut)}}.tile .st{{font-size:13px;margin:3px 0}}.tile .v{{font-size:15px;font-weight:500}}
.card{{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:6px 16px}}
.r{{display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid var(--bd)}}.r:last-child{{border:none}}
.dot{{width:7px;height:7px;border-radius:50%;background:#16a34a;flex:none}}
.rn{{flex:1;font-size:14px}}.rn small{{display:block;font-size:11px;color:var(--mut)}}
.when{{font-size:11px;color:var(--mut);background:var(--bg2);padding:2px 8px;border-radius:6px;white-space:nowrap}}
.home{{font-size:10px;padding:1px 7px;border-radius:6px;white-space:nowrap}}
.home.mini{{background:var(--infbg);color:var(--inf)}}.home.laptop{{border:1px solid var(--bd);color:var(--mut)}}
ul{{margin:0;padding:0 0 0 18px}}li{{margin:5px 0}}.muted{{color:var(--mut)}}
.desk{{border:2px solid var(--inf);border-radius:12px;padding:12px 16px}}
</style></head><body>
<h1>Founder OS — control centre</h1>
<p class="sub">generated {today} · read-only view of the brain · regenerate with <code>python3 tools/dashboard.py</code></p>

<div class="cap">the goals</div>
<div class="okr">{okr_cards}</div>

<div class="cap">on your desk — what needs you</div>
<div class="desk"><ul>{desk}</ul></div>

<div class="cap">the machine — routines</div>
<div class="card">{rrows}</div>

<div class="cap">recent runs</div>
<div class="card" style="padding:12px 16px"><ul>{runs}</ul></div>
</body></html>"""


if __name__ == "__main__":
    OUT.write_text(html(), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}  ({len(okrs())} goals, {len(blockers())} desk items)")
