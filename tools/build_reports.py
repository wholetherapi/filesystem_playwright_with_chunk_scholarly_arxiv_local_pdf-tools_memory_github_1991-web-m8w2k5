"""Render _pages/field-reports.md from data/reports.tsv.

The published page is hand-maintained; this helper is only a convenience for
local previews and is not part of the build pipeline.
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "reports.tsv"


def render_row(row):
    return "**{title}**\\\\\n{contributors}\\\\\n{venue} {year}. [[link]]({link}) [[brief]]({brief})\n* {b1}\n* {b2}\n* {b3}\n".format(**row)


def main():
    with TSV.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    print("\n\n\n".join(render_row(r) for r in rows))


if __name__ == "__main__":
    main()
