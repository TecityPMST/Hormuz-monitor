#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebuilds gas_series.json (the "US retail gasoline — the two tracked series"
chart) directly from the Bloomberg extract "US Iran BBG Data.xlsx" — the
same file, and the same robust column-scanning parser, that the daily PDF
build uses (see HORMUZ_MONITOR_INSTRUCTIONS.md section 3). This does NOT
hand-copy numbers: it reads the spreadsheet's header rows fresh every run,
so a relabelled ticker or inserted column doesn't silently break it.

Usage:
    python3 update_gas_series.py "/path/to/US Iran BBG Data.xlsx"

If no path is given, it looks for a file named "US Iran BBG Data.xlsx" in
this script's directory (convenient if you've staged/copied it alongside
the dashboard for a one-off run).
"""
import sys, os, json
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))

def find_input_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    candidate = os.path.join(HERE, "US Iran BBG Data.xlsx")
    if os.path.exists(candidate):
        return candidate
    sys.exit(
        "Usage: python3 update_gas_series.py \"/path/to/US Iran BBG Data.xlsx\"\n"
        "(or place a copy named 'US Iran BBG Data.xlsx' next to this script)"
    )

def robust_parse_gasoline(xlsx_path):
    raw = pd.read_excel(xlsx_path, header=None)

    # row0 = ticker labels, row1 = description, row2 = field (Close/High/Low), data from row3
    labs = [(ci, raw.iloc[0, ci].strip()) for ci in range(raw.shape[1])
            if isinstance(raw.iloc[0, ci], str) and raw.iloc[0, ci].strip() and ci > 0]
    labs = sorted(labs)
    bounds = {}
    for i, (ci, name) in enumerate(labs):
        nxt = labs[i + 1][0] if i + 1 < len(labs) else raw.shape[1]
        bounds[name] = (ci, nxt)

    def close_col(name):
        c0, c1 = bounds[name]
        for c in range(c0, c1):
            v = raw.iloc[2, c]
            if isinstance(v, str) and v.strip().lower() == "close":
                return c
        return c0

    # Ticker map per HORMUZ_MONITOR_INSTRUCTIONS.md section 3
    aaa_ticker = "AUTMUSAG Index" if "AUTMUSAG Index" in bounds else next(
        (n for n in bounds if n.split()[0] == "AUTMUSAG"), None)
    doe_ticker = "USRFRUSA Index" if "USRFRUSA Index" in bounds else next(
        (n for n in bounds if n.split()[0] == "USRFRUSA"), None)
    if not aaa_ticker or not doe_ticker:
        sys.exit(f"Could not find AUTMUSAG/USRFRUSA columns in {xlsx_path}. "
                  f"Tickers seen: {sorted(bounds.keys())}")

    dates = pd.to_datetime(raw.iloc[3:, 0], errors="coerce")
    aaa = pd.to_numeric(raw.iloc[3:, close_col(aaa_ticker)], errors="coerce")
    doe = pd.to_numeric(raw.iloc[3:, close_col(doe_ticker)], errors="coerce")

    df = pd.DataFrame({"date": dates, "GasAAA": aaa, "GasDOE": doe}).dropna(subset=["date"])
    df = df[df["date"] >= "2026-01-01"].reset_index(drop=True)
    return df

def main():
    xlsx_path = find_input_path()
    df = robust_parse_gasoline(xlsx_path)

    aaa_rows = df[["date", "GasAAA"]].dropna()
    doe_rows = df[["date", "GasDOE"]].dropna()

    out = {
        "source": "US Iran BBG Data.xlsx (AUTMUSAG / USRFRUSA, close, parsed 2026-01-01 onward)",
        "aaa": [{"date": d.strftime("%Y-%m-%d"), "v": float(v)} for d, v in zip(aaa_rows["date"], aaa_rows["GasAAA"])],
        "doe": [{"date": d.strftime("%Y-%m-%d"), "v": float(v)} for d, v in zip(doe_rows["date"], doe_rows["GasDOE"])],
    }

    out_path = os.path.join(HERE, "gas_series.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)

    print(f"Wrote {out_path}: {len(out['aaa'])} AAA points, {len(out['doe'])} DOE points "
          f"(latest AAA {out['aaa'][-1]['date']}=${out['aaa'][-1]['v']:.2f}, "
          f"latest DOE {out['doe'][-1]['date']}=${out['doe'][-1]['v']:.3f})")

if __name__ == "__main__":
    main()
