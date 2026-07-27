#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebuilds pdf_manifest.json by scanning pdf/*.pdf — this drives the "Full PDF
editions" archive table so EVERY PDF copy sitting in the folder gets a
download link, not just the two editions kept in full detail in
editions.json. Run this whenever a PDF is added to (or removed from) pdf/.
"""
import glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_DIR = os.path.join(HERE, "pdf")

FNAME_RE = re.compile(r"hormuz_us_shock_monitor_(\d{4})-(\d{2})-(\d{2})-bbg\.pdf$")
MONTHS = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def main():
    entries = []
    for pdf_path in sorted(glob.glob(os.path.join(PDF_DIR, "*.pdf"))):
        fname = os.path.basename(pdf_path)
        m = FNAME_RE.search(fname)
        if not m:
            print(f"SKIP (unexpected filename): {fname}")
            continue
        year, month, day = m.groups()
        date = f"{year}-{month}-{day}"
        label = f"{int(day)} {MONTHS[int(month)]} {year}"
        entries.append({"date": date, "filename": fname, "label": label})

    entries.sort(key=lambda e: e["date"], reverse=True)

    out_path = os.path.join(HERE, "pdf_manifest.json")
    with open(out_path, "w") as f:
        json.dump(entries, f, indent=2)

    print(f"Wrote {out_path} with {len(entries)} editions "
          f"({entries[-1]['date']} to {entries[0]['date']})" if entries else "No PDFs found.")

if __name__ == "__main__":
    main()
