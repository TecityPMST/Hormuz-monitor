#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebuilds score_history.json by reading the ACTUAL score out of every
archived PDF in pdf/ — no hand-entered numbers. This is the source the
dashboard's "Score history" chart and the "Full PDF editions" archive table
both draw on.

For each pdf/hormuz_us_shock_monitor_YYYY-MM-DD-bbg.pdf:
  1. Extract text with pdftotext (must be on PATH — `apt install poppler-utils`
     if missing).
  2. Find the "Score FALLS/RISES/HOLDS/JUMPS/returns/crosses ... to/at N/30"
     sentence in the headline judgment (handles every phrasing seen across
     editions: "Score HOLDS at 25/30", "Score FALLS to 26/30", "Score RISES
     +1 to 21/30", "Score returns to 20/30", "Score crosses into the CRISIS
     band at 22/30").
  3. Use that whole sentence (up to the first period) as the "driver" shown
     in the chart tooltip.

Run this after adding a new PDF to pdf/ (and before running
build_dashboard.py). It reprocesses every PDF in the folder each time, so
it's always a full, verifiable rebuild rather than an incremental patch.
"""
import glob, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_DIR = os.path.join(HERE, "pdf")

# NOTE: "Score" is matched case-SENSITIVELY (capital S only). Every edition's
# actual verdict sentence starts with capitalized "Score" ("Score HOLDS at
# 25/30", "Score falls to 20/30", "Score returns to 20/30", "Score crosses
# into the CRISIS band at 22/30"...). Incidental lowercase mentions like
# "AAA pump — score reference" must NOT match, or the driver sentence grabs
# the wrong context (the score number can still end up right by luck since
# the non-greedy scan keeps extending to the next digit/30 it finds, but the
# extracted driver text ends up nonsensical). The verb itself varies in
# casing across editions, so only the verb alternation is case-flexible.
SCORE_RE = re.compile(
    r"Score\s+(?:FALLS|falls|RISES|rises|HOLDS|holds|JUMPS|jumps|"
    r"returns|Returns|crosses|Crosses)\b.{0,100}?(\d{1,2})\s*/\s*30",
    re.DOTALL,
)
FNAME_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")

def extract_text(pdf_path):
    try:
        out = subprocess.run(["pdftotext", pdf_path, "-"], capture_output=True, text=True, check=True)
        return out.stdout
    except FileNotFoundError:
        sys.exit("pdftotext not found on PATH — install poppler-utils (apt install poppler-utils).")
    except subprocess.CalledProcessError as e:
        print(f"WARNING: pdftotext failed on {pdf_path}: {e}", file=sys.stderr)
        return ""

def find_score_and_driver(text):
    m = SCORE_RE.search(text)
    if not m:
        return None, None
    score = int(m.group(1))
    # driver = from "Score" through the first period after the match
    start = m.start()
    tail = text[start:]
    period_idx = tail.find(".")
    sentence = tail[:period_idx + 1] if period_idx != -1 else tail[:220]
    driver = re.sub(r"\s+", " ", sentence).strip()
    return score, driver

def main():
    rows = []
    for pdf_path in sorted(glob.glob(os.path.join(PDF_DIR, "*.pdf"))):
        fname = os.path.basename(pdf_path)
        dm = FNAME_RE.search(fname)
        if not dm:
            print(f"SKIP (no date in filename): {fname}", file=sys.stderr)
            continue
        date = dm.group(1)
        text = extract_text(pdf_path)
        score, driver = find_score_and_driver(text)
        if score is None:
            print(f"WARNING: could not find a score in {fname} — skipped. Check the PDF's headline phrasing.", file=sys.stderr)
            continue
        rows.append({"date": date, "score": score, "driver": driver})

    rows.sort(key=lambda r: r["date"])

    out_path = os.path.join(HERE, "score_history.json")
    with open(out_path, "w") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

    print(f"Wrote {out_path} with {len(rows)} editions "
          f"({rows[0]['date']} to {rows[-1]['date']})" if rows else "No editions found.")

if __name__ == "__main__":
    main()
