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
# 1 SEPTEMBER 2026
# ---------------------------------------------------------------------
# NOTE: 28 August was dropped from the toggle on 2 September, per the
# two-editions-only rule. It remains fully present in the archive table
# and the score-history chart (edition PDF + annex, both downloadable),
# and ed28_block.py stays on disk unimported.
# 31 August is still absent from the toggle and the reason stands: the
# 31 Aug PDF build used UNSUFFIXED fragment names and the 1 Sep build
# overwrote them, so its tape and analysis sections have no surviving
# source. Rebuild it here only from a real source, never from OCR.
# From the 2 September build every fragment is DATE-SUFFIXED, so this
# cannot recur.
# =====================================================================
from ed01sep_block import ED01SEP
EDITIONS['2026-09-01'] = ED01SEP

# =====================================================================
# 2 SEPTEMBER 2026
# =====================================================================
from ed02sep_block import ED02SEP
EDITIONS['2026-09-02'] = ED02SEP


with open("editions.json", "w") as f:
    json.dump(EDITIONS, f, indent=2, ensure_ascii=False)

print("Wrote editions.json with full sections for:", list(EDITIONS.keys()))
