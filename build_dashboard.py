#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds index.html for the Iran-Hormuz War & US Economic Shock Monitor
dashboard, mirroring the FULL PDF format: all 9 numbered sections in the
same order, with the same tables and full narrative text (not a condensed
summary). Two extras beyond the PDF: a live toggle between the latest and
previous edition, and a score-history chart under a "Score history" panel.

Per-edition full-detail data lives in editions.json (embedded directly into
the HTML each run, per the "embed in HTML" choice) for just the two most
recent editions (the toggle). Three other data files are all regenerated
FROM YOUR SOURCE FILES, not hand-maintained, and also get embedded:

  - score_history.json  <- update_score_history.py reads every pdf/*.pdf
                            and extracts its actual score. Feeds the trend
                            chart AND the score column in the full archive
                            table.
  - gas_series.json      <- update_gas_series.py reads "US Iran BBG Data.xlsx"
                            directly (AUTMUSAG/USRFRUSA columns) via the same
                            robust column-scanning parser the PDF build uses.
                            Feeds the gasoline chart.
  - pdf_manifest.json    <- update_pdf_manifest.py scans pdf/*.pdf. Feeds the
                            "Full PDF editions" archive table (capped to the
                            newest ARCHIVE_LIMIT rows; every PDF in
                            the folder gets a row+download link, not just the
                            two in editions.json).

Each new edition:
  1. Run generate_editions.py after editing it with the new date's full
     section content (copy the newest entry's structure; keep only the
     two most recent dates in EDITIONS).
  2. Copy the new PDF into pdf/ (keep old ones too — the full archive table
     wants all of them). Then run:
       python3 update_score_history.py
       python3 update_pdf_manifest.py
  3. Run update_gas_series.py against the latest "US Iran BBG Data.xlsx".
  4. Re-run: python3 build_dashboard.py
  5. Commit + push index.html, editions.json, score_history.json,
     gas_series.json, pdf_manifest.json, and pdf/*.pdf to the repo.
"""
import json, base64, os

HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, "editions.json")) as f:
    editions = json.load(f)
with open(os.path.join(HERE, "score_history.json")) as f:
    score_history = json.load(f)
with open(os.path.join(HERE, "gas_series.json")) as f:
    gas_series = json.load(f)
with open(os.path.join(HERE, "pdf_manifest.json")) as f:
    pdf_manifest = json.load(f)

with open(os.path.join(HERE, "logo.png"), "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()

dates_sorted = sorted(editions.keys())
# How many rows the "Full PDF editions" archive table shows, newest first.
# Every PDF in pdf/ is still shipped and still downloadable by direct URL —
# this only caps what the table lists. Set to None to show all of them.
ARCHIVE_LIMIT = 7

latest_date = dates_sorted[-1]
previous_date = dates_sorted[-2] if len(dates_sorted) > 1 else None

DATA_JS = f"""
const EDITIONS = {json.dumps(editions, indent=2, ensure_ascii=False)};
const PDF_MANIFEST = {json.dumps(pdf_manifest, indent=2, ensure_ascii=False)};
const SCORE_HISTORY = {json.dumps(score_history, indent=2, ensure_ascii=False)};
const GAS_SERIES = {json.dumps(gas_series, indent=2, ensure_ascii=False)};
const LATEST_DATE = {json.dumps(latest_date)};
const PREVIOUS_DATE = {json.dumps(previous_date)};
const ARCHIVE_LIMIT = {json.dumps(ARCHIVE_LIMIT)};
"""

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Iran-Hormuz War &amp; US Economic Shock Monitor</title>
<script src="vendor/chart.umd.min.js"></script>
<style>
  :root{
    --navy:#1f3a5f; --hdr:#2c4a6e; --rule:#b8c4d2; --lgrey:#e9edf2;
    --grey:#666666; --amber:#c77f2e; --bg:#eef1f4; --paper:#ffffff; --ink:#1b2733;
    --crisis:#a6303a; --systemic:#c77f2e; --stress:#c9a227; --watch:#3c7a4e;
    --up:#a6303a; --down:#3c7a4e;
  }
  *{box-sizing:border-box;}
  body{
    margin:0; background:var(--bg); color:var(--ink);
    font-family:Helvetica,Arial,"Segoe UI",sans-serif;
    font-size:13.5px; line-height:1.52;
  }
  .sheet{max-width:900px; margin:0 auto 60px; background:var(--paper); box-shadow:0 0 0 1px var(--rule);}
  .pad{padding:26px 34px;}

  header.masthead{
    display:flex; align-items:center; gap:16px; flex-wrap:wrap;
    border-bottom:2px solid var(--rule); padding:16px 34px;
    position:sticky; top:0; background:var(--paper); z-index:10;
  }
  header.masthead img{height:40px; width:auto;}
  header.masthead .divider{width:1px; align-self:stretch; background:var(--rule);}
  header.masthead .title-block{flex:1; min-width:240px;}
  header.masthead h1{font-size:13.5px; margin:0 0 3px; font-weight:700; color:var(--navy); letter-spacing:.2px;}
  header.masthead .edition-line{font-size:10.5px; color:var(--grey);}
  .toggle-group{display:flex; gap:6px;}
  .toggle-btn{
    background:#fff; color:var(--navy); border:1px solid var(--rule);
    padding:6px 13px; border-radius:16px; font-size:11.5px; cursor:pointer; font-weight:700;
  }
  .toggle-btn.active{background:var(--navy); border-color:var(--navy); color:#fff;}

  .band-strip{display:flex; align-items:center; gap:14px; padding:14px 34px; border-bottom:1px solid var(--rule); background:var(--lgrey);}
  .band-strip .score-num{font-size:30px; font-weight:800; color:var(--navy);}
  .band-strip .score-den{font-size:13px; color:var(--grey); font-weight:600; margin-left:2px;}
  .band-badge{display:inline-block; padding:3px 12px; border-radius:12px; font-size:11px; font-weight:700; color:#fff; letter-spacing:.4px;}
  .band-crisis{background:var(--crisis);} .band-systemic{background:var(--systemic);}
  .band-stress{background:var(--stress); color:#3a2c00;} .band-watch{background:var(--watch);}
  .band-strip .session-note{font-size:11.5px; color:var(--grey);}

  h1.hj{font-size:11.5px; font-weight:700; color:var(--navy); margin:18px 0 6px; letter-spacing:.3px;}
  p.headline{font-size:12.5px; line-height:1.6;}
  p.headline b{color:var(--navy);}

  h2.section{color:var(--navy); font-size:13px; font-weight:700; border-bottom:2px solid var(--rule); padding-bottom:5px; margin:28px 0 12px;}
  h3.subsection{color:var(--navy); font-size:11.8px; font-weight:700; margin:16px 0 4px;}
  p.tablecaption{font-weight:700; font-size:12px; margin:14px 0 2px;}
  p.tablenote{font-size:10.5px; color:var(--grey); margin:0 0 6px;}
  p.body-text{font-size:12.3px; margin:6px 0;}
  p.item-lead{font-size:12.3px; margin:9px 0;}
  p.item-lead b{color:var(--navy);}

  table.mtable{width:100%; border-collapse:collapse; font-size:11px; margin-bottom:4px;}
  table.mtable th{background:var(--hdr); color:#fff; text-align:left; padding:6px 8px; font-size:10px; font-weight:700;}
  table.mtable td{padding:6px 8px; border:1px solid var(--rule); vertical-align:top;}
  table.mtable tr:nth-child(even) td{background:var(--lgrey);}
  table.mtable td.num{white-space:nowrap;}

  .pbar{background:var(--lgrey); border-radius:6px; overflow:hidden; height:7px; margin-top:3px;}
  .pbar span{display:block; height:100%; background:var(--amber);}

  .score-grid-total td{font-weight:700; background:#dfe6ee !important;}

  ul.plainlist{list-style:none; margin:6px 0; padding:0;}
  ul.plainlist li{font-size:12.3px; margin:8px 0; padding-left:14px; border-left:3px solid var(--amber);}
  ul.plainlist li b{color:var(--navy);}

  .chart-panel{border:1px solid var(--rule); border-radius:6px; padding:14px; margin:10px 0 4px; background:#fbfcfd;}
  .chart-panel .chart-note{font-size:10.5px; color:var(--grey); margin-top:8px;}

  td a.dl-link{display:inline-block; background:var(--navy); color:#fff; text-decoration:none; padding:5px 12px; border-radius:5px; font-size:11px; font-weight:600;}
  td a.dl-link:hover{background:var(--hdr);}

  footer.pagefoot{border-top:1px solid var(--rule); padding:14px 34px; font-size:10px; color:var(--grey); display:flex; justify-content:space-between;}
  @media (max-width:640px){
    .pad, header.masthead, .band-strip, footer.pagefoot{padding-left:16px; padding-right:16px;}
    table.mtable{font-size:10px;}
  }
</style>
</head>
<body>
<div class="sheet">
  <header class="masthead">
    <img src="data:image/png;base64,__LOGO_B64__" alt="Tecity logo">
    <div class="divider"></div>
    <div class="title-block">
      <h1>IRAN&ndash;HORMUZ WAR &amp; US ECONOMIC SHOCK MONITOR</h1>
      <div class="edition-line" id="editionLine"></div>
    </div>
    <div class="toggle-group" id="toggleGroup"></div>
  </header>

  <div class="band-strip">
    <span><span class="score-num" id="scoreNum">--</span><span class="score-den">/30</span></span>
    <span class="band-badge" id="bandBadge">--</span>
    <span class="session-note" id="seqLine"></span>
    <span class="session-note" id="sessionNote"></span>
  </div>

  <div class="pad">
    <h1 class="hj">HEADLINE JUDGMENT</h1>
    <p class="headline" id="headlineText"></p>

    <h2 class="section" id="sec1title">1 &middot; Live tape</h2>
    <p class="tablecaption">Oil and natural gas &mdash; Bloomberg front-month / active</p>
    <p class="tablenote" id="oilGasNote"></p>
    <table class="mtable"><thead><tr id="oilGasHead"></tr></thead><tbody id="oilGasBody"></tbody></table>

    <p class="tablecaption">US Treasuries and inflation expectations &mdash; Bloomberg</p>
    <p class="tablenote" id="ustNote"></p>
    <table class="mtable"><thead><tr id="ustHead"></tr></thead><tbody id="ustBody"></tbody></table>

    <p class="tablecaption">Cross-asset stress and political-transmission gauges &mdash; Bloomberg</p>
    <table class="mtable"><thead><tr id="crossHead"></tr></thead><tbody id="crossBody"></tbody></table>

    <p class="tablecaption">US retail gasoline &mdash; the two tracked series, 2026 year-to-date</p>
    <div class="chart-panel">
      <canvas id="gasChart" height="90"></canvas>
    </div>
    <p class="tablenote" id="gasChartNote"></p>

    <p class="tablecaption">Strait operational state</p>
    <table class="mtable"><thead><tr id="straitHead"></tr></thead><tbody id="straitBody"></tbody></table>

    <h2 class="section">2 &middot; US economic shock &mdash; analysis with bond yields</h2>
    <p class="body-text" id="analysisIntro"></p>

    <h3 class="subsection">2.1 &middot; Bond-yield transmission</h3>
    <p class="tablenote" id="bondYieldNote"></p>
    <div id="bondYieldItems"></div>

    <h3 class="subsection">2.2 &middot; What would push the shock to Stage 4</h3>
    <p class="tablenote" id="stage4Note"></p>
    <div id="stage4Items"></div>

    <h3 class="subsection">2.3 &middot; Cross-asset</h3>
    <p class="body-text" id="analysisCrossAsset"></p>

    <h2 class="section">3 &middot; Shock score</h2>
    <p class="body-text" id="scoreGridCaption"></p>
    <table class="mtable">
      <thead><tr><th style="width:16%">Channel</th><th style="width:8%">Score</th><th style="width:52%">Rationale</th><th style="width:24%">Triggers</th></tr></thead>
      <tbody id="scoreGridBody"></tbody>
    </table>

    <div class="chart-panel">
      <canvas id="scoreChart" height="80"></canvas>
      <div class="chart-note">Score history (web-only addition, not in the PDF) &mdash; every point is the confirmed score read from an archived edition PDF (12 Jun 2026 onward). Bands: 0&ndash;7 watch &middot; 8&ndash;14 stress &middot; 15&ndash;21 systemic-risk watch &middot; 22&ndash;30 crisis.</div>
    </div>

    <h2 class="section" id="sec4title">4 &middot; What's changed</h2>
    <div id="whatsChangedItems"></div>

    <h2 class="section">5 &middot; Scenario map &middot; next 7 to 30 days</h2>
    <table class="mtable">
      <thead><tr><th style="width:22%">Scenario</th><th style="width:10%">P</th><th style="width:38%">Description</th><th style="width:30%">Market path</th></tr></thead>
      <tbody id="scenarioBody"></tbody>
    </table>
    <p class="tablenote" id="scenarioShift"></p>

    <h2 class="section">6 &middot; Watchlist &middot; next 24&ndash;72 hours</h2>
    <ul class="plainlist" id="watchlist"></ul>

    <h2 class="section">7 &middot; Source log &middot; this edition</h2>
    <p class="body-text"><b>Tier 1 &mdash; primary market data.</b> <span id="tier1Market"></span></p>
    <p class="body-text"><b>Tier 1 &mdash; news and institutional.</b> <span id="tier1News"></span></p>
    <p class="body-text"><b>Tier 3 &mdash; state media and combatant claims (labelled).</b> <span id="tier3"></span></p>

    <h2 class="section">8 &middot; On-demand update protocol</h2>
    <table class="mtable">
      <thead><tr><th style="width:6%">#</th><th style="width:28%">Step</th><th style="width:66%">Detail</th></tr></thead>
      <tbody id="protocolBody"></tbody>
    </table>

    <h2 class="section">9 &middot; Methodology</h2>
    <p class="body-text"><b>Shock-score scale.</b> <span id="methScale"></span></p>
    <p class="body-text" id="methScaleCapP"><b>Scale cap.</b> <span id="methScaleCap"></span></p>
    <p class="body-text" id="methIntegrityP"><b>Data integrity this edition.</b> <span id="methIntegrity"></span></p>
    <p class="body-text"><b>Gasoline series.</b> <span id="methGasoline"></span></p>
    <p class="body-text"><b>Pre-war anchor (27 Feb 2026 close).</b> <span id="methAnchor"></span></p>
    <p class="body-text"><b>Intraday caveat.</b> <span id="methIntraday"></span></p>

    <h2 class="section">Full PDF editions</h2>
    <p class="tablenote" id="archiveNote"></p>
    <table class="mtable">
      <thead><tr><th style="width:20%">Edition</th><th style="width:14%">Score</th><th style="width:20%">Band</th><th style="width:46%">Download</th></tr></thead>
      <tbody id="archiveBody"></tbody>
    </table>
  </div>

  <footer class="pagefoot">
    <span>Prepared by PMST Claude Agent</span>
    <span id="footRight"></span>
  </footer>
</div>

<script>
__DATA_JS__

function bandClass(band){
  if(band==='CRISIS') return 'band-crisis';
  if(band==='SYSTEMIC-RISK WATCH'||band==='SYSTEMIC') return 'band-systemic';
  if(band==='STRESS') return 'band-stress';
  return 'band-watch';
}
function bandForScore(s){
  if(s>=22) return 'CRISIS';
  if(s>=15) return 'SYSTEMIC-RISK WATCH';
  if(s>=8) return 'STRESS';
  return 'WATCH';
}
const SCORE_BY_DATE = {};
SCORE_HISTORY.forEach(r=>{ SCORE_BY_DATE[r.date] = r.score; });
function esc(s){ return (s===undefined||s===null) ? '' : s; }
function rowHtml(cells, header){
  const tag = header ? 'th' : 'td';
  return cells.map(c=>`<${tag}>${esc(c)}</${tag}>`).join('');
}
function fillTable(rows, tbodyId){
  const tb = document.getElementById(tbodyId);
  tb.innerHTML = '';
  rows.forEach(r=>{
    const tr = document.createElement('tr');
    tr.innerHTML = rowHtml(r,false);
    tb.appendChild(tr);
  });
}

let currentDate = LATEST_DATE;

function renderToggle(){
  const dates = Object.keys(EDITIONS).sort().reverse();
  const g = document.getElementById('toggleGroup');
  g.innerHTML = '';
  dates.forEach(d=>{
    const b = document.createElement('button');
    b.className = 'toggle-btn' + (d===currentDate?' active':'');
    b.textContent = (d===LATEST_DATE?'Latest · ':'') + EDITIONS[d].label;
    b.onclick = ()=>{ currentDate = d; render(); };
    g.appendChild(b);
  });
}

function render(){
  const ed = EDITIONS[currentDate];
  renderToggle();
  document.getElementById('editionLine').textContent = ed.editionLine;
  document.getElementById('scoreNum').textContent = ed.score;
  const bb = document.getElementById('bandBadge');
  bb.textContent = ed.band + ' BAND';
  bb.className = 'band-badge ' + bandClass(ed.band);
  document.getElementById('seqLine').textContent = 'Sequencing ' + ed.sequencing;
  document.getElementById('sessionNote').textContent = ed.sessionNote;
  document.getElementById('headlineText').innerHTML = '<b>' + ed.headline + '</b>';

  // Section 1 — live tape
  document.getElementById('oilGasNote').textContent = ed.tape.note;
  fillTable([ed.tape.oilGasHeader], 'oilGasHead');
  document.getElementById('oilGasHead').innerHTML = rowHtml(ed.tape.oilGasHeader, true);
  fillTable(ed.tape.oilGas, 'oilGasBody');

  document.getElementById('ustNote').textContent = ed.tape.ustNote;
  document.getElementById('ustHead').innerHTML = rowHtml(ed.tape.ustHeader, true);
  fillTable(ed.tape.ust, 'ustBody');

  document.getElementById('crossHead').innerHTML = rowHtml(ed.tape.crossHeader, true);
  fillTable(ed.tape.cross, 'crossBody');

  document.getElementById('gasChartNote').textContent = ed.tape.gasChartNote;

  document.getElementById('straitHead').innerHTML = rowHtml(ed.tape.straitHeader, true);
  fillTable(ed.tape.strait, 'straitBody');

  // Section 2 — analysis
  document.getElementById('analysisIntro').textContent = ed.analysis.intro;
  document.getElementById('bondYieldNote').textContent = ed.analysis.bondYieldNote;
  const byWrap = document.getElementById('bondYieldItems');
  byWrap.innerHTML = '';
  ed.analysis.bondYield.forEach(it=>{
    const p = document.createElement('p');
    p.className = 'item-lead';
    p.innerHTML = '<b>' + it.title + '</b> ' + it.text;
    byWrap.appendChild(p);
  });
  document.getElementById('stage4Note').textContent = ed.analysis.stage4Note;
  const s4Wrap = document.getElementById('stage4Items');
  s4Wrap.innerHTML = '';
  ed.analysis.stage4.forEach(it=>{
    const p = document.createElement('p');
    p.className = 'item-lead';
    p.innerHTML = '<b>' + it.title + '</b> ' + it.text;
    s4Wrap.appendChild(p);
  });
  document.getElementById('analysisCrossAsset').textContent = ed.analysis.crossAsset;

  // Section 3 — score grid
  document.getElementById('scoreGridCaption').innerHTML = '<b>Total: ' + ed.score + '/30 &mdash; ' + ed.band + ' band.</b> Band thresholds: 0&ndash;7 watch &middot; 8&ndash;14 stress &middot; 15&ndash;21 systemic-risk watch &middot; 22&ndash;30 crisis.';
  const sgb = document.getElementById('scoreGridBody');
  sgb.innerHTML = '';
  ed.channels.forEach(ch=>{
    const tr = document.createElement('tr');
    tr.innerHTML = `<td><b>${ch.name}</b></td><td class="num">${ch.score}/5</td><td>${ch.rationale}</td><td>&uarr; ${ch.upgrade}<br>&darr; ${ch.downgrade}</td>`;
    sgb.appendChild(tr);
  });
  const totalTr = document.createElement('tr');
  totalTr.className = 'score-grid-total';
  totalTr.innerHTML = `<td>TOTAL</td><td class="num">${ed.score}/30</td><td colspan="2">${ed.scoreTotal}</td>`;
  sgb.appendChild(totalTr);

  // Section 4 — what's changed
  document.getElementById('sec4title').innerHTML = ed.whatsChanged.title;
  const wcWrap = document.getElementById('whatsChangedItems');
  wcWrap.innerHTML = '';
  ed.whatsChanged.items.forEach(txt=>{
    const p = document.createElement('p');
    p.className = 'item-lead';
    p.textContent = txt;
    wcWrap.appendChild(p);
  });

  // Section 5 — scenarios
  const scb = document.getElementById('scenarioBody');
  scb.innerHTML = '';
  ed.scenarios.forEach(s=>{
    const tr = document.createElement('tr');
    tr.innerHTML = `<td><b>${s.name}</b></td><td class="num">${s.p}%<div class="pbar"><span style="width:${s.p}%"></span></div></td><td>${s.desc}</td><td>${s.path}</td>`;
    scb.appendChild(tr);
  });
  document.getElementById('scenarioShift').textContent = ed.scenarioShift;

  // Section 6 — watchlist
  const wl = document.getElementById('watchlist');
  wl.innerHTML = '';
  ed.watchlist.forEach(w=>{
    const li = document.createElement('li');
    li.textContent = w;
    wl.appendChild(li);
  });

  // Section 7 — source log
  document.getElementById('tier1Market').textContent = ed.sourceLog.tier1Market;
  document.getElementById('tier1News').textContent = ed.sourceLog.tier1News;
  document.getElementById('tier3').textContent = ed.sourceLog.tier3;

  // Section 8 — protocol
  const prb = document.getElementById('protocolBody');
  prb.innerHTML = '';
  ed.protocol.forEach((p,i)=>{
    const tr = document.createElement('tr');
    tr.innerHTML = `<td class="num">${i+1}</td><td><b>${p.step}</b></td><td>${p.detail}</td>`;
    prb.appendChild(tr);
  });

  // Section 9 — methodology
  document.getElementById('methScale').textContent = ed.methodology.scale;
  // Optional paragraphs — present from the 30 Jul 2026 edition onward. Hidden
  // entirely for earlier editions rather than rendering "undefined".
  [['methScaleCap','scaleCap'],['methIntegrity','integrity']].forEach(([id,key])=>{
    const val = ed.methodology[key];
    document.getElementById(id+'P').style.display = val ? '' : 'none';
    document.getElementById(id).textContent = val || '';
  });
  document.getElementById('methGasoline').textContent = ed.methodology.gasoline;
  document.getElementById('methAnchor').textContent = ed.methodology.anchor;
  document.getElementById('methIntraday').textContent = ed.methodology.intraday;

  // Full PDF archive — every PDF in pdf/, joined against its own extracted score
  const ab = document.getElementById('archiveBody');
  ab.innerHTML = '';
  const archiveRows = (ARCHIVE_LIMIT === null || ARCHIVE_LIMIT === undefined)
    ? PDF_MANIFEST
    : PDF_MANIFEST.slice(0, ARCHIVE_LIMIT);
  archiveRows.forEach(p=>{
    const score = SCORE_BY_DATE[p.date];
    const band = score!==undefined ? bandForScore(score) : '—';
    const tr = document.createElement('tr');
    tr.innerHTML = `<td><b>${p.label}</b></td><td class="num">${score!==undefined?score+'/30':'—'}</td>` +
      `<td><span class="band-badge ${bandClass(band)}" style="font-size:9.5px;padding:2px 8px;">${band}</span></td>` +
      `<td><a class="dl-link" href="pdf/${p.filename}" target="_blank" rel="noopener">Edition PDF</a>` +
      (p.annex ? ` &middot; <a class="dl-link" href="annex/${p.annex}" target="_blank" rel="noopener">Annex</a>` : '') +
      `</td>`;
    ab.appendChild(tr);
  });

  const shownCount = archiveRows.length, totalCount = PDF_MANIFEST.length;
  document.getElementById('archiveNote').innerHTML = (shownCount < totalCount
      ? `The <b>${shownCount}</b> most recent archived editions, newest first. `
        + `${totalCount} editions are archived in total and the full run is charted above; `
        + `older PDFs remain in the <code>pdf/</code> folder and stay reachable by direct link. `
      : 'Every archived PDF in the folder, most recent first. ')
    + "Score is read directly from that edition's own PDF (see <code>update_score_history.py</code>). "
    + "From 21 Aug 2026 an edition may carry a companion <b>Annex</b> holding the full evidence, "
    + "source log and methodology; where one exists it is linked beside the edition.";

  document.getElementById('footRight').textContent = ed.editionLine;
}

// Peak-score and current-score markers + labels, mirroring the gas chart's
// GAS_ANNOTATIONS pattern (dot marker, value+date label, edge-clip guard).
const SCORE_ANNOTATIONS = {
  id: 'scoreAnnotations',
  afterDatasetsDraw(chart){
    const {ctx, chartArea:{top}, scales:{x, y}} = chart;
    const dates = SCORE_HISTORY.map(r=>r.date);
    const vals = SCORE_HISTORY.map(r=>r.score);

    ctx.save();

    // resolve() answers "which side will this label actually end up on",
    // accounting for the top-edge clip guard, WITHOUT drawing anything. The
    // caller needs this to keep two labels off the same side.
    function resolve(idx, direction){
      const py = y.getPixelForValue(vals[idx]);
      if(direction === 'above' && (py - 14) - 8 < top) return 'below';
      return direction;
    }

    function drawPoint(idx, color, text, direction, stack){
      const px = x.getPixelForValue(idx);
      const py = y.getPixelForValue(vals[idx]);
      ctx.beginPath();
      ctx.arc(px, py, 3, 0, Math.PI*2);
      ctx.fillStyle = color;
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 1;
      ctx.stroke();
      ctx.font = 'bold 9.5px Helvetica';
      ctx.fillStyle = color;
      ctx.textAlign = px > x.right - 95 ? 'right' : 'left';
      const tx = ctx.textAlign === 'right' ? px - 7 : px + 7;
      const resolved = resolve(idx, direction);
      let ty = resolved === 'above' ? py - 14 : py + 20;
      ty += (stack || 0);          // extra line offset when both labels share a side
      ctx.fillText(text, tx, ty);
      return resolved;
    }

    let peakIdx = 0;
    vals.forEach((v,i)=>{ if(v > vals[peakIdx]) peakIdx = i; });
    const curIdx = vals.length - 1;
    // if the peak and the current reading land close together on the x-axis,
    // force them to opposite sides so the two labels don't overlap
    const closeTogether = Math.abs(curIdx - peakIdx) <= 3;

    if(peakIdx === curIdx){
      // the latest reading IS the all-time peak — one marker, one combined label,
      // otherwise the two labels print on top of each other
      drawPoint(curIdx, '#c77f2e', `peak & current ${vals[curIdx]}/30 · ${shortDate(dates[curIdx])}`, 'above');
    } else {
      const peakSide = drawPoint(peakIdx, '#1f3a5f', `peak ${vals[peakIdx]}/30 · ${shortDate(dates[peakIdx])}`, 'above');
      // put the current label on the side the peak label did NOT end up on
      const want = closeTogether ? (peakSide === 'above' ? 'below' : 'above') : 'above';
      // ...but the top-edge clip guard can force it straight back onto the peak's
      // side (both labels high on the y-axis, e.g. a peak set one session before
      // the latest reading at the same score). Ask where it would actually land,
      // and if that is the same side, stack it a line clear instead of overprinting.
      const curSide = resolve(curIdx, want);
      const stack = (closeTogether && curSide === peakSide) ? 13 : 0;
      drawPoint(curIdx, '#c77f2e', `current ${vals[curIdx]}/30 · ${shortDate(dates[curIdx])}`, curSide, stack);
    }

    ctx.restore();
  }
};

let scoreChartInstance, gasChartInstance;
function renderScoreChart(){
  const ctx = document.getElementById('scoreChart').getContext('2d');
  if(scoreChartInstance) scoreChartInstance.destroy();
  scoreChartInstance = new Chart(ctx, {
    type:'line',
    data:{
      labels: SCORE_HISTORY.map(r=>r.date),
      datasets:[{
        label:'Shock score', data: SCORE_HISTORY.map(r=>r.score),
        borderColor:'#1f3a5f', backgroundColor:'rgba(31,58,95,0.08)',
        fill:true, tension:0.15, pointRadius:2.5, pointBackgroundColor:'#1f3a5f'
      }]
    },
    plugins:[SCORE_ANNOTATIONS],
    options:{
      responsive:true,
      layout:{ padding:{ top: 18, right: 66, bottom: 4 } },
      plugins:{legend:{display:false}, tooltip:{callbacks:{afterLabel:c=>SCORE_HISTORY[c.dataIndex].driver}}},
      scales:{y:{min:0,max:30,ticks:{stepSize:5,font:{size:9}}, grid:{color:'#e9edf2'}}, x:{ticks:{font:{size:8}}, grid:{display:false}}}
    }
  });
}
function shortDate(iso){
  const months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  const d = new Date(iso+'T00:00:00');
  return d.getDate()+' '+months[d.getMonth()];
}

// Custom draw-on-canvas plugin (no extra vendored dependency) replicating the
// PDF chart's annotations: a dashed "war start 28 Feb" line, a peak marker +
// label per series, and a latest-value label per series.
const GAS_ANNOTATIONS = {
  id: 'gasAnnotations',
  afterDatasetsDraw(chart){
    const {ctx, chartArea:{top, bottom}, scales:{x, y}} = chart;
    const labels = chart.data.labels;
    const aaaDates = GAS_SERIES.aaa.map(r=>r.date), aaaVals = GAS_SERIES.aaa.map(r=>r.v);
    const doeDates = GAS_SERIES.doe.map(r=>r.date), doeVals = GAS_SERIES.doe.map(r=>r.v);

    function idxForDate(target){
      const exact = labels.indexOf(target);
      if(exact !== -1) return exact;
      let best=0, bestDiff=Infinity;
      labels.forEach((d,i)=>{
        const diff = Math.abs(new Date(d) - new Date(target));
        if(diff < bestDiff){ bestDiff = diff; best = i; }
      });
      return best;
    }

    ctx.save();

    // --- war-start vertical dashed line ---
    const warIdx = idxForDate('2026-02-28');
    const warX = x.getPixelForValue(warIdx);
    ctx.strokeStyle = '#8a94a0';
    ctx.setLineDash([4,3]);
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(warX, top);
    ctx.lineTo(warX, bottom);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.save();
    ctx.translate(warX - 5, top + 2);
    ctx.rotate(-Math.PI/2);
    ctx.fillStyle = '#666666';
    ctx.font = '10px Helvetica';
    ctx.textAlign = 'right'; // anchor at top+2, text extends DOWN into the chart (not up off the canvas)
    ctx.fillText('war start 28 Feb', 0, 0);
    ctx.restore();

    // --- peak markers ---
    // direction is forced per series (rather than auto-picked) so the two
    // peak labels never land in the same vertical band even when the two
    // peaks fall close together on the x-axis (as AAA's 20 May and DOE's
    // 11 May do) — AAA peak always renders above its dot, DOE always below.
    function drawPeak(dates, vals, color, direction){
      let peakIdx = 0;
      vals.forEach((v,i)=>{ if(v > vals[peakIdx]) peakIdx = i; });
      const px = x.getPixelForValue(idxForDate(dates[peakIdx]));
      const py = y.getPixelForValue(vals[peakIdx]);
      ctx.beginPath();
      ctx.arc(px, py, 3, 0, Math.PI*2);
      ctx.fillStyle = color;
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 1;
      ctx.stroke();
      const text = `peak $${vals[peakIdx].toFixed(2)} · ${shortDate(dates[peakIdx])}`;
      ctx.font = 'bold 9.5px Helvetica';
      ctx.fillStyle = color;
      ctx.textAlign = px > x.right - 95 ? 'right' : 'left';
      const tx = ctx.textAlign === 'right' ? px - 7 : px + 7;
      let resolved = direction;
      let ty = direction === 'above' ? py - 14 : py + 20;
      if(direction === 'above' && ty - 8 < top){ ty = py + 20; resolved = 'below'; } // flip if it would clip the top edge
      ctx.fillText(text, tx, ty);
      return resolved;
    }
    drawPeak(aaaDates, aaaVals, '#1f3a5f', 'above');
    drawPeak(doeDates, doeVals, '#c77f2e', 'below');

    // --- latest-value labels ---
    function drawLast(dates, vals, color, decimals, dy){
      const i = dates.length - 1;
      const px = x.getPixelForValue(idxForDate(dates[i]));
      const py = y.getPixelForValue(vals[i]);
      ctx.beginPath();
      ctx.arc(px, py, 2.6, 0, Math.PI*2);
      ctx.fillStyle = color;
      ctx.fill();
      ctx.font = 'bold 10px Helvetica';
      ctx.fillStyle = color;
      ctx.textAlign = 'left';
      ctx.fillText(`$${vals[i].toFixed(decimals)} · ${shortDate(dates[i])}`, px + 7, py + dy);
    }
    drawLast(aaaDates, aaaVals, '#1f3a5f', 2, 3);
    drawLast(doeDates, doeVals, '#c77f2e', 3, 3);

    ctx.restore();
  }
};

function renderGasChart(){
  const ctx = document.getElementById('gasChart').getContext('2d');
  if(gasChartInstance) gasChartInstance.destroy();
  gasChartInstance = new Chart(ctx, {
    type:'line',
    data:{
      labels: GAS_SERIES.aaa.map(r=>r.date),
      datasets:[
        {label:'AAA all-grades retail (daily)', data: GAS_SERIES.aaa.map(r=>({x:r.date,y:r.v})), borderColor:'#1f3a5f', backgroundColor:'#1f3a5f', pointRadius:0, tension:0.1},
        {label:'DOE regular retail spot (weekly)', data: GAS_SERIES.doe.map(r=>({x:r.date,y:r.v})), borderColor:'#c77f2e', backgroundColor:'#c77f2e', pointRadius:3, tension:0.1}
      ]
    },
    plugins:[GAS_ANNOTATIONS],
    options:{
      responsive:true, parsing:false,
      layout:{ padding:{ right: 78, top: 16, bottom: 22 } },
      plugins:{legend:{labels:{font:{size:9}}}},
      scales:{
        x:{
          type:'category',
          // one tick per calendar month, formatted "mmm/yy" — filtering to
          // month-start indices (rather than relying on autoSkip) keeps the
          // spacing clean regardless of how many daily/weekly points exist
          afterBuildTicks: scale => {
            const labels = scale.chart.data.labels;
            const monthStarts = [];
            let lastKey = null;
            labels.forEach((d,i)=>{
              const key = d.slice(0,7);
              if(key !== lastKey){ monthStarts.push(i); lastKey = key; }
            });
            scale.ticks = monthStarts.map(i=>({value:i}));
          },
          ticks:{
            autoSkip:false, font:{size:9}, maxRotation:0, minRotation:0,
            callback: function(value){
              const label = this.getLabelForValue(value);
              const months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
              const d = new Date(label+'T00:00:00');
              return months[d.getMonth()] + '/' + String(d.getFullYear()).slice(-2);
            }
          },
          grid:{display:false}
        },
        y:{
          min:2.5, max:5.5,
          title:{ display:true, text:'US$', font:{size:10, weight:'bold'}, color:'#666666' },
          ticks:{ font:{size:9}, callback: v => '$'+v.toFixed(2) },
          grid:{color:'#e9edf2'}
        }
      }
    }
  });
}

render();
renderScoreChart();
renderGasChart();
</script>
</body>
</html>
"""

html = HTML.replace("__LOGO_B64__", logo_b64).replace("__DATA_JS__", DATA_JS)

out_path = os.path.join(HERE, "index.html")
with open(out_path, "w") as f:
    f.write(html)

print("Built", out_path, "for edition", latest_date, "(previous:", previous_date, ")")
