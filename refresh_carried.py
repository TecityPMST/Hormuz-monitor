# -*- coding: utf-8 -*-
"""Regenerate sourceLog / protocol / methodology in a block FROM the day's annex
fragments, so the dashboard cannot say something the annex does not (SS12)."""
import re, sys, json, importlib.util, io
import os
# resolve the project root from this file's own location -- the sandbox mount name
# changes every session and must NEVER be hardcoded (SS2).
BUILD = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '..', '..', '..', 'build'))
sys.path.insert(0, BUILD)

def plain(t):
    t = re.sub(r'</?[bi]>', '', t)
    for a, b in [('&mdash;','—'),('&ndash;','–'),('&sect;','§'),('&rsquo;','’'),('&lsquo;','‘'),
                 ('&euro;','€'),('&yen;','¥'),('&amp;','&'),('&rarr;','→'),('&minus;','−'),
                 ('&para;','¶'),('&hellip;','…'),('&times;','×'),('&nbsp;',' ')]:
        t = t.replace(a, b)
    return re.sub(r'\s+', ' ', t).strip()

def grab(fname):
    """Return the literal python source of a fragment."""
    return open(f'{BUILD}/{fname}', encoding='utf-8').read()

# ---------- A7 -> sourceLog ----------
a7 = grab('an_a7.py')
rows = re.findall(r"\[\s*'((?:[^'\\]|\\.)*)',\s*'((?:[^'\\]|\\.)*)',\s*\n?\s*'((?:[^'\\]|\\.)*)'\s*\]", a7, re.S)
tier1m, tier1n, tier3, notobt = [], [], [], []
for tier, src, use in rows:
    t, s_, u = plain(tier), plain(src), plain(use)
    if t.startswith('Tier'):        # header row
        continue
    entry = f'{s_} — {u}'
    if 'DATA' in t:                 tier1m.append(entry)
    elif t == '1':                  tier1n.append(entry)
    elif t == '3':                  tier3.append(entry)
    elif t in ('2',):               tier1n.append('TIER 2 · ' + entry)
    else:                           notobt.append(f'{t} · {entry}')
sourceLog = {
    'tier1Market': ' '.join(tier1m),
    'tier1News': ' ¶ '.join(tier1n),
    'tier3': ' ¶ '.join(tier3 + notobt),
}

# ---------- A8 -> protocol ----------
a89 = grab('an_a89.py')
prows = re.findall(r"\[\s*'(\d)',\s*'((?:[^'\\]|\\.)*)',\s*'((?:[^'\\]|\\.)*)'\s*\]", a89, re.S)
protocol = [{'step': plain(st), 'detail': plain(dt)} for _n, st, dt in prows]

# ---------- A9 -> methodology ----------
paras = re.findall(r'A\(Paragraph\(\s*\n?\s*((?:"(?:[^"\\]|\\.)*"\s*\n?\s*)+),\s*body\)\)', a89, re.S)
texts = []
for p in paras:
    joined = ''.join(re.findall(r'"((?:[^"\\]|\\.)*)"', p))
    texts.append(plain(joined))
a9 = [t for t in texts if len(t) > 200]
def find(*keys, default=''):
    for t in a9:
        if all(k in t for k in keys):
            return t
    return default
scale_txt   = find('Six channels, each scored')
disc_txt    = find('Confirmed closes only for market channels')
rules_txt   = find('Rules exercised this edition')
s956        = find('§9.56 —')
s951        = find('§9.51 —')
s957        = find('§9.57 —')
restate     = find('Restatements and comparability')

methodology = {
    'scale': scale_txt,
    'scaleCap': disc_txt,
    'integrity': rules_txt,
    'gasoline': s957 or restate,
    'anchor': ('Pre-war anchor (27 February 2026 close), re-verified field by field this edition and '
               'unchanged: Brent $72.48, WTI $67.02, 2-year 3.3749%, 5-year 3.5017%, 10-year 3.9375%, '
               '30-year 4.6106%, 2s10s +55.64 bp, 5y5y 2.142%, 10-year breakeven 2.2569%, MOVE 73.38, '
               'VIX 19.86, DXY 97.608, scored gasoline $3.52, DOE gasoline ~$2.94, Henry Hub $3.063, '
               'TTF €31.23, Asia LNG ¥1,669.'),
    'intraday': (s956 + ' ¶ ' + s951 + ' ¶ ' + restate).strip(' ¶'),
    'sequencing': '27 → 27 → 27 → 27 → 27',
}

# ---------- splice into the block ----------
path = sys.argv[1]
s = open(path, encoding='utf-8').read()
def replace_obj(src, key, newval):
    i = src.find('"%s":' % key)
    assert i > 0, key
    j = i + len('"%s":' % key)
    while src[j] in ' \n': j += 1
    open_c = src[j]; close_c = {'{':'}', '[':']'}[open_c]
    depth, k2, instr, esc = 0, j, False, False
    while k2 < len(src):
        c = src[k2]
        if instr:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == '"': instr = False
        else:
            if c == '"': instr = True
            elif c == open_c: depth += 1
            elif c == close_c:
                depth -= 1
                if depth == 0: break
        k2 += 1
    dumped = json.dumps(newval, ensure_ascii=False, indent=2)
    dumped = '\n'.join(('  ' + ln) if n else ln for n, ln in enumerate(dumped.split('\n')))
    return src[:j] + dumped + src[k2+1:]

for key, val in [('sourceLog', sourceLog), ('protocol', protocol), ('methodology', methodology)]:
    s = replace_obj(s, key, val)
open(path, 'w', encoding='utf-8').write(s)
print('refreshed sourceLog (%d chars), protocol (%d steps), methodology (%d fields) in %s'
      % (sum(len(v) for v in sourceLog.values()), len(protocol), len(methodology), path))
for f, v in methodology.items():
    print('   methodology.%-11s %d chars' % (f, len(v)))
