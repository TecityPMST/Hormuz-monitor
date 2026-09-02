#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Source of truth for editions.json — the two-edition toggle on the dashboard.

Holds the FULL section-by-section content of the two most recent editions as
Python literals, copied from that edition's PDF build script. Edit the ed*_block
files, never editions.json. Keep exactly two dates: when a new edition is added,
drop the oldest block from the import list below.

Run:  python3 generate_editions.py
"""
import json

EDITIONS = {}

# =====================================================================
# 28 AUGUST 2026
# ---------------------------------------------------------------------
# NOTE (1 Sep 2026): this slot should hold 31 AUGUST, the immediately
# preceding edition. It does not, and the reason is recorded rather than
# hidden: the 31 Aug PDF build used UNSUFFIXED fragment names
# (ed_s1.py / ed_s15.py / ed_s2.py) and the 1 Sep build overwrote them,
# per the handover's own "RENAME the *NNaug fragments back on copy"
# instruction. The tape and analysis sections for 31 Aug therefore have no
# surviving source, and reconstructing their tables from the PDF's extracted
# text would mean publishing re-keyed numbers as if they were sourced.
# 31 August remains fully present in the archive table and the score-history
# chart (edition PDF + annex, both downloadable). Rebuild it here only from
# a real source, never from OCR.
# =====================================================================
from ed28_block import ED28
EDITIONS['2026-08-28'] = ED28

# =====================================================================
# 1 SEPTEMBER 2026
# =====================================================================
from ed01sep_block import ED01SEP
EDITIONS['2026-09-01'] = ED01SEP


with open("editions.json", "w") as f:
    json.dump(EDITIONS, f, indent=2, ensure_ascii=False)

print("Wrote editions.json with full sections for:", list(EDITIONS.keys()))
