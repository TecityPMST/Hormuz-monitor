#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds editions.json with the FULL content of each PDF edition (all 9
sections, verbatim from the PDF build scripts / extracted PDF text) so the
HTML dashboard can mirror the PDF format exactly rather than a condensed
summary. Run once per edition change, then run build_dashboard.py.
"""
import json

EDITIONS = {}

# ======================================================================
# 2026-07-28 (previous)
# ======================================================================
EDITIONS['2026-07-28'] = {'label': '28 Jul 2026',
 'editionLine': 'Daily edition · 28 Jul 2026 intraday · Bloomberg · Singapore 28 Jul AM update',
 'score': 25,
 'band': 'CRISIS',
 'sequencing': '25 → 25 → 25',
 'sessionNote': 'Tenth session at 25',
 'headline': 'Note: 28 Jul figures are intraday prints; 27 Jul is now a final close ($85.87 Brent, down $5.81 from '
             "24 Jul's $91.68 close — the second consecutive daily decline and the fastest two-session unwind since "
             'the 2–3 Jul deal-hope window). Restated continuation series (front-month CO2/CL2) in force. Score '
             'HOLDS at 25/30 — all six channels unchanged, a TENTH session at 25 — and the de-escalation that began '
             'over the weekend is now confirmed on closes, not just intraday prints: Brent has fallen in '
             'back-to-back sessions ($94.26 → $91.68 → $85.87), $8.39 off the 23 Jul peak close, and prints $85.40 '
             'this morning (H 85.58 / L 84.96), a further 47-cent decline; the active COA contract, which touched '
             '$100.69 on Thursday, prints $87.94. The US strike pause has now held for three consecutive nights '
             '(25–27 Jul) — the longest of the war — while the naval blockade stays fully operational; Iran–Oman '
             'technical talks on Hormuz transit are advancing toward a framework in which Iran would manage vessel '
             'transit with fewer restrictions, closer to the June interim deal. Trump on Sunday dismissed concerns '
             'that US munitions stockpiles were running low, pushing back on the operational-necessity reading of '
             "the pause. Friday's inflation-complex divergence has partly reversed: 5Y5Y closed 27 Jul at 2.2617% — "
             "down from Friday's 2.2877%, the war's closest trigger approach — and prints 2.2603% this morning, now "
             "3.8 bp from the →5 line on a close basis rather than Friday's 1.2 bp. AAA gasoline's latest confirmed "
             'print is still $4.75 (24 Jul, a ninth consecutive rise) — sitting exactly AT the political→5 line but '
             'not through it — and the extract has now gone four sessions (25–28 Jul) without a fresh AAA print, the '
             "longest gap of the war outside the JGLA stale-carry episode; today's edition cannot say whether the "
             'run continued, stalled, or reversed with crude. The 10Y closed 27 Jul at 4.6487% — its first close '
             'back below the 4.65% Stage-4 leg after three consecutive closes above, by just 0.13 bp — and prints '
             '4.6345% this morning (1.55 bp below); the 30Y closed 5.1365% and prints 5.1239%, narrowing the cushion '
             "above the Treasury-channel's 5.00% downgrade line to 12.4 bp intraday even as it widens the gap to "
             "Stage-4 Threshold B's 5.20% upgrade line to 7.6 bp — the same rally is disarming the upside threshold "
             "and arming the downside one, simultaneously. MOVE's confirmed 27 Jul close ticked back up to 77.21 "
             "(+0.39 from Thursday's 76.82) — Friday's snap was one session, not a reversal — still 2.2 pts above "
             'the 75 downgrade leg, with no 28 Jul print yet. No trigger fired on a confirmed close, so no channel '
             'moved; with both event channels maxed, the hold is an artifact of the scale. Netanyahu meets Trump at '
             "the White House TODAY (11am ET, Iran foremost on the agenda) — the session's swing factor for whether "
             "the pause hardens or resets — and the FOMC's two-day meeting also opens today, with hike odds priced "
             "near 34%, up sharply from 13% a week earlier, against Chair Warsh's public line that inflation "
             "'remains too high.' Sequencing 25 → 25 → 25.",
 'tape': {'note': '28 Jul 2026 readings are intraday prints; 27 Jul and earlier are final closes (restated '
                  'continuation series; front-month CO2/CL2). d/d deltas are 28 Jul intraday vs 27 Jul close; w/w '
                  'deltas are vs 21 Jul close.',
          'oilGasHeader': ['Benchmark', 'Intraday 28 Jul', 'Δ d/d', 'Δ vs pre-war close (27 Feb)', 'BBG ticker'],
          'oilGas': [['Brent front-month',
                      '$85.40 /bbl (H 85.58 / L 84.96)',
                      '–$0.47 (–$3.12 w/w)',
                      "from $72.48 (+17.8%) — $12.92/bbl premium, down from the 23 Jul close's $21.78 peak premium; "
                      'active COA prints $87.94',
                      'CO2 Comdty (Close)'],
                     ['Brent · 27 Jul close (final)',
                      '$85.87 /bbl (–$2.01 vs my 27 Jul intraday $87.88)',
                      '–$5.81 d/d — second straight decline; US leg extended the Asia-session drop for a second '
                      'session',
                      '$13.39 below the $95 trigger on a close basis — the widest gap since 16 Jul; active COA '
                      'closed $88.36',
                      'CO2 Comdty (Close)'],
                     ['WTI front-month',
                      '$79.77 /bbl',
                      '–$0.48 (–$4.57 w/w)',
                      'from $67.02 (+19.0%) — the CL2 artifact persists: 27 Jul CL2 close $80.25 vs active CLA '
                      '$82.61; CLA prints $82.02 intraday',
                      'CL2 Comdty (Close)'],
                     ['Brent–WTI spread', '$5.63 /bbl', 'flat (+$0.01)', '~$5.9 on the active contracts', 'derived'],
                     ['Henry Hub natural gas',
                      '$2.751 /MMBtu',
                      '–$0.016 (–$0.114 w/w)',
                      'from $3.06 (–10.2%) — US gas further BELOW pre-war; not Hormuz-exposed',
                      'NGA Comdty (Close)'],
                     ['TTF Dutch gas (active)',
                      '€56.98 /MWh',
                      '–€1.27 (–€2.68 w/w)',
                      'from €31.23 (+82.5%) — the second straight session off the 24 Jul war-era record €63.58 (one '
                      "confirmed close plus this morning's print); €6.60 has now come out",
                      'TZTA Comdty (Close)'],
                     ['Japan/Asia LNG (27 Jul close — fresh print)',
                      '¥3,492',
                      '–¥101 vs the ¥3,593 24 Jul print',
                      'from ¥1,669 (+109.2%) — eased off the war-era record on its one fresh print since; no 28 Jul '
                      'print yet (flagged, not carried)',
                      'JGLA Comdty (Close)']],
          'ustNote': "28 Jul 2026 yields are intraday. d/d deltas are vs the 27 Jul close; w/w vs 21 Jul. The 10Y's "
                     "three-close-above run on Stage-4 Threshold B ended 27 Jul; the 30Y's gap to its own 5.00% "
                     'downgrade line narrowed to 12.4 bp intraday. See section 2.1 for the full read.',
          'ustHeader': ['Tenor',
                        'Yield (%) — intraday 28 Jul',
                        'Δ d/d (bp)',
                        'Δ w/w (bp)',
                        'Δ vs pre-war (bp)',
                        'BBG ticker'],
          'ust': [['2-year UST', '4.31', '–1.1', '+5.0', '+93.7 (from 3.37%)', 'USGG2YR Index'],
                  ['5-year UST', '4.39', '–1.2', '+2.3', '+89.1 (from 3.50%)', 'USGG5YR Index'],
                  ['10-year UST',
                   '4.63',
                   '–1.4',
                   '+0.6',
                   '+69.7 (from 3.94%) — 27 Jul close 4.6487%, FIRST close below the 4.65% Stage-4 leg after three '
                   'above',
                   'USGG10YR Index'],
                  ['30-year UST',
                   '5.12',
                   '–1.3',
                   '–0.7',
                   '+51.3 (from 4.61%) — 27 Jul close 5.1365%, 6.35 bp below the 5.20% leg, 13.65 bp above the 5.00% '
                   'leg',
                   'USGG30YR Index'],
                  ['2s10s spread', '+32.1 bp', '–0.4', '–4.2', '–23.6 (flatter)', 'USYC2Y10 Index'],
                  ['10Y breakeven inflation',
                   '2.203',
                   '+0.0',
                   '–6.7',
                   '–5.4 (from 2.257%) — 27 Jul close BELOW the pre-war anchor for a second session',
                   'USGGBE10 Index'],
                  ['5Y5Y forward inflation',
                   '2.260',
                   '–0.1',
                   '+4.1',
                   "+11.8 (from 2.14%) — 27 Jul close 2.2617%, back from Friday's 2.2877% peak; 3.8 bp from the →5 "
                   'line',
                   'USGG5Y5Y Index'],
                  ['SOFR (lagged print, 24 Jul)', '3.64', '—', '—', 'series lags', 'SOFRRATE Index']],
          'crossHeader': ['Gauge', 'Latest', 'As of', 'Δ vs pre-war', 'Interpretation'],
          'cross': [['DXY',
                     '101.51',
                     '28 Jul intraday',
                     '+3.90 (from 97.61)',
                     'Flat on the day; still no haven bid — the dollar remains a bystander, not the stress valve.'],
                    ['MOVE',
                     '77.21',
                     '27 Jul close (28 Jul lagged)',
                     '+3.83 (from 73.38)',
                     "Ticked back UP +0.39 from Thursday's 76.82 — one session's snap, not a reversal; 2.2 pts above "
                     'the 75 leg.'],
                    ['VIX',
                     '18.67',
                     '27 Jul close (28 Jul lagged)',
                     '–1.19 (from 19.86)',
                     'Steady into the pause; the 23 Jul tanker-attack snap has fully unwound.'],
                    ['AAA gasoline',
                     '$4.75 /gal',
                     '24 Jul print (latest; 25–28 Jul pending)',
                     '+$1.23 (from $3.52, +34.9%)',
                     'Political-stress reference. NINTH consecutive rise, sitting exactly AT $4.75, not through it. '
                     'Four sessions pending — longest gap outside JGLA.'],
                    ['DOE gasoline',
                     '$4.001 /gal',
                     '20 Jul weekly print',
                     '+$1.06 (from ~$2.94, +36%)',
                     'The 27 Jul weekly print has NOT landed — a second corroboration series now also pending.']],
          'gasChartNote': 'AUTMUSAG (AAA all-grades retail pump, daily) is the political-stress score reference '
                          '(pre-war $3.52, peak $5.18, latest $4.75 on 24 Jul); USRFRUSA (DOE regular-grade retail '
                          'spot, weekly) is the complementary gauge (pre-war ~$2.94, peak $4.50, latest $4.001 on 20 '
                          'Jul; the 27 Jul print is overdue). Both series have gone dark since 24–25 Jul — the '
                          'longest simultaneous gap of the war — and the channel holds at 4 until fresh confirmed '
                          'data lands.',
          'straitHeader': ['Indicator', 'Current reading', 'Source'],
          'strait': [['Strait closed · day ~150',
                      'Closed since 28 Feb; naval blockade plus escort operation (12 vessels redirected, two '
                      'disabled, two boarded over the weekend). Iran claims it now “controls” the strait — rhetoric, '
                      'not verified.',
                      'CENTCOM / maritime trackers / The Hill'],
                     ['US strikes ON HOLD — three quiet nights (25–27 Jul)',
                      'Third straight quiet night; Pentagon/White House call it ‘on a hold’; blockade stays fully '
                      'operational; Trump (27 Jul) dismissed dwindling-stockpile reports. Iran says its own '
                      'retaliation is paused too.',
                      'DoD / White House / NPR / CBS'],
                     ['Houthi strikes on Saudi soil — Jizan/Yanbu, no new attack since',
                      '25 Jul strikes set Jizan refinery ablaze (satellite-confirmed); Yanbu missiles intercepted. '
                      'Saudi Arabia hit Houthi-held Hodeidah 24–25 Jul, its first direct combat entry. No further '
                      'exchange since the weekend.',
                      'NASA FIRMS / Al Jazeera / CNBC'],
                     ['Mediation — Oman talks advance; Netanyahu–Trump today',
                      'Iran–Oman weekend talks reportedly progressed toward Iran managing transit with fewer '
                      'restrictions — nothing signed. Netanyahu meets Trump 11am ET today, Iran ‘first and '
                      'foremost.’',
                      'Fortune / Times of Israel']]},
 'analysis': {'intro': 'The US economic shock holds at 25/30 for a tenth session, and for the first time since the '
                       'plateau began the geopolitical and market tapes moved the SAME direction together: the '
                       'strike pause extended to a third night, Iran–Oman talks advanced toward a transit framework, '
                       'and crude posted its first back-to-back daily close declines of the war ($94.26 → $91.68 → '
                       "$85.87), now $8.39 off the 23 Jul peak. The inflation leg that tightened to the war's "
                       'closest trigger approach on Friday (5Y5Y 2.2877%, 1.2 bp from 2.30%) eased back to 2.2617% '
                       'on the 27 Jul close — still the second-closest approach of the war, but receding rather than '
                       "closing the gap. Political stress is frozen mid-approach: AAA gasoline's last confirmed "
                       'print, $4.75 on 24 Jul, sits exactly AT the trigger with four sessions of prints now pending '
                       '— the longest data gap of the war outside the JGLA episode. Treasury stress is doing '
                       'something unusual: the same rally that is disarming Stage-4 Threshold B from above (30Y '
                       "receding from 5.20%, 10Y's three-close-above run just broken) is simultaneously arming the "
                       "Treasury channel's own downgrade leg from below (30Y cushion above 5.00% narrowed to 12.4 bp "
                       "intraday) — though MOVE's confirmed 27 Jul close ticked back UP to 77.21, still 2.2 pts "
                       'above its own downgrade line, so the second leg has not moved with it. No trigger fired on a '
                       'confirmed close; nothing moved. Two live events frame the next 48 hours: Netanyahu meets '
                       "Trump at the White House today, and the FOMC's two-day meeting opens today with hike odds "
                       're-priced to 34% from 13% a week ago.',
              'bondYieldNote': '28 Jul yields are intraday; d/d vs 27 Jul close, w/w vs 21 Jul. No channel moved; '
                               'score held at 25.',
              'bondYield': [{'title': '(i) Treasury — held at 5; both downgrade legs still fail, but the composition '
                                      'of the failure changed.',
                             'text': 'The 30Y closed 27 Jul at 5.1365% — 13.65 bp above the 5.00% downgrade leg, '
                                     "narrowed from 24 Jul's 15.74 bp — and prints 5.1239% this morning, a 12.39 bp "
                                     'cushion; this is the SECOND consecutive session the 30Y has moved toward its '
                                     'own release line. MOVE, however, reversed: the confirmed 27 Jul close ticked '
                                     "UP to 77.21 from Thursday's 76.82, undoing part of Friday's snap, and sits 2.2 "
                                     'pts above its 75 leg with no 28 Jul print yet. Both legs must clear '
                                     'simultaneously and sustain to downgrade — the 30Y leg is closer than it has '
                                     'been in a week, but MOVE has not confirmed the move. The FOMC (28–29 Jul) is '
                                     'the binary: hike odds have risen to roughly a third from an eighth a week ago, '
                                     "and Chair Warsh's public framing — inflation 'remains too high,' and a "
                                     "welcomed appetite for a 'family fight' among committee members — cuts against "
                                     'a dovish surprise. A hawkish outcome (or a strike resumption) re-arms the long '
                                     'end from below; a genuine multi-week pause pulls the 30Y further toward its '
                                     'downgrade line.'},
                            {'title': "(ii) Inflation anchor — held at 4; the war's closest trigger approach receded "
                                      'for the first time since the rally began.',
                             'text': "5Y5Y closed 27 Jul at 2.2617%, down 2.6 bp from Friday's 2.2877% peak "
                                     'approach, and prints 2.2603% intraday — now 3.8 bp from the 2.30% line on a '
                                     "close basis (3.97 bp intraday) rather than Friday's 1.2 bp. The pullback "
                                     'tracks the broader risk-off unwind rather than a change in the underlying '
                                     "pass-through story: AAA gasoline's last confirmed print was still a ninth "
                                     'consecutive rise, and the 10Y breakeven stayed BELOW its pre-war anchor for a '
                                     'second session (2.2028% on the 27 Jul close), consistent with the curve '
                                     'pricing medium-term persistence rather than a near-term spike. One close above '
                                     '2.30% starts the clock; a second consecutive close confirms and takes the '
                                     'channel to 5/5 and the score to 26. The downgrade (sustained at/below the '
                                     '2.142% anchor, currently 11.8 bp away) is not in play.'},
                            {'title': '(iii) Oil — held at 2; the gap to the $95 upgrade trigger widened to $13.39 '
                                      'on the close ($9.60 intraday), the widest since 16 Jul.',
                             'text': "Two consecutive daily declines — Friday's $2.58 drop and Monday's further "
                                     '$5.81 — have erased $8.39 of the 23 Jul $94.26 peak close, and the active COA '
                                     "contract gave back its entire triple-digit excursion (Thursday's $100.69 close "
                                     'is now $12.75 above the active spot). The driver is the strike-pause '
                                     'continuation and the advancing Oman transit talks, which have now outweighed '
                                     'the Houthi strikes on Saudi soil for a second consecutive session — Jizan is a '
                                     'domestic refinery, not a crude-export node, and the Yanbu intercepts left the '
                                     'roughly 92% export corridor physically intact. The two-close rule kept the '
                                     'channel at 2 through the entire $95 approach and now spares it a symmetric '
                                     'whipsaw on the way down: a downgrade to 1 still needs a mediated pause AND a '
                                     'close at or below the $72.48 anchor — $13.39 away, further than at any point '
                                     "since mid-July. (OPEC+'s modest August quota increase and the still-elevated "
                                     'CPC Black Sea drone-strike risk remain the supply-side crosscurrents.)'}],
              'stage4Note': 'Stage 4 is a credit/auction event. Threshold B continues to disarm from above — both '
                            "legs moved further from their lines on 27 Jul and again intraday — while the 10Y leg's "
                            'own three-close-above run just broke.',
              'stage4': [{'title': 'Threshold A · 13 May 30Y auction.',
                          'text': 'Historical. Cleared at 5.050%; the 9 Jul re-opening cleared 5.06% with a 0.3 bp '
                                  'stop-through. The 30Y still trades above both marks; no coupon supply until the '
                                  "August refunding, so the FOMC statement and presser (Wednesday) are this week's "
                                  'only long-duration pricing events.'},
                         {'title': 'Threshold B · 30Y above 5.20% with 10Y above 4.65%.',
                          'text': 'Continuing to disarm: the 30Y closed 27 Jul at 5.1365% (6.35 bp below its leg) '
                                  "and prints 5.1239% (7.61 bp below); the 10Y's three-consecutive-closes-above run "
                                  '(22–24 Jul) ended on 27 Jul, closing 0.13 bp BELOW the 4.65% line — the closest '
                                  'confirmed close to the line all war — and prints 1.55 bp below intraday. One more '
                                  "sub-line close would formally reset the 10Y leg's sustained status. B re-arms on "
                                  'a hawkish FOMC, a strike resumption, or a Yanbu re-attack that lands; it disarms '
                                  'fully if the pause holds through the week and the FOMC surprises dovish.'},
                         {'title': 'Threshold C · MOVE above 130.',
                          'text': 'Far off — 77.21 on the last confirmed close, and the metric ticked up rather than '
                                  'down on 27 Jul, a reminder that the vol bid has not fully unwound even as spot '
                                  'risk has.'}],
              'crossAsset': 'The unwind widened and deepened: crude posted its first back-to-back daily close '
                            'declines of the war, European gas fell for a second straight session (TTF €56.98, €6.60 '
                            'off the 24 Jul record), Asia LNG eased on its one fresh print since the record (¥3,492, '
                            '–¥101, no 28 Jul print yet), and the long end of the Treasury curve rallied — all while '
                            'the dollar sat essentially flat (101.51) and MOVE ticked marginally higher rather than '
                            'following crude and gas lower. That divergence is the tell: rates vol has not repriced '
                            "with spot risk, which keeps the Treasury channel's downgrade path a two-leg proposition "
                            'even as the 30Y itself moves toward release. US Henry Hub remains 10.2% BELOW pre-war — '
                            'still a Hormuz/LNG-routing shock, not a global-energy shock. With both AAA and DOE '
                            'gasoline now dark for four and eight sessions respectively, the political channel is '
                            "the war's most opaque market read heading into a day that carries both a "
                            'Netanyahu–Trump meeting and an FOMC opening session.'},
 'channels': [{'name': 'Maritime denial',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 (max). Strait closed to commercial traffic, day ~150; transits ~17% of '
                            'typical (15 vs 88/day); 445–540 anchored (revised basis); 92 tankers AIS-dark in 24h vs '
                            'a 70.9 average; war-risk ~8×, VLCC ~$2.5m; six P&I clubs withdrawn; 8 of 9 major '
                            "carriers rerouting via the Cape. Iran's public claim to now 'control' the strait is "
                            'rhetoric, not a verified change — no confirmed reopening.',
               'upgrade': 'at max.',
               'downgrade': 'verified reopening (escorted convoys) with traffic above 25% of normal for 10 sessions '
                            '→ to 3–4.'},
              {'name': 'Oil price shock',
               'score': 2,
               'state': 'hold',
               'rationale': 'Held at 2 — and the gap widened sharply. 27 Jul close $85.87 (–$5.81, second straight '
                            'decline), $13.39 below the $95 trigger; intraday $85.40, $9.60 below. Two-close rule '
                            "kept the channel from whipsawing on the way up through Thursday's $95 approach and now "
                            "spares a symmetric move down. Active COA prints $87.94, $12.75 off Thursday's $100.69.",
               'upgrade': 'Brent above $95 sustained → to 3.',
               'downgrade': 'mediated pause + close at/below the $72.48 anchor → to 1.'},
              {'name': 'US inflation impulse',
               'score': 4,
               'state': 'hold',
               'rationale': "Held at 4 — the war's closest trigger approach receded. 5Y5Y closed 2.2617% (–2.6 bp "
                            "from Friday's 2.2877% peak), 3.8 bp from the line; intraday 2.2603%. 10Y breakeven "
                            'stayed below its pre-war anchor for a second session (2.2028%), consistent with '
                            'pass-through pricing rather than a fresh spot spike.',
               'upgrade': '5Y5Y sustained above 2.30% → to 5.',
               'downgrade': '5Y5Y sustained at/below the 2.142% pre-war anchor → to 3.'},
              {'name': 'Treasury stress',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 — both downgrade legs still fail, but only one is moving toward release. 30Y '
                            'closed 5.1365% (13.65 bp above the 5.00% leg, narrowed from 15.74 bp), prints 5.1239% '
                            "(12.39 bp); MOVE's confirmed close ticked UP to 77.21, 2.2 pts above its 75 leg — the "
                            'two legs are no longer moving together.',
               'upgrade': 'at max.',
               'downgrade': '30Y close under 5.00% with MOVE under 75 sustained → to 4.'},
              {'name': 'Political stress',
               'score': 4,
               'state': 'hold',
               'rationale': 'Held at 4 — frozen exactly AT the trigger. AAA $4.75 (24 Jul print, latest confirmed) — '
                            'ninth consecutive rise, sitting on the $4.75 line but not through it; 25–28 Jul prints '
                            'pending, the longest gap of the war outside JGLA. DOE weekly overdue since 27 Jul. '
                            'Evaluated on confirmed prints only.',
               'upgrade': 'gasoline above $4.75 sustained → to 5.',
               'downgrade': 'toward the $3.52 pre-war level → to 3.'},
              {'name': 'Escalation risk',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 (max). The strike pause extended to a third night and Iran–Oman talks '
                            'advanced toward a transit framework — genuine de-escalation signals — but no mediated '
                            "stand-down has been declared and the administration's 'locked and loaded' posture "
                            'stands. A downgrade needs a mediated stand-down plus resumed formal talks — a third '
                            'quiet night is a necessary step, not yet the event.',
               'upgrade': 'at max.',
               'downgrade': 'mediated stand-down + talks resume → to 4–3.'}],
 'scoreTotal': 'CRISIS band — tenth session at 25, with the market tape now confirming the weekend de-escalation on '
               "closes: Brent's first back-to-back daily declines of the war, the 10Y's three-close-above run "
               'broken, and the inflation-complex approach receding. Political stress is frozen mid-approach by a '
               'data gap, not a reversal. With both event channels maxed, only the four market channels can move the '
               'score — in either direction — and today brings a Netanyahu–Trump meeting and an FOMC opening session '
               'that could move several of them at once.',
 'whatsChanged': {'title': "4 · What's changed since the last edition (27 Jul → 28 Jul AM)",
                  'items': ['The strike pause extended to a third consecutive quiet night. No new US strikes 25–27 '
                            "Jul; the Pentagon and White House continue to call the campaign 'on a hold'; the naval "
                            'blockade stays fully operational. Trump on 27 Jul dismissed reports of dwindling '
                            "munitions stockpiles. Iran's military says its own retaliatory operations are likewise "
                            'paused. Source: DoD / White House / NPR / CBS.',
                            'Iran–Oman talks advanced toward an actual transit framework. Weekend technical '
                            'consultations reportedly progressed toward Iran managing Hormuz vessel transit with '
                            'reduced restrictions — closer to the June interim deal — though nothing is signed; Iran '
                            "separately claimed publicly to now 'control' the strait, a rhetorical escalation of its "
                            'negotiating position, not a verified change on the water. Source: Fortune / The Hill.',
                            "Crude posted the war's first back-to-back daily close declines. Brent: $94.26 (23 Jul "
                            'close) → $91.68 (24 Jul) → $85.87 (27 Jul, –$5.81) → $85.40 intraday. The active COA '
                            "contract gave back its entire triple-digit excursion, from Thursday's $100.69 close to "
                            '$87.94. TTF fell a second straight session, €6.60 off the 24 Jul record. Source: '
                            'Bloomberg.',
                            "5Y5Y receded from the war's closest trigger approach. The 27 Jul close, 2.2617%, pulled "
                            "back 2.6 bp from Friday's 2.2877% — now 3.8 bp from the →5 line on a close basis rather "
                            'than 1.2 bp. The 10Y breakeven stayed below its pre-war anchor for a second session. '
                            'Source: Bloomberg.',
                            "The 10Y's three-close-above run on Stage-4 Threshold B broke. 27 Jul closed 4.6487%, "
                            '0.13 bp below the 4.65% line, after three consecutive closes above (22–24 Jul); prints '
                            "1.55 bp below intraday. The 30Y's cushion above its own 5.00% downgrade line narrowed "
                            "to 12.4 bp intraday even as its gap to the 5.20% upside line widened to 7.6 bp. MOVE's "
                            "confirmed close ticked UP to 77.21, undoing part of Friday's snap. Source: Bloomberg.",
                            "Gasoline data gap widened to four sessions — the longest since JGLA. AAA's last "
                            'confirmed print remains $4.75 (24 Jul); 25–28 Jul are pending. The DOE weekly print '
                            'expected 27 Jul has not landed either. The political channel holds at 4 on the last '
                            'confirmed data. Source: AUTMUSAG / USRFRUSA via Bloomberg.',
                            'Two live catalysts open today. Netanyahu meets Trump at the White House at 11am ET, '
                            "their first sit-down since before the war — Iran 'first and foremost' on the agenda. "
                            "The FOMC's two-day meeting also opens today; hike odds have risen to roughly 34% from "
                            '13% a week ago. Source: Times of Israel / Fortune / CME FedWatch.']},
 'scenarios': [{'name': 'Return to full war',
                'p': 29,
                'desc': 'Still the modal path but weakening for a second straight edition: three quiet nights, an '
                        "advancing Oman transit framework, and Netanyahu's visit could still reset Washington toward "
                        "escalation if it goes the other way — the administration's 'locked and loaded' posture is "
                        'unchanged.',
                'path': 'Brent $105–140; MOVE above 90; oil to 3–4, political to 5, US-inflation to 5; score 28–30.'},
               {'name': 'Mediated pause — the ceasefire sticks',
                'p': 20,
                'desc': 'The strongest version of this scenario all war: three consecutive quiet nights, a '
                        'substantive Oman transit framework rather than just talks, Trump downplaying operational '
                        "strain, and a market pricing the unwind on closes rather than just intraday. Needs today's "
                        'Netanyahu meeting not to reset it and Iran to formalize the framework.',
                'path': 'Brent $74–85; MOVE under 72; Treasury→4, US-inflation→3, escalation→4; score falls toward '
                        '19–21.'},
               {'name': 'Contained but violent — blockaded stalemate',
                'p': 18,
                'desc': 'Strikes stay paused at low intensity, escort-only transits continue, and the Jizan/Yanbu '
                        "exchange doesn't escalate further — but nothing is resolved and the blockade holds "
                        'indefinitely.',
                'path': 'Brent $82–92; MOVE 72–82; risk premium $10–20/bbl; score holds 24–25.'},
               {'name': 'Deal collapse — MoU formally lapses',
                'p': 18,
                'desc': 'The Oman transit framework is rejected or stalls, the pause is revealed as tactical rather '
                        'than genuine, and strikes resume without a formal ceasefire ever forming. The three-night '
                        'pause makes this marginally less likely this week, but nothing is signed yet.',
                'path': 'Brent $92–108; oil back to 3; 30Y back above 5.15% toward the 5.20% leg; score 26–27.'},
               {'name': 'Regional relapse — Gulf energy infrastructure hit',
                'p': 15,
                'desc': 'No new Houthi attack since the 25 Jul weekend, but the demonstrated capability against '
                        "Jizan and the near-miss at Yanbu stand; Saudi Arabia's entry into direct combat is an "
                        'unresolved escalation channel that a single landed hit on the export corridor would '
                        'reactivate.',
                'path': 'Brent $150+; emergency policy response; HY spreads above 500 bp; score 29–30.'}],
 'scenarioShift': 'Probability shifts from the 27 Jul edition: mediated pause +6 (14→20) — a third consecutive quiet '
                  'night plus an actual Oman transit framework (not just talks) is the strongest de-escalation '
                  'signal of the war; full war –4 (33→29) — still modal but weakening for a second edition running; '
                  'contained-but-violent –1 (19→18) and deal collapse –1 (19→18); regional relapse unchanged (15). '
                  'Driver: the pause held through a third night and the market repriced it on CLOSES, not just '
                  "intraday — but Netanyahu's visit and the FOMC both land today, either of which could reverse the "
                  'drift.',
 'watchlist': ["Netanyahu–Trump, 11am ET today. Their first meeting since before the war; Iran 'first and foremost.' "
               'A signal toward formalizing the pause supports the mediated-pause path; a hawkish readout (or a '
               'resumed-strikes signal) reprices the whole weekend unwind back in.',
               'FOMC · Tuesday–Wednesday 28–29 Jul. Hike odds have risen to roughly 34% from 13% a week ago; Chair '
               "Warsh's public line is that inflation 'remains too high' and he has welcomed a 'family fight' among "
               'committee members. A hawkish hold or hike re-arms the long end and Stage-4 B; a dovish surprise '
               'accelerates the Treasury-channel release path (30Y under 5.00% with MOVE under 75 — currently 12.4 '
               'bp and 2.2 pts away, and only the 30Y leg is currently moving that way).',
               "US-inflation →5 (5Y5Y above 2.30% sustained) — 3.8 bp, receding. Friday's approach to 1.2 bp was the "
               "war's closest; the 27 Jul close pulled back to 3.8 bp. Whether the FOMC reopens the approach or "
               "extends the pullback is the channel's live question.",
               'Political →5 ($4.75) — AT the line, four prints pending. The ninth consecutive AAA rise landed '
               "exactly on the threshold on 24 Jul; 25–28 Jul haven't printed. The DOE weekly is also overdue. "
               'Whether the backfill shows a tenth rise through $4.75, a stall, or a reversal with crude is '
               'unresolved — the longest data blackout since the JGLA stale-carry episode.',
               '10Y reset status on Threshold B. 27 Jul closed 0.13 bp below the 4.65% line after three closes '
               "above; one more sub-line close formally resets the leg's sustained status and further disarms B.",
               'Yanbu re-attack risk — the demonstrated tail, dormant since the weekend. Jizan proved reach and '
               "Yanbu's intercepts held once; no further Houthi action has landed since. A hit that lands on the "
               'roughly 92% export corridor is the regional-relapse trigger and reprices crude, breakevens and bond '
               'vol together, at full amplitude.',
               'Gas complex — unwind now in its second session. TTF €56.98 after the €63.58 record; Asia LNG ¥3,492, '
               'no 28 Jul print yet — verify the next JGLA print fresh, never carry.'],
 'sourceLog': {'tier1Market': 'Bloomberg Terminal extract (US Iran BBG Data.xlsx, restated front-month continuation '
                              'series). Tickers: CO2/CL2 Comdty (Brent/WTI front-month; the CL2 artifact persists — '
                              'CL2 closed $80.25 vs active CLA $82.61 on 27 Jul; WTI is read off the active board); '
                              'COA/CLA Comdty (active, unscored — COA closed $88.36, prints $87.94); NGA/TZTA/JGLA '
                              'Comdty (JGLA printed fresh 27 Jul at ¥3,492, –¥101 off the 24 Jul record; no 28 Jul '
                              'print); USGG2YR/5YR/10YR/20YR/30YR Index; USYC2Y10; USGGBE10 (27 Jul close 2.2028 — '
                              'below the pre-war anchor for a second session); USGG5Y5Y (27 Jul close 2.2617 — 3.8 '
                              'bp from the →5 trigger); SOFRRATE (lagged, 24 Jul, 3.64%); MOVE and VIX (27 Jul '
                              'closes 77.21 / 18.67; 28 Jul lagged, carried and labelled); DXY; AUTMUSAG (AAA pump — '
                              'score reference; latest confirmed print 24 Jul $4.75; 25–28 Jul pending) and USRFRUSA '
                              '(DOE regular spot, weekly — corroboration; 20 Jul print $4.001; 27 Jul weekly print '
                              'overdue).',
               'tier1News': 'US DoD / White House via NPR, CBS News, CNBC and Al Jazeera (strike pause held a third '
                            "consecutive night; 'on a hold' framing; naval blockade fully operational; Trump "
                            'dismissed dwindling-stockpile concerns 27 Jul), Fortune (Iran–Oman transit-framework '
                            'negotiations; 12 commercial vessels redirected, two disabled, two boarded over the '
                            'weekend), Times of Israel / Foreign Policy / Axios (Netanyahu–Trump meeting confirmed '
                            'for 11am ET today, Iran the top agenda item, security posture around the visit), '
                            'Washington Times / Washington Institute for Near East Policy (Michael Singh on the '
                            'significance of a sustained pause), TechTimes citing NASA FIRMS satellite thermal data '
                            '/ Al Jazeera / The National / CNBC (Jizan refinery fires, Yanbu intercepts, Saudi '
                            'retaliatory strikes on Hodeidah — no new exchange reported since the weekend), CME '
                            'FedWatch via Fortune (FOMC hike-probability repricing to ~34% from ~13% a week earlier; '
                            "Chair Warsh's public 'family fight' framing and inflation-too-high line), Bloomberg / "
                            'TradingEconomics (OPEC+ August quota increase; CPC Black Sea terminal drone-strike risk '
                            'persists), straits.live / Windward / IMF PortWatch (day count, transits 15 vs 88/day — '
                            '~17% of typical, 19 Jul count; 445–540 anchored on a revised basis; 92 AIS-dark in 24h '
                            'vs 70.9 avg; ~8× war-risk cover; six P&I withdrawals; 8-of-9-carrier disruption).',
               'tier3': "Iran's public assertion that it now 'controls' the Strait of Hormuz (The Hill, citing "
                        'Iranian officials) is a negotiating-posture claim, not a verified change in transit access, '
                        'and is not used for any scoring decision. The Houthi military statement (Brig. Gen. Yahya '
                        'Saree) claiming successful strikes on Jizan and Yanbu is a combatant claim — the Jizan '
                        'fires are independently corroborated by satellite thermal data; the Yanbu intercepts are '
                        'corroborated by multiple Tier 1 outlets. IRNA, Mehr, Press TV used only with explicit role '
                        'labels; none used this edition.'},
 'protocol': [{'step': 'Refresh the Bloomberg extract',
               'detail': 'Parse the latest dated row (28 Jul) as intraday; reclassify 27 Jul as a final close; '
                         're-map columns via the robust scan (front-month CO2/CL2; both gasoline series checked — '
                         'AAA and DOE both pending since 24–25/20 Jul respectively; JGLA checked fresh, printed 27 '
                         'Jul ¥3,492, no 28 Jul print, flagged not carried; MOVE/VIX 28 Jul lagged, 27 Jul closes '
                         'carried and labelled; SOFR lagged 24 Jul).'},
              {'step': 'Recompute deltas',
               'detail': 'd/d vs the 27 Jul close; w/w vs the close five trading sessions back (21 Jul this '
                         'edition); vs-pre-war vs the 27 Feb 2026 anchor (re-verified, unchanged).'},
              {'step': 'Re-evaluate the six channels',
               'detail': 'Market channels move on confirmed closes only — all held: oil 2 (close $85.87, gap widened '
                         'to $13.39); Treasury 5 (30Y 5.1365% above 5.00%; MOVE 77.21 above 75); US-inflation 4 '
                         '(5Y5Y 2.2617%, 3.8 bp under 2.30%); political 4 (AAA $4.75 confirmed, exactly on the $4.75 '
                         'line, not through it). Maritime/escalation event-based, both maxed — three quiet nights is '
                         'not yet a mediated stand-down.'},
              {'step': 'Reconcile against the prior edition',
               'detail': 'The US session took the tape DOWN through the Asia snapshot for a second consecutive '
                         'session: Brent 27 Jul intraday (quoted in the prior edition) $87.88 → close $85.87 '
                         '(–$2.01); 10Y 4.6365% → 4.6487%; 30Y 5.1218% → 5.1365%; TTF €58.50 → €58.253; 5Y5Y 2.2799% '
                         '→ 2.2617% — every series the prior edition carried as intraday confirmed lower or flat on '
                         'the close.'},
              {'step': 'Update scenarios and watchlist',
               'detail': 'Re-rank catalysts: Netanyahu–Trump (11am ET today) and the FOMC opening (28–29 Jul) both '
                         'land today; US-inflation→5 (3.8 bp, receding), political→5 (AT the line, four prints '
                         'pending), 10Y reset status on Threshold B (one more sub-line close needed); mediated pause '
                         '14→20, full war 33→29.'}],
 'methodology': {'scale': 'Six transmission channels (maritime denial, oil price shock, US inflation impulse, '
                          'Treasury stress, political stress, escalation risk), each 0–5, summed to 0–30. Bands: 0–7 '
                          'watch · 8–14 stress · 15–21 systemic-risk watch · 22–30 crisis. Market/economic channels '
                          'move only on a confirmed close through a trigger; escalation-risk is event-based. '
                          'Hysteresis note: upgrades fire on a sustained break; downgrades only on a sustained '
                          'reversal past a wider threshold — deliberately, to avoid whipsawing. This edition '
                          'illustrates the discipline working in both directions on the SAME channel: Stage-4 '
                          "Threshold B's 10Y leg needs a second consecutive sub-line close to formally reset its "
                          "three-close-above 'sustained' status (only one such close has landed, 27 Jul), while the "
                          "Treasury channel's own downgrade leg requires the 30Y sustained below 5.00% together with "
                          "MOVE sustained below 75 — the 30Y is moving that way for a second session, but MOVE's "
                          'confirmed close ticked the wrong way on 27 Jul, so neither reset nor downgrade has '
                          "occurred. Scale cap: maritime and escalation are both at 5/5, so neither the pause's "
                          'extension to a third night nor the advancing Oman talks (already-maxed channels) can move '
                          'the score — only the four market channels can, in either direction.',
                 'gasoline': 'Political-stress is scored on AUTMUSAG (AAA all-grades retail pump; pre-war $3.52, '
                             'peak $5.18, latest confirmed print $4.75 on 24 Jul — a ninth consecutive rise, sitting '
                             'exactly on the $4.75 threshold) for continuity; the 25–28 Jul prints are pending in '
                             'the extract and the channel holds until they are confirmed — per the parser discipline '
                             'established after the JGLA stale-carry episode, a missing print is flagged, never '
                             'carried forward as if confirmed. USRFRUSA (DOE regular-grade retail spot; pre-war '
                             '~$2.94, peak $4.50, latest $4.001 on 20 Jul; the 27 Jul weekly print is overdue) is '
                             'tracked alongside. See the chart in section 1.',
                 'anchor': 'Brent $72.48; WTI $67.02; 2Y 3.375%; 5Y 3.502%; 10Y 3.938%; 30Y 4.611%; 2s10s +55.64 bp; '
                           '5Y5Y 2.142%; 10Y BE 2.257%; MOVE 73.38; VIX 19.86; DXY 97.608; gasoline (AAA) $3.52; '
                           'Henry Hub $3.06; TTF €31.23; Asia LNG ¥1,669. (Re-verified — unchanged.) Brent +17.8%, '
                           'WTI +19.0%, TTF +82.5%, Asia LNG +109.2% (27 Jul print); the 30Y (+51.3 bp), 10Y (+69.7 '
                           'bp), 5Y5Y (+11.8 bp), MOVE (+3.83) and DXY (+3.90) sit above their anchors; the 10Y '
                           'breakeven (–5.4 bp) remains below its anchor for a second session, and VIX and US Henry '
                           'Hub remain below pre-war — the Hormuz/LNG-routing signature intact.',
                 'intraday': 'The latest dated row is a Singapore-AM intraday snapshot; US-hours trading and '
                             'headlines set the close (recent reconciliation gaps on Brent: –$0.90, +$1.91, +$0.60, '
                             '+$3.10, –$1.81, –$2.01 — the 27 Jul session was the SECOND straight session to close '
                             'the crude tape below the Asia snapshot, the first repeated occurrence of the war). '
                             'Tuesday-edition note: MOVE and VIX carry the 27 Jul closes, labelled; the UST curve '
                             'printed live this morning. The CL2 WTI series remains flagged as a data artifact '
                             'against the active CLA contract; WTI levels are read off the active board pending '
                             'resolution. Market-channel triggers are evaluated on confirmed closes; escalation-risk '
                             'is event-based. Absolute levels use the restated continuation series and are not '
                             'directly comparable with pre-restatement editions, though the directional analysis is '
                             'continuous.'}}

# ======================================================================
# 2026-07-29 (current)
# ======================================================================
EDITIONS['2026-07-29'] = {'label': '29 Jul 2026',
 'editionLine': 'Daily edition · 29 Jul 2026 intraday · Bloomberg · Singapore 29 Jul AM update',
 'score': 25,
 'band': 'CRISIS',
 'sequencing': '25 → 25 → 25',
 'sessionNote': 'Eleventh session at 25',
 'headline': 'Note: 29 Jul figures are intraday prints; 28 Jul is now a final close ($82.08 Brent, down $3.79 from '
             "27 Jul's $85.87 — the third consecutive daily decline and, cumulatively, $12.18 off the 23 Jul $94.26 "
             'peak close). Restated continuation series (front-month CO2/CL2) in force. Score HOLDS at 25/30 — all '
             'six channels unchanged, an eleventh session at 25 — but beneath the flat number the two most '
             'consequential things in this edition move in opposite directions. First, the de-escalation survived '
             'its biggest scheduled test: the US strike pause held a fourth consecutive night (25–28 Jul), the '
             'longest of the war, and the Netanyahu–Trump White House meeting produced no resumption signal — an '
             "Israeli official called it an 'excellent and comprehensive discussion... first and foremost Iran' with "
             "an 'ironclad' nuclear commitment, and the White House framed both of Tuesday's leader meetings as "
             "'positive and productive.' Oman went further, tabling a Malacca-model joint-management framework with "
             'voluntary vessel fees. Second, Iran hardened its terms in the same 24 hours: the Khatam al-Anbiya '
             'Central Headquarters declared on 28 Jul that vessels of any country or company accepting compensation '
             "from Iran's frozen assets 'will not be allowed' to transit, and Tehran separately tabled a rival "
             'temporary plan giving itself greater control of the transit lanes. Crude read the second story: after '
             'the 28 Jul close, Brent has bounced to $85.04 intraday (H 85.45 / L 83.95, +$2.96), with the active '
             "COA contract back to $87.61 from Tuesday's $84.09 close. The reconciliation gap was the widest of the "
             'war on the downside — my 28 Jul quote of $85.40 closed $3.32 lower — the third straight session in '
             'which the US leg took the tape below the Asia snapshot, a first. On rates the news is a genuine change '
             "of state: for the first time in the war both legs of the Treasury channel's downgrade test moved "
             'toward release in the same session. The 30Y closed 5.0886%, cutting its cushion above the 5.00% line '
             "from 13.65 bp to 8.86 bp (a third consecutive session toward it), and MOVE's confirmed close fell 1.12 "
             'to 76.09 — now just 1.09 pts above the 75 leg, the closest of the war. Neither has cleared, so nothing '
             "moved; but Treasury 5→4 is now the score's most probable next step, and it is a downgrade. Stage-4 "
             "Threshold B disarmed further: the 10Y's 4.6062% close was a second consecutive print below 4.65%, "
             "formally resetting that leg's sustained status, and the 30Y sits 11.14 bp below 5.20%. The gasoline "
             "blackout partly cleared and the news is a stall, not a break — AAA's backfilled 27 Jul print came in "
             'at $4.75, flat, ending the nine-session run of rises exactly ON the political→5 line without going '
             'through it, while the overdue DOE weekly landed at $4.096 (+9.5¢). The inflation leg edged the wrong '
             'way again — 5Y5Y closed 2.2667%, 3.33 bp from the trigger. No trigger fired on a confirmed close, so '
             'no channel moved; with both event channels maxed, the hold remains an artifact of the scale. The FOMC '
             'decides at 2pm ET today with hike odds near a third (roughly 32–38%, against 10.7% on 15 Jul) and '
             "Chair Warsh's presser at 2:30 — the single event most likely to resolve the Treasury channel in either "
             'direction. Sequencing 25 → 25 → 25.',
 'tape': {'note': '29 Jul 2026 readings are intraday prints; 28 Jul and earlier are final closes (restated '
                  'continuation series; front-month CO2/CL2). d/d deltas are 29 Jul intraday vs the 28 Jul close; '
                  'w/w deltas are vs the 22 Jul close.',
          'oilGasHeader': ['Benchmark', 'Intraday 29 Jul', 'Δ d/d', 'Δ vs pre-war close (27 Feb)', 'BBG ticker'],
          'oilGas': [['Brent front-month',
                      '$85.04 /bbl (H 85.45 / L 83.95)',
                      '+$2.96 (–$5.14 w/w)',
                      'from $72.48 (+17.3%) — $12.56/bbl premium; the first bounce after three straight declines, on '
                      "Iran's new transit threat; active COA prints $87.61",
                      'CO2 Comdty (Close)'],
                     ['Brent · 28 Jul close (final)',
                      '$82.08 /bbl (–$3.32 vs my 28 Jul intraday $85.40)',
                      '–$3.79 d/d — third straight decline; the US leg took the tape below the Asia snapshot for a '
                      'third session, a first',
                      '$12.92 below the $95 trigger on a close basis; $9.60 above the $72.48 anchor; active COA '
                      'closed $84.09',
                      'CO2 Comdty (Close)'],
                     ['WTI front-month',
                      '$79.97 /bbl',
                      '+$2.80 (–$3.67 w/w)',
                      'from $67.02 (+19.3%) — the CL2 artifact persists: 28 Jul CL2 close $77.17 vs active CLA '
                      '$79.26; CLA prints $82.42',
                      'CL2 Comdty (Close)'],
                     ['Brent–WTI spread', '$5.07 /bbl', '+$0.16', '~$5.2 on the active contracts', 'derived'],
                     ['Henry Hub natural gas',
                      '$2.651 /MMBtu',
                      '–$0.011 (–$0.274 w/w)',
                      'from $3.06 (–13.5%) — US gas further BELOW pre-war; not Hormuz-exposed',
                      'NGA Comdty (Close)'],
                     ['TTF Dutch gas (active)',
                      '€59.11 /MWh',
                      '+€1.37 (–€3.43 w/w)',
                      'from €31.23 (+89.3%) — bounced with crude after three sessions off the 24 Jul war-era record '
                      '€63.58',
                      'TZTA Comdty (Close)'],
                     ['Japan/Asia LNG (28 Jul close — fresh print)',
                      '¥3,418',
                      '–¥74 vs the 27 Jul ¥3,492',
                      'from ¥1,669 (+104.8%) — a third consecutive easing off the war-era record; no 29 Jul print '
                      'yet (flagged, not carried)',
                      'JGLA Comdty (Close)']],
          'ustNote': '29 Jul 2026 yields are intraday. d/d deltas are vs the 28 Jul close; w/w vs 22 Jul. The 10Y '
                     'logged a second consecutive close below the 4.65% Stage-4 leg, formally resetting it; the '
                     "30Y's cushion above its own 5.00% downgrade line narrowed to 8.86 bp on the close. See section "
                     '2.1 for the full read.',
          'ustHeader': ['Tenor',
                        'Yield (%) — intraday 29 Jul',
                        'Δ d/d (bp)',
                        'Δ w/w (bp)',
                        'Δ vs pre-war (bp)',
                        'BBG ticker'],
          'ust': [['2-year UST', '4.30', '+0.8', '–0.3', '+92.0 (from 3.37%)', 'USGG2YR Index'],
                  ['5-year UST', '4.38', '+0.9', '–2.5', '+87.7 (from 3.50%)', 'USGG5YR Index'],
                  ['10-year UST',
                   '4.61',
                   '+0.8',
                   '–4.0',
                   '+67.7 (from 3.94%) — 28 Jul close 4.6062%, second consecutive close below the 4.65% Stage-4 leg; '
                   "the leg's sustained status is reset",
                   'USGG10YR Index'],
                  ['30-year UST',
                   '5.10',
                   '+0.8',
                   '–4.8',
                   '+48.6 (from 4.61%) — 28 Jul close 5.0886%: 11.14 bp below the 5.20% leg, only 8.86 bp above the '
                   '5.00% leg',
                   'USGG30YR Index'],
                  ['2s10s spread',
                   '+31.7 bp',
                   '–0.0',
                   '–3.8',
                   '–23.9 (flatter) — the flattest of the war',
                   'USYC2Y10 Index'],
                  ['10Y breakeven inflation',
                   '2.196',
                   '+0.0',
                   '–8.6',
                   '–6.1 (from 2.257%) — 28 Jul close BELOW the pre-war anchor for a third session',
                   'USGGBE10 Index'],
                  ['5Y5Y forward inflation',
                   '2.263',
                   '–0.4',
                   '+4.4',
                   '+12.1 (from 2.14%) — 28 Jul close 2.2667%, up 0.5 bp; 3.33 bp from the →5 line',
                   'USGG5Y5Y Index'],
                  ['SOFR (lagged print, 24 Jul)', '3.64', '—', '—', 'series lags', 'SOFRRATE Index']],
          'crossHeader': ['Gauge', 'Latest', 'As of', 'Δ vs pre-war', 'Interpretation'],
          'cross': [['DXY',
                     '101.38',
                     '29 Jul intraday',
                     '+3.77 (from 97.61)',
                     'Flat again on the day; still no haven bid — the dollar remains a bystander, not the stress '
                     'valve.'],
                    ['MOVE',
                     '76.09',
                     '28 Jul close (29 Jul lagged)',
                     '+2.71 (from 73.38)',
                     'Fell 1.12 from 77.21 — now only 1.09 pts above the 75 downgrade leg, the closest of the war.'],
                    ['VIX',
                     '18.21',
                     '28 Jul close (29 Jul lagged)',
                     '–1.65 (from 19.86)',
                     'Eased with the crude unwind; still below pre-war.'],
                    ['AAA gasoline',
                     '$4.75 /gal',
                     '27 Jul print (backfilled; 28–29 Jul pending)',
                     '+$1.23 (from $3.52, +34.9%)',
                     'Political-stress reference. The backfilled print landed FLAT — the nine-session run of rises '
                     'ended, still exactly AT $4.75, not through it.'],
                    ['DOE gasoline',
                     '$4.096 /gal',
                     '27 Jul weekly print (backfilled)',
                     '+$1.16 (from ~$2.94, +39.4%)',
                     'The overdue weekly landed at +9.5¢ from $4.001 — corroborates continued pass-through even as '
                     'AAA stalled.']],
          'gasChartNote': 'AUTMUSAG (AAA all-grades retail pump, daily) is the political-stress score reference '
                          '(pre-war $3.52, peak $5.18, latest $4.75 on 27 Jul — flat, the first non-rising print in '
                          'ten sessions); USRFRUSA (DOE regular-grade retail spot, weekly) is the complementary '
                          'gauge (pre-war ~$2.94, peak $4.50, latest $4.096 on 27 Jul, +9.5¢ on the week). Both '
                          'series backfilled their overdue 27 Jul prints in this extract, closing most of the '
                          'four-session blackout flagged yesterday; the 28–29 Jul AAA prints are still pending and '
                          'the channel holds at 4 on confirmed data.',
          'straitHeader': ['Indicator', 'Current reading', 'Source'],
          'strait': [['Strait closed · day ~151',
                      'Closed since 28 Feb; naval blockade plus escort operation fully operational. Transit activity '
                      'at a war low — one recorded transit on 25 Jul (0 inbound, 1 outbound); 43 Arabian Gulf crude '
                      'tankers logged AIS gaps 15–22 Jul, the highest single reading in four years and ~25% above '
                      'the 35-vessel baseline; 24 dark tankers in the Kharg eastern waiting area (26 Jul).',
                      'Windward / straits.live / IMF PortWatch'],
                     ['US strikes ON HOLD — four quiet nights (25–28 Jul)',
                      'The longest pause of the war, after 13 consecutive nights of strikes. Pentagon and White '
                      'House keep the ‘on a hold’ framing; the blockade is unchanged. Iran’s own retaliation remains '
                      'paused.',
                      'DoD / White House / Bloomberg / NPR'],
                     ['Netanyahu–Trump, 28 Jul — no resumption signal',
                      'Closed-press meeting; an Israeli official described ‘an excellent and comprehensive '
                      'discussion... first and foremost Iran’ and an ‘ironclad’ commitment against an Iranian '
                      'nuclear weapon. The White House called Tuesday’s leader meetings ‘positive and productive.’ '
                      'Trump had earlier dismissed Netanyahu’s Pickaxe Mountain briefing: ‘I don’t need Bibi to tell '
                      'me that.’',
                      'UPI / Jerusalem Post / The Forward / NBC'],
                     ['Iran hardens transit terms — 28 Jul',
                      'Khatam al-Anbiya Central Headquarters: vessels of any country or company accepting '
                      'compensation from Iran’s frozen assets ‘will not be allowed’ to transit. Iran separately '
                      'tabled a temporary Hormuz plan giving itself greater control of the transit lanes.',
                      'Xinhua / Washington Times / US News'],
                     ['Mediation — Oman tables a Malacca-model framework',
                      'Omani FM Badr Al Busaidi chaired a GCC virtual ministerial on freedom of navigation and '
                      'maritime security. Oman’s proposal is joint management with voluntary vessel fees — '
                      'explicitly not unilateral Iranian control, and distinct from the mandatory toll Washington '
                      'rejected. Nothing signed.',
                      'The National / Oman MFA / Fortune'],
                     ['Red Sea / Saudi front — quiet since 25 Jul',
                      'No new Houthi action since the Jizan refinery fire and the Yanbu intercepts. Yanbu loadings '
                      'remain ~40% below the pre-19 Jul run rate (5.16 → 3.09 mb/d); Bab al-Mandeb transits 17 in / '
                      '14 out on 25 Jul vs 20 / 19 prior.',
                      'Windward / Al Jazeera / TechTimes']]},
 'analysis': {'intro': 'The US economic shock holds at 25/30 for an eleventh session, but the composition of the '
                       'standstill changed materially. On the geopolitical side the de-escalation cleared its '
                       'highest hurdle: the strike pause reached a fourth night, and the Netanyahu visit — the '
                       'single most plausible reset event on the calendar — came and went without a resumption '
                       'signal, while Oman put an actual joint-management framework on the table. On the Iranian '
                       'side the terms hardened in the same 24 hours, with the Khatam al-Anbiya command threatening '
                       "transit denial over the frozen-asset compensation scheme and Tehran countering Oman's draft "
                       'with a plan that concentrates control in its own hands. Crude priced the second story, '
                       'bouncing $2.96 off a 28 Jul close that had itself fallen $3.79. The more important '
                       "development is on rates. Until this session the Treasury channel's two downgrade legs had "
                       'been moving apart — the 30Y toward release, MOVE away from it. On the 28 Jul close they '
                       'moved together for the first time: the 30Y cut its cushion above 5.00% to 8.86 bp and MOVE '
                       'fell to 76.09, 1.09 pts from its own line. Neither cleared and neither has sustained, so the '
                       'channel held at 5 — but a 5→4 downgrade is now the most probable next move in the score, and '
                       'the FOMC decision at 2pm ET today, with hike odds near a third and a new Chair holding only '
                       'his second meeting, is the event most likely to settle it in one direction or the other.',
              'bondYieldNote': '29 Jul yields are intraday; d/d vs the 28 Jul close, w/w vs 22 Jul. No channel '
                               'moved; score held at 25.',
              'bondYield': [{'title': '(i) Treasury — held at 5; for the first time in the war both downgrade legs '
                                      'moved toward release together.',
                             'text': 'The 30Y closed 28 Jul at 5.0886% — 8.86 bp above the 5.00% downgrade leg, '
                                     'narrowed from 13.65 bp on Monday and 15.74 bp on 24 Jul — a third consecutive '
                                     'session toward its own release line; it prints 5.0969% this morning (9.69 bp) '
                                     'as the curve backs up marginally into the FOMC. MOVE, which had ticked the '
                                     'wrong way on 27 Jul, reversed: the confirmed 28 Jul close fell 1.12 to 76.09, '
                                     'leaving it 1.09 pts above the 75 leg — the closest approach of the war. Both '
                                     'legs must clear simultaneously and sustain to downgrade, so nothing has moved; '
                                     'but the arithmetic is now within a single strong session on each. The FOMC is '
                                     'the binary: hike odds have risen to roughly 32–38% from 10.7% on 15 Jul, and '
                                     "Warsh's framing — 'no tolerance for persistently elevated inflation,' 'prices "
                                     "are too high' — cuts against a dovish surprise, though June payrolls of 57k "
                                     'against 115k expected complicate the case for acting now. A hawkish outcome '
                                     're-arms the long end from below; a dovish or neutral one puts Treasury 5→4 '
                                     'genuinely in play within the week.'},
                            {'title': '(ii) Inflation anchor — held at 4; the approach resumed, marginally.',
                             'text': "5Y5Y closed 28 Jul at 2.2667%, up 0.5 bp from Monday's 2.2617% and now 3.33 bp "
                                     'from the 2.30% line on a close basis, with the intraday at 2.2627% (3.73 bp). '
                                     "That is a second-order move against Friday's 1.2 bp approach, but the "
                                     'direction turned back toward the trigger while crude was falling — a '
                                     'divergence worth watching, since it points at the FOMC and the pass-through '
                                     'story rather than at spot energy. The corroboration is unchanged: the 10Y '
                                     'breakeven closed 2.1955%, below its pre-war anchor for a third consecutive '
                                     'session, consistent with the curve pricing medium-term persistence rather than '
                                     "a near-term spike, and AAA gasoline's backfilled print stalled rather than "
                                     'accelerated. One close above 2.30% starts the clock; a second consecutive '
                                     'close confirms and takes the channel to 5/5 and the score to 26. The downgrade '
                                     '(sustained at or below the 2.142% anchor, 12.1 bp away) is not in play.'},
                            {'title': '(iii) Oil — held at 2; the close-basis gap to $95 widened to $12.92 before '
                                      "this morning's bounce narrowed it to $9.96.",
                             'text': 'Three consecutive daily declines took Brent from the 23 Jul $94.26 peak close '
                                     'to $82.08, a $12.18 unwind, and the active COA contract from $100.69 to '
                                     '$84.09. The 29 Jul intraday reverses part of that — $85.04, up $2.96, with COA '
                                     "at $87.61 — on Iran's frozen-asset transit threat and its rival Hormuz plan, "
                                     'which together reintroduce the risk that the Oman framework stalls on terms '
                                     'rather than on violence. The two-close rule held the channel at 2 through the '
                                     'entire $95 approach and now spares it a symmetric whipsaw on the way down and '
                                     'back up: a downgrade to 1 still needs a mediated pause AND a close at or below '
                                     'the $72.48 anchor, $9.60 away on the 28 Jul close. That is the closest the '
                                     'downgrade has been since early July, and if the Oman framework is signed it '
                                     "becomes the live question rather than the upgrade. (OPEC+'s modest August "
                                     'quota increase and the CPC Black Sea drone-strike risk remain the supply-side '
                                     'crosscurrents; Yanbu loadings are still running ~40% below their pre-19 Jul '
                                     'rate.)'}],
              'stage4Note': "Stage 4 is a credit/auction event. Threshold B is now disarmed on both legs — the 10Y's "
                            'second consecutive sub-line close formally reset its sustained status, and the 30Y sits '
                            '11.14 bp below its own leg.',
              'stage4': [{'title': 'Threshold A · 13 May 30Y auction.',
                          'text': 'Historical. Cleared at 5.050%; the 9 Jul re-opening cleared 5.06% with a 0.3 bp '
                                  'stop-through. The 30Y still trades above both marks, but by the least since that '
                                  "auction. No coupon supply until the August refunding, so today's FOMC statement "
                                  "and presser are the week's only long-duration pricing events."},
                         {'title': 'Threshold B · 30Y above 5.20% with 10Y above 4.65%.',
                          'text': 'Now disarmed on both legs. The 10Y closed 4.6062% on 28 Jul — 4.38 bp below the '
                                  'line and a second consecutive sub-line close, which formally resets the '
                                  'three-close-above run of 22–24 Jul; it prints 4.6144% intraday, still 3.56 bp '
                                  'below. The 30Y closed 5.0886%, 11.14 bp below its own leg, the widest gap since '
                                  '16 Jul. B re-arms on a hawkish FOMC, a strike resumption, or a landed hit on the '
                                  "Saudi export corridor; nothing else on this week's calendar reaches it."},
                         {'title': 'Threshold C · MOVE above 130.',
                          'text': 'Far off — 76.09 on the last confirmed close, and now moving down rather than up. '
                                  "The same print that pushes C further away brings the Treasury channel's own "
                                  'downgrade closer; the two read the same number in opposite directions.'}],
              'crossAsset': 'The unwind ran a third session and then stopped. Crude, European gas and Asia LNG all '
                            'fell again into the 28 Jul close (Brent $82.08, TTF €57.74, JGLA ¥3,418) and all three '
                            "bounced this morning or held — Brent +$2.96, TTF +€1.37 — on Iran's transit threat "
                            'rather than on any change in the strike picture. The Treasury curve rallied through the '
                            'close and gave a little back intraday, the dollar was flat for a second session at '
                            '101.38, and MOVE finally followed spot risk lower after two sessions of refusing to. '
                            'That last point is the meaningful one: rates vol and spot risk are repricing together '
                            "again, which is what makes the Treasury channel's two-leg downgrade a live proposition "
                            'instead of a theoretical one. US Henry Hub is now 13.5% BELOW pre-war, its widest '
                            'discount of the war — the Hormuz/LNG-routing signature, not a global-energy shock, in '
                            "its clearest form yet. The political channel's data fog partly lifted: both gasoline "
                            'series backfilled their 27 Jul prints, and both said the same thing — pass-through '
                            'continuing (DOE +9.5¢ on the week) but the daily pump series stalling exactly at the '
                            'trigger.'},
 'channels': [{'name': 'Maritime denial',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 (max). Strait closed to commercial traffic, day ~151; transit activity at a '
                            'war low (one recorded transit on 25 Jul); 43 Arabian Gulf crude tankers with AIS gaps '
                            '15–22 Jul, a four-year high; 24 dark tankers in the Kharg waiting area; blockade and '
                            "escort operation fully operational despite the pause. Iran's new frozen-asset transit "
                            'threat narrows access further, not less.',
               'upgrade': 'at max.',
               'downgrade': 'verified reopening (escorted convoys) with traffic above 25% of normal for 10 sessions '
                            '→ to 3–4.'},
              {'name': 'Oil price shock',
               'score': 2,
               'state': 'hold',
               'rationale': 'Held at 2. 28 Jul close $82.08 (–$3.79, third straight decline), $12.92 below the $95 '
                            'trigger and $9.60 above the $72.48 anchor — the closest the downgrade has been since '
                            "early July. Intraday $85.04 (+$2.96) on Iran's transit threat; active COA $87.61 vs "
                            "Tuesday's $84.09 close.",
               'upgrade': 'Brent above $95 sustained → to 3.',
               'downgrade': 'mediated pause + close at/below the $72.48 anchor → to 1.'},
              {'name': 'US inflation impulse',
               'score': 4,
               'state': 'hold',
               'rationale': 'Held at 4 — the approach resumed. 5Y5Y closed 2.2667% (+0.5 bp from Monday), 3.33 bp '
                            'from the line; intraday 2.2627%. The turn back toward the trigger came while crude was '
                            'falling, pointing at the FOMC rather than spot energy. 10Y breakeven closed 2.1955%, '
                            'below its pre-war anchor for a third session.',
               'upgrade': '5Y5Y sustained above 2.30% → to 5.',
               'downgrade': '5Y5Y sustained at/below the 2.142% pre-war anchor → to 3.'},
              {'name': 'Treasury stress',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 — but both downgrade legs moved toward release in the same session for the '
                            'first time in the war. 30Y closed 5.0886%, cushion above the 5.00% leg cut from 13.65 '
                            "bp to 8.86 bp (third consecutive session toward it); MOVE's confirmed close fell 1.12 "
                            'to 76.09, 1.09 pts above its 75 leg. Neither cleared and neither has sustained, so '
                            "nothing moved — but this is now the score's most probable next step, and it is a "
                            'downgrade.',
               'upgrade': 'at max.',
               'downgrade': '30Y close under 5.00% with MOVE under 75 sustained → to 4.'},
              {'name': 'Political stress',
               'score': 4,
               'state': 'hold',
               'rationale': "Held at 4 — the blackout cleared and the answer was a stall. AAA's backfilled 27 Jul "
                            'print came in at $4.75, FLAT, ending the nine-session run of rises exactly ON the '
                            'trigger without going through it; 28–29 Jul are still pending. The overdue DOE weekly '
                            'landed at $4.096, +9.5¢, corroborating continued pass-through. Evaluated on confirmed '
                            'prints only.',
               'upgrade': 'gasoline above $4.75 sustained → to 5.',
               'downgrade': 'toward the $3.52 pre-war level → to 3.'},
              {'name': 'Escalation risk',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 (max). The pause reached a fourth night and the Netanyahu visit produced no '
                            'resumption signal — the strongest de-escalation sequence of the war — but Iran hardened '
                            'its transit terms in the same 24 hours and no mediated stand-down has been declared. A '
                            'fourth quiet night and a competing draft framework are steps toward a downgrade, not '
                            'the event.',
               'upgrade': 'at max.',
               'downgrade': 'mediated stand-down + talks resume → to 4–3.'}],
 'scoreTotal': 'CRISIS band — an eleventh session at 25. The geopolitical tape produced its best 24 hours of the war '
               '(fourth quiet night, Netanyahu visit without a reset, an actual Omani framework tabled) and Iran '
               'answered by hardening its terms; crude split the difference. The substantive change is on rates: '
               'both Treasury downgrade legs moved toward release together for the first time, making 5→4 the '
               "score's most probable next step — and today's FOMC can move two market channels at once.",
 'whatsChanged': {'title': "4 · What's changed since the last edition (28 Jul → 29 Jul AM)",
                  'items': ['Score holds at 25/30 for an eleventh session. No channel moved — but the Treasury '
                            "channel's downgrade test came within one strong session on both legs. Source: "
                            'Bloomberg.',
                            'The strike pause reached a fourth consecutive night and survived the Netanyahu visit. '
                            'No new US strikes 25–28 Jul — the longest pause of the war, following 13 consecutive '
                            'nights of attacks. The Netanyahu–Trump White House meeting on 28 Jul was closed-press; '
                            "an Israeli official described 'an excellent and comprehensive discussion on the key "
                            "issues of the day, first and foremost Iran' and an 'ironclad' commitment against an "
                            "Iranian nuclear weapon, and the White House called the day's leader meetings 'positive "
                            "and productive.' No resumption signal emerged; the naval blockade is unchanged. Source: "
                            'DoD / White House / UPI / Jerusalem Post / NBC.',
                            'Oman tabled a Malacca-model framework — and Iran countered with its own. Omani FM Badr '
                            "Al Busaidi chaired a GCC virtual ministerial on freedom of navigation; Oman's proposal "
                            'is joint management with voluntary vessel fees, explicitly barring unilateral Iranian '
                            'control. Tehran countered with a temporary plan giving itself greater control of the '
                            'lanes. Nothing is signed, and the gap is now over terms rather than over whether to '
                            'talk. Source: The National / Oman MFA / US News / Fortune.',
                            'Iran threatened transit denial over the frozen-asset compensation scheme. The Khatam '
                            'al-Anbiya Central Headquarters said on 28 Jul that vessels of any country or company '
                            "accepting compensation from Iran's frozen assets 'will not be allowed' to transit, "
                            'rejecting responsibility for vessel damage. This is the proximate driver of this '
                            "morning's crude bounce. Source: Xinhua / Washington Times / Press TV (Tier 3, "
                            'corroborated).',
                            'Crude posted a third consecutive daily close decline, then bounced. Brent: $94.26 (23 '
                            'Jul) → $91.68 → $85.87 → $82.08 (28 Jul, –$3.79), a $12.18 unwind, with the active COA '
                            'contract down from $100.69 to $84.09. The 29 Jul intraday reverses part of it at $85.04 '
                            '(+$2.96), COA $87.61. TTF closed €57.74 and prints €59.11; Asia LNG printed fresh at '
                            '¥3,418 (–¥74). Source: Bloomberg.',
                            'Both Treasury downgrade legs moved toward release together — a first. The 30Y closed '
                            '5.0886%, cutting its cushion above the 5.00% leg from 13.65 bp to 8.86 bp in a third '
                            "consecutive session toward the line; MOVE's confirmed close fell 1.12 to 76.09, now "
                            '1.09 pts above its 75 leg, the closest of the war. Neither cleared; the channel held at '
                            '5. Source: Bloomberg.',
                            'Stage-4 Threshold B disarmed on the 10Y leg. The 10Y closed 4.6062% — a second '
                            'consecutive close below the 4.65% line after the three-close-above run of 22–24 Jul — '
                            "which formally resets the leg's sustained status. The 30Y closed 11.14 bp below its own "
                            '5.20% leg, the widest since 16 Jul. Source: Bloomberg.',
                            "The gasoline blackout cleared, and the pump series stalled at the trigger. AAA's "
                            'backfilled 27 Jul print landed at $4.75 — flat, ending nine consecutive rises exactly '
                            'ON the political→5 line. The overdue DOE weekly landed at $4.096, +9.5¢ from $4.001. '
                            'The 28–29 Jul AAA prints remain pending. Source: AUTMUSAG / USRFRUSA via Bloomberg.',
                            "The FOMC decides today. Statement 2pm ET, Warsh's presser 2:30 — his second meeting. "
                            'Hike odds are roughly 32–38% against 10.7% on 15 Jul; the June dot plot had 9 of 18 '
                            'officials projecting a 2026 hike, while June payrolls came in at 57k against 115k '
                            'expected. Source: CME FedWatch / Morningstar / CBS News.']},
 'scenarios': [{'name': 'Return to full war',
                'p': 26,
                'desc': 'Still the modal path but weakening for a third straight edition: a fourth quiet night, a '
                        'Netanyahu visit that produced no reset, and an actual Omani framework on the table. The '
                        "administration's posture is unchanged and the pause remains revocable, but the calendar's "
                        'biggest reset risk has now passed without one.',
                'path': 'Brent $105–140; MOVE above 90; oil to 3–4, political to 5, US-inflation to 5; score 28–30.'},
               {'name': 'Mediated pause — the ceasefire sticks',
                'p': 23,
                'desc': 'The strongest version of this scenario all war and now within a point of modal: four '
                        'consecutive quiet nights, a concrete Omani joint-management draft with voluntary fees, GCC '
                        'ministerial backing, and a Netanyahu meeting that did not reset Washington. Needs Iran to '
                        'accept a framework it does not control.',
                'path': 'Brent $74–85; MOVE under 72; Treasury→4, US-inflation→3, escalation→4; score falls toward '
                        '19–21.'},
               {'name': 'Deal collapse — talks stall on terms',
                'p': 20,
                'desc': "Raised: the dispute has migrated from whether to talk to who controls the lane. Iran's "
                        'rival plan and its frozen-asset transit threat both point at a framework that stalls on '
                        'terms rather than on violence — the version of failure this week actually risks.',
                'path': 'Brent $92–108; oil back to 3; 30Y back above 5.15% toward the 5.20% leg; score 26–27.'},
               {'name': 'Contained but violent — blockaded stalemate',
                'p': 18,
                'desc': 'Strikes stay paused at low intensity, escort-only transits continue, and neither the Omani '
                        'nor the Iranian draft is adopted — nothing is resolved and the blockade holds indefinitely.',
                'path': 'Brent $82–92; MOVE 72–82; risk premium $10–20/bbl; score holds 24–25.'},
               {'name': 'Regional relapse — Gulf energy infrastructure hit',
                'p': 13,
                'desc': 'No Houthi action since 25 Jul and the front has been quiet for four days, but the '
                        'demonstrated capability against Jizan and the near-miss at Yanbu stand, and Yanbu loadings '
                        'are still ~40% below their pre-19 Jul rate. A single landed hit on the export corridor '
                        'reactivates it.',
                'path': 'Brent $150+; emergency policy response; HY spreads above 500 bp; score 29–30.'}],
 'scenarioShift': 'Probability shifts from the 28 Jul edition: mediated pause +3 (20→23) — a fourth quiet night plus '
                  'a Netanyahu meeting that produced no reset is the strongest de-escalation sequence of the war; '
                  'deal collapse +2 (18→20) — the failure mode has migrated from violence to terms; full war –3 '
                  '(29→26) — still modal but weakening for a third edition; regional relapse –2 (15→13) on four '
                  "quiet days on the Saudi front; contained-but-violent unchanged (18). Driver: the calendar's "
                  'biggest reset risk passed without a reset, but the negotiation moved from access to control.',
 'watchlist': ["FOMC · statement 2pm ET today, Warsh presser 2:30. The session's dominant event and the one most "
               'likely to resolve the Treasury channel. Hike odds roughly 32–38% against 10.7% on 15 Jul; Warsh has '
               "said the Fed has 'no tolerance for persistently elevated inflation' and that 'prices are too high,' "
               'but June payrolls of 57k against 115k expected cut the other way. A hawkish outcome re-arms the long '
               'end and Stage-4 B; a dovish or neutral one puts Treasury 5→4 in play within the week and 5Y5Y back '
               'toward its own trigger.',
               'Treasury →4 (downgrade) — 8.86 bp and 1.09 pts away, both legs moving. The first session of the war '
               'in which the 30Y and MOVE moved toward release together. A 30Y close under 5.00% with MOVE under 75, '
               'sustained, takes the channel to 4 and the score to 24 — the first downgrade since 9 Jul.',
               'Political →5 ($4.75) — AT the line, and the run has stalled. The backfilled 27 Jul AAA print was '
               'flat, ending nine consecutive rises exactly on the threshold; 28–29 Jul are pending. With crude down '
               "three sessions the pump series may roll over before it breaks through — the DOE weekly's +9.5¢ "
               'argues the other way. Unresolved either direction.',
               'US-inflation →5 (5Y5Y above 2.30% sustained) — 3.33 bp, resuming. The 28 Jul close turned back '
               "toward the trigger while crude fell. Whether the FOMC extends that turn is the channel's live "
               'question.',
               "Whether Iran accepts a framework it does not control. Oman's draft is joint management with "
               "voluntary fees; Iran's counter concentrates control in its own hands, and the frozen-asset transit "
               'threat is a second lever on the same question. Acceptance collapses escalation risk and probably oil '
               'with it; rejection is the deal-collapse path.',
               'Whether the pause reaches a fifth and sixth night. Four nights is the longest of the war and nothing '
               'in the Netanyahu readout signalled resumption; a strike overnight reprices everything back in at '
               'full amplitude.',
               "Yanbu re-attack risk — the demonstrated tail, dormant four days. Jizan proved reach and Yanbu's "
               'intercepts held once; loadings are still ~40% below their pre-19 Jul rate. A hit that lands on the '
               'export corridor reprices crude, breakevens and bond vol together.',
               'Gas complex — verify the next JGLA print fresh. Asia LNG ¥3,418 on the 28 Jul close, a third '
               'consecutive easing; no 29 Jul print yet — never carried forward.'],
 'sourceLog': {'tier1Market': 'Bloomberg Terminal extract (US Iran BBG Data.xlsx, restated front-month continuation '
                              'series). Tickers: CO2/CL2 Comdty (front-month; the CL2 artifact persists — CL2 closed '
                              '$77.17 vs active CLA $79.26; WTI is read off the active board); COA/CLA Comdty '
                              '(active, unscored — COA closed $84.09, prints $87.61); NGA/TZTA/JGLA (JGLA printed '
                              'fresh 28 Jul at ¥3,418, –¥74; no 29 Jul print, flagged not carried); '
                              'USGG2YR/5YR/10YR/20YR/30YR; USYC2Y10; USGGBE10 (2.1955 — below the pre-war anchor for '
                              'a third session); USGG5Y5Y (2.2667 — 3.33 bp from the →5 trigger); SOFRRATE (lagged, '
                              '24 Jul, 3.64%); MOVE and VIX (28 Jul closes 76.09 / 18.21; 29 Jul lagged, carried and '
                              'labelled); DXY; AUTMUSAG (AAA pump — score reference; 27 Jul print backfilled at '
                              '$4.75, flat; 28–29 Jul pending) and USRFRUSA (DOE regular spot, weekly — '
                              'corroboration; overdue 27 Jul print backfilled at $4.096).',
               'tier1News': 'US DoD / White House via NPR, CBS News and Bloomberg (strike pause held a fourth '
                            "consecutive night; 'on a hold' framing; naval blockade fully operational), UPI / "
                            'Jerusalem Post / NBC News / The Forward / Al Jazeera (Netanyahu–Trump White House '
                            "meeting 28 Jul — closed press, 'positive and productive,' Iran 'first and foremost'), "
                            "The National / Oman Ministry of Foreign Affairs / Fortune / Bloomberg (Oman's "
                            "Malacca-model joint-management proposal with voluntary vessel fees; Badr Al Busaidi's "
                            "GCC virtual ministerial; the Iran–Oman technical track), US News (Iran's rival "
                            'temporary Hormuz plan giving itself greater control of transit lines), Xinhua / '
                            'Washington Times / ANI (Khatam al-Anbiya Central Headquarters statement of 28 Jul), CME '
                            'FedWatch via Morningstar / CBS News / Kiplinger (FOMC hike odds roughly 32–38% against '
                            '10.7% on 15 Jul; June dot plot 9 of 18 for a 2026 hike; June payrolls 57k vs 115k '
                            "expected; Warsh's 14 Jul testimony and Sintra remarks), Windward / straits.live / IMF "
                            'PortWatch (one recorded Hormuz transit on 25 Jul; 43 Arabian Gulf tankers with AIS gaps '
                            '15–22 Jul, a four-year high; 24 dark tankers in the Kharg waiting area; Yanbu loadings '
                            '5.16 → 3.09 mb/d after 19 Jul), Al Jazeera / TechTimes citing NASA FIRMS (Jizan '
                            'refinery fire and Yanbu intercepts of 25 Jul — no further exchange since), Bloomberg / '
                            'TradingEconomics (OPEC+ August quota increase; CPC Black Sea drone-strike risk '
                            'persists).',
               'tier3': 'The Khatam al-Anbiya Central Headquarters statement is an Iranian military declaration of '
                        'intent, reported by Xinhua and Press TV and corroborated by Tier 1 outlets; it is treated '
                        'as a stated policy position, not a verified change in transit access, and is used here only '
                        "to explain the crude bounce, not to move a channel. Iran's earlier claim to 'control' the "
                        'strait remains a negotiating-posture claim. The Houthi claim to the Jizan and Yanbu strikes '
                        'is a combatant claim — the Jizan fires are corroborated by satellite thermal data. IRNA and '
                        'Mehr not used this edition.'},
 'protocol': [{'step': 'Refresh the Bloomberg extract',
               'detail': 'Parse the latest dated row (29 Jul) as intraday; reclassify 28 Jul as a final close; '
                         're-map columns via the robust scan (front-month CO2/CL2; both gasoline series checked — '
                         'AAA and DOE both backfilled their 27 Jul prints, AAA 28–29 Jul still pending; JGLA checked '
                         'fresh, printed 28 Jul ¥3,418, no 29 Jul print, flagged not carried; MOVE/VIX 29 Jul '
                         'lagged, 28 Jul closes carried and labelled; SOFR lagged 24 Jul).'},
              {'step': 'Recompute deltas',
               'detail': 'd/d vs the 28 Jul close; w/w vs the close five trading sessions back (22 Jul this '
                         'edition); vs-pre-war vs the 27 Feb 2026 anchor (re-verified, unchanged).'},
              {'step': 'Re-evaluate the six channels',
               'detail': 'Market channels move on confirmed closes only — all held: oil 2 (close $82.08, $12.92 '
                         'below $95, $9.60 above the anchor); Treasury 5 (30Y 5.0886% above 5.00%, cushion 8.86 bp; '
                         'MOVE 76.09 above 75 by 1.09 — both legs moving toward release for the first time); '
                         'US-inflation 4 (5Y5Y 2.2667%, 3.33 bp under 2.30%); political 4 (AAA $4.75 confirmed, '
                         'flat, exactly on the line). Maritime/escalation event-based, both maxed — a fourth quiet '
                         'night and a Netanyahu meeting without a reset are steps, not a mediated stand-down.'},
              {'step': 'Reconcile against the prior edition',
               'detail': 'The US session took the tape DOWN through the Asia snapshot for a THIRD consecutive '
                         'session — a first — and by the widest margin of the war: Brent $85.40 → close $82.08 '
                         '(–$3.32); WTI $79.77 → $77.17; 10Y 4.6345% → 4.6062%; 30Y 5.1239% → 5.0886%; Henry Hub '
                         '$2.751 → $2.662. Two series went the other way: TTF €56.98 → €57.737 and 5Y5Y 2.2603% → '
                         '2.2667%.'},
              {'step': 'Update scenarios and watchlist',
               'detail': 'Re-rank catalysts: the FOMC (2pm ET today) is dominant; Treasury→4 (8.86 bp and 1.09 pts, '
                         'both legs moving) replaces political→5 as the nearest score move; US-inflation→5 3.33 bp '
                         'and resuming; whether Iran accepts a framework it does not control. Mediated pause 20→23, '
                         'deal collapse 18→20, full war 29→26, regional relapse 15→13.'}],
 'methodology': {'scale': 'Six transmission channels (maritime denial, oil, US inflation impulse, Treasury stress, '
                          'political stress, escalation risk), each 0–5, summed to 0–30. Bands: 0–7 watch · 8–14 '
                          'stress · 15–21 systemic-risk watch · 22–30 crisis. Market channels move only on a '
                          'confirmed close through a trigger; escalation-risk is event-based. Hysteresis note: '
                          'upgrades fire on a sustained break; downgrades only on a sustained reversal past a wider '
                          'threshold — deliberately, to avoid whipsawing. This edition is the clearest test of that '
                          "discipline on the downside so far: the Treasury channel's two downgrade legs both moved "
                          'toward release in the same session (30Y 8.86 bp above 5.00%, MOVE 1.09 pts above 75), and '
                          'the channel still held at 5, because the rule requires both legs to clear simultaneously '
                          'AND to sustain. The same rule worked in the other direction on oil, which held at 2 '
                          'through a $95 approach four sessions ago and through a $12.18 unwind since. Stage-4 '
                          "Threshold B's 10Y leg, by contrast, has now formally reset: two consecutive closes below "
                          '4.65% undo the three-close-above run of 22–24 Jul. Scale cap: maritime and escalation are '
                          "both at 5/5, so neither the pause's extension to a fourth night nor a Netanyahu meeting "
                          'that produced no reset (already-maxed channels) can move the score — only the four market '
                          'channels can, in either direction.',
                 'gasoline': 'Political-stress is scored on AUTMUSAG (AAA all-grades retail pump; pre-war $3.52, '
                             'peak $5.18, latest confirmed print $4.75 on 27 Jul — flat, ending nine consecutive '
                             'rises exactly on the $4.75 threshold); the 28–29 Jul prints are pending and the '
                             'channel holds until confirmed — per the discipline established after the JGLA '
                             'stale-carry episode, a missing print is flagged, never carried forward. Both series '
                             "backfilled their overdue 27 Jul prints here, which is why yesterday's four-session "
                             'blackout has partly cleared. USRFRUSA (DOE regular spot; pre-war ~$2.94, peak $4.50, '
                             'latest $4.096 on 27 Jul, +9.5¢) is tracked alongside.',
                 'anchor': 'Brent $72.48; WTI $67.02; 2Y 3.375%; 5Y 3.502%; 10Y 3.938%; 30Y 4.611%; 2s10s +55.64 bp; '
                           '5Y5Y 2.142%; 10Y BE 2.257%; MOVE 73.38; VIX 19.86; DXY 97.608; gasoline (AAA) $3.52; '
                           'Henry Hub $3.06; TTF €31.23; Asia LNG ¥1,669. (Re-verified — unchanged.) Brent +17.3%, '
                           'WTI +19.3%, TTF +89.3%, Asia LNG +104.8%; the 30Y (+48.6 bp), 10Y (+67.7 bp), 5Y5Y '
                           '(+12.1 bp), MOVE (+2.71) and DXY (+3.77) sit above their anchors; the 10Y breakeven '
                           '(–6.1 bp) is below its anchor for a third session; VIX and Henry Hub remain below '
                           'pre-war, Henry Hub at –13.5%.',
                 'intraday': 'The latest dated row is a Singapore-AM snapshot; US hours set the close (recent Brent '
                             'gaps: +$1.91, +$0.60, +$3.10, –$1.81, –$2.01, –$3.32 — 28 Jul was the THIRD straight '
                             'close below the snapshot, a first, and the widest downside miss of the war). MOVE and '
                             'VIX carry the 28 Jul closes, labelled; the UST curve printed live; JGLA and AAA had no '
                             '29 Jul print and are flagged, not carried; CL2 remains an artifact against active CLA. '
                             'Triggers are evaluated on confirmed closes; escalation-risk is event-based. '
                             'Restated-series levels are not comparable with pre-restatement editions, though the '
                             'directional analysis is continuous.'}}


with open("editions.json", "w") as f:
    json.dump(EDITIONS, f, indent=2, ensure_ascii=False)

print("Wrote editions.json with full sections for:", list(EDITIONS.keys()))
