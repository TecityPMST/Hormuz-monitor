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
# 2026-08-03 (previous)
# ======================================================================
EDITIONS['2026-08-03'] = {'label': '3 Aug 2026',
 'editionLine': 'Daily edition · 3 Aug 2026 intraday · Bloomberg · Singapore 3 Aug AM update',
 'score': 26,
 'band': 'CRISIS',
 'sequencing': '25 → 26 → 26',
 'sessionNote': 'Score held · three war records on the 31 Jul close · escalation downgrade '
                'live for the first time since 9 Jul',
 'headline': 'Note: 3 Aug figures are intraday prints; the last confirmed close is Friday 31 '
             'Jul. The integrity check clears — the 31 Jul row has refreshed properly and '
             'differs materially from the snapshot published for it, so it is a true close. '
             'Score HOLDS at 26/30 — all six channels unchanged (maritime 5, oil 2, US '
             'inflation 5, Treasury 5, political 4, escalation 5), but for the first time in '
             'the war the monitor carries a live downgrade candidate and a live upgrade '
             'candidate at the same time. Two things happened over the weekend and they point '
             'in opposite directions. First, and larger for markets: the US session on '
             'Friday, which the Singapore morning snapshot had missed, was a violent bear '
             'steepener. The 30Y closed at 5.2724%, the 10Y at 4.7347% and 5Y5Y forward '
             'inflation at 2.3597% — all three the highest readings of the war — and MOVE '
             'jumped 5.93 to 83.02, its highest since 19 May. Stage-4 Threshold B is now '
             'satisfied on a third consecutive confirmed close, and the 30Y sits 22.24 bp '
             'above the 13 May auction stop, the widest margin of the war, going into a '
             'refunding week. Second, and larger for the narrative: President Trump said on 2 '
             "Aug that he had cancelled a planned strike package he described as 'the biggest "
             "attack since World War II' and announced a new round of talks beginning Monday "
             '3 Aug with Oman mediating. Iran immediately rejected the framing — Tehran '
             "denies asking for the pause, denies any Hormuz deal, calling the claim 'a new "
             "lie', and says what is actually near-final is a bilateral Iran–Oman negotiation "
             'on a NEW corridor, not a reopening of the old one. This is the first genuinely '
             'live downgrade candidate the escalation channel has had since it maxed on 9 '
             'July, and it is deliberately not taken today: the talks had not convened at the '
             'time of this snapshot, no principal has confirmed terms, an LNG carrier loaded '
             'with Qatari cargo was struck mid-transit on 31 Jul, UKMTO logged an explosion '
             'beside a tanker off Khasab on 2 Aug, and the hysteresis rule exists precisely '
             'to stop a channel moving on an announcement. Crude, characteristically, moved '
             'first and moved hard: Brent front-month prints $81.56 this morning, –$6.37 on '
             'the day and the largest single-session decline since 25 May, with OPEC+ having '
             'approved a final +188k b/d for September on 2 Aug. So the tape is now split '
             'cleanly in two. The energy complex is trading the diplomacy; the bond market is '
             'trading the Federal Reserve, and it set three war records on Friday doing it. '
             'Sequencing 25 → 26 → 26.',
 'tape': {'note': '3 Aug 2026 readings are intraday prints from the Singapore morning. The 31 '
                  'Jul row has refreshed and is a confirmed close; the integrity check '
                  'clears. d/d is 3 Aug intraday vs the 31 Jul close; w/w is vs the 27 Jul '
                  'close (five sheet-rows back); vs-pre-war is against the 27 Feb 2026 close. '
                  'Restated continuation series (front-month CO2/CL2) in force. The ICE Brent '
                  'September contract expired on 31 Jul, so the active COA now references a '
                  'new contract and the front-month/active gap has widened again in the AM '
                  'snapshot; the scored CO2 continuation series is unaffected.',
          'oilGasHeader': ['Benchmark',
                           'Intraday 3 Aug',
                           '∆ d/d',
                           '∆ vs pre-war close (27 Feb)',
                           'BBG ticker'],
          'oilGas': [['Brent front-month',
                      '$81.56 /bbl (H 82.05 / L 79.83)',
                      '–$6.37 (–$4.31 w/w)',
                      'from $72.48 (+12.5%) — a $9.08/bbl premium, the narrowest of the war '
                      'since 10 Jul. The largest single-session decline since 25 May, on '
                      'Trump’s cancelled strike package and the OPEC+ September increase; '
                      'active COA prints $84.12',
                      'CO2 Comdty (Close)'],
                     ['Brent · 31 Jul close (last confirmed)',
                      '$87.93 /bbl',
                      '+$1.05 vs the 30 Jul close $86.88',
                      '$7.07 below the $95 trigger on a close basis; $15.45 above the $72.48 '
                      'anchor. July finished +20.6% from the 30 Jun close of $72.92. Friday’s '
                      'close ran $1.97 ABOVE my Friday-morning snapshot — the US session bid '
                      'crude back up before the weekend’s diplomacy took it apart.',
                      'CO2 Comdty (Close)'],
                     ['WTI front-month',
                      '$78.42 /bbl',
                      '–$3.07 (–$1.83 w/w)',
                      'from $67.02 (+17.0%) — the CL2 artifact against the active contract '
                      'persists, CLA prints $80.77 against CL2’s $78.42',
                      'CL2 Comdty (Close)'],
                     ['Brent–WTI spread',
                      '$3.14 /bbl',
                      'narrowed $3.30 on the day',
                      '$3.35 on the active contracts (COA $84.12 / CLA $80.77). Brent has '
                      'given back the Hormuz-specific premium faster than WTI, which is what '
                      'a diplomacy trade looks like rather than a demand trade',
                      'derived'],
                     ['Henry Hub natural gas',
                      '$2.766 /MMBtu',
                      '+$0.019 (–$0.022 w/w)',
                      'from $3.06 (–9.7%) — US gas still BELOW pre-war after twenty-two weeks '
                      'of war; the Hormuz/LNG-routing signature is intact and this remains a '
                      'routing shock, not a global-energy shock',
                      'NGA Comdty (Close)'],
                     ['TTF Dutch gas (active)',
                      '€56.300 /MWh',
                      '–€2.771 (–€2.031 w/w)',
                      'from €31.23 (+80.3%) — the lowest since 16 Jul and €7.35 below the 24 '
                      'Jul war record of €63.65. European gas is trading the same '
                      'de-escalation headline as crude',
                      'TZTA Comdty (Close)'],
                     ['Japan/Asia LNG (31 Jul close — no 3 Aug print)',
                      '¥3,440',
                      '–¥87 vs the 30 Jul ¥3,527',
                      'from ¥1,669 (+106.1%) — the series turned lower on Friday for the '
                      'first time in three sessions. No 3 Aug print; flagged, NOT carried '
                      'forward. Hormuz still moves roughly a fifth of global LNG, and a '
                      'Qatari-laden carrier was struck in transit on 31 Jul',
                      'JGLA Comdty (Close)']],
          'ustNote': '3 Aug 2026 yields are intraday. The 31 Jul close is confirmed and is '
                     'the reading on which every trigger and Stage-4 test below is judged. '
                     'd/d is vs the 31 Jul close; w/w vs 27 Jul. Friday’s US session repriced '
                     'the long end hard after my morning snapshot — see the reconciliation in '
                     'section 4 and the intraday caveat in section 9.',
          'ustHeader': ['Tenor',
                        'Yield (%) — intraday 3 Aug',
                        '∆ d/d (bp)',
                        '∆ w/w (bp)',
                        '∆ vs pre-war (bp)',
                        'BBG ticker'],
          'ust': [['2-year UST',
                   '4.25',
                   '–4.6',
                   '–7.7',
                   '+87.1 (from 3.37%) — the front end keeps grinding lower as the long end '
                   'sells off',
                   'USGG2YR Index'],
                  ['5-year UST',
                   '4.40',
                   '–4.6',
                   '–0.1',
                   '+90.1 (from 3.50%)',
                   'USGG5YR Index'],
                  ['10-year UST',
                   '4.69',
                   '–4.1',
                   '+4.5',
                   '+75.6 (from 3.94%) — the 31 Jul close of 4.7347% is the highest of the '
                   'war; this morning’s 4.6939% is still 4.39 bp ABOVE the 4.65% Stage-4 leg, '
                   'a third session clear of it',
                   'USGG10YR Index'],
                  ['30-year UST',
                   '5.24',
                   '–3.5',
                   '+10.1',
                   '+62.6 (from 4.61%) — the 31 Jul close of 5.2724% is the highest of the '
                   'war and 22.24 bp above the 13 May auction stop, the widest margin '
                   'recorded. This morning’s 5.2370% remains 3.70 bp above the 5.20% Stage-4 '
                   'leg and 23.70 bp above the 5.00% downgrade line',
                   'USGG30YR Index'],
                  ['2s10s spread',
                   '+44.6 bp',
                   '+0.7',
                   '+12.2',
                   '–11.0 (still flatter than pre-war) — but the steepest since 26 May and '
                   '20.4 bp off the 24 Jun war low of +24.25 bp. A bear steepener, four '
                   'sessions running',
                   'USYC2Y10 Index'],
                  ['10Y breakeven inflation',
                   '2.279',
                   '–0.6',
                   '+7.6',
                   '+2.2 (from 2.2569%) — back above its pre-war anchor after touching it '
                   'exactly on 31 Jul’s snapshot; the Friday close of 2.2846% was the highest '
                   'since 3 Jul',
                   'USGGBE10 Index'],
                  ['5Y5Y forward inflation',
                   '2.337',
                   '–2.3',
                   '+7.5',
                   '+19.5 (from 2.14%) — the 31 Jul close of 2.3597% is the highest of the '
                   'war and a fourth consecutive close above the 2.30% trigger. The '
                   'US-inflation channel, upgraded 4→5 on 31 Jul, is being confirmed rather '
                   'than faded',
                   'USGG5Y5Y Index'],
                  ['SOFR (blank 31 Jul and 3 Aug)',
                   '3.65',
                   '—',
                   'no print',
                   'last printed 3.65 on 30 Jul; two consecutive blank sessions, flagged and '
                   'NOT carried as fresh',
                   'SOFRRATE Index']],
          'crossHeader': ['Gauge', 'Latest', 'As of', '∆ vs pre-war', 'Interpretation'],
          'cross': [['DXY',
                     '99.59',
                     '3 Aug intraday',
                     '+1.98 (from 97.61)',
                     'Down 0.32 this morning and down 1.94 on the week, the lowest since 16 '
                     'June. The dollar has now fallen through a week in which the long end '
                     'sold off 10 bp. That combination — yields up, currency down — is the '
                     'signature of an inflation-credibility repricing rather than a haven '
                     'bid, and it is the single most consistent cross-asset message of the '
                     'past fortnight.'],
                    ['MOVE',
                     '83.02',
                     '31 Jul close (no 3 Aug print)',
                     '+9.64 (from 73.38)',
                     'Up 5.93 on Friday and the highest since 19 May. Rates volatility has '
                     'now risen in three of the last four sessions and sits 8.02 pts ABOVE '
                     'the 75 line that forms the second leg of the Treasury downgrade. It is '
                     'still 46.98 pts below the 130 Stage-4 Threshold C and well under the '
                     '115.02 war high of 26 March, but the direction into a refunding week is '
                     'the wrong one.'],
                    ['VIX',
                     '15.99',
                     '31 Jul close (no 3 Aug print)',
                     '–3.87 (from 19.86)',
                     'Down 1.10 to its lowest since 15 July. Equity volatility is now nearly '
                     '4 points BELOW pre-war while rates volatility is 9.64 points above it. '
                     'The divergence is the whole story: equity investors are pricing a war '
                     'that ends in a deal, bond investors are pricing a central bank that has '
                     'lost the inflation argument.'],
                    ['AAA gasoline',
                     '$4.76 /gal',
                     '30 Jul print (31 Jul–3 Aug blank)',
                     '+$1.24 (from $3.52, +35.2%)',
                     'Political-stress score reference. The 30 Jul print backfilled at $4.76 '
                     '— the FIRST print above the $4.75 trigger, and the highest since 10 '
                     'June — after four straight sessions exactly on the line. The series is '
                     'then blank for 31 Jul and 3 Aug. One close above a trigger is not a '
                     'sustained break; the channel needs a second consecutive close and the '
                     'backfill has not arrived.'],
                    ['DOE gasoline',
                     '$4.096 /gal',
                     '27 Jul weekly print',
                     '+$1.16 (from ~$2.94, +39.4%)',
                     'Corroboration only; the next weekly print is due 3 Aug US time and is '
                     'not yet in the extract. EIA has crude stocks ~6% and gasoline stocks '
                     '~7% below the five-year average with refinery utilisation at 97.2%, so '
                     'the binding constraint on the pump is refining capacity, not crude — a '
                     'point Exxon and Chevron both made publicly on 1 Aug.']],
          'gasChartNote': 'AUTMUSAG (AAA all-grades retail pump, daily) is the '
                          'political-stress score reference (pre-war $3.52, peak $5.18, '
                          'latest confirmed print $4.76 on 30 Jul; 31 Jul and 3 Aug blank); '
                          'USRFRUSA (DOE regular-grade retail spot, weekly) is the '
                          'complementary gauge (pre-war ~$2.94, peak $4.50, latest $4.096 for '
                          'the week of 27 Jul). The dotted line is the $4.75 political→5 '
                          'threshold. The scored series printed exactly $4.75 on 24, 27, 28 '
                          'and 29 Jul and then $4.76 on 30 Jul — its first print through the '
                          'line and its highest since 10 June — before going dark for two '
                          'sessions. AAA’s separately published regular-grade national '
                          'average was $4.098 on 30 Jul against $4.091 a week earlier, so the '
                          'corroborating series still shows a stall; on-highway diesel, by '
                          'contrast, rose 17.9 cents in the week to 27 Jul.',
          'straitHeader': ['Indicator', 'Current reading', 'Source'],
          'strait': [['Strait closed · day ~157',
                      'Closed since 28 Feb. Traffic remains at crisis levels and the two '
                      'trackers are not directly comparable: Kpler counted 10 commodity '
                      'vessels crossing on 31 Jul (7 out, 3 in, two with transponders '
                      'disabled) after 4 on 30 Jul and 15 on 29 Jul, against a pre-war '
                      'baseline above 100 a day; Windward, which counts all vessels, logged '
                      'just 5 in the 24 hours to 31 Jul, three of them OFAC-designated, '
                      'against roughly 140 a day pre-crisis, and recorded 66 vessels '
                      'GPS-jammed in the Gulf that day. Lloyd’s List Intelligence puts the '
                      'week to 26 Jul at 39 total transits against 82 the week before, with '
                      '70% of traffic untraceable on AIS and inbound Gulf traffic down more '
                      'than 90%. War-risk cover is quoted at 7.5–10% of hull value against '
                      '1–3% pre-escalation.',
                      'Kpler via The National / Windward / Lloyd’s List Intelligence'],
                     ['TRUMP CANCELS A STRIKE PACKAGE AND ANNOUNCES TALKS FOR 3 AUGUST',
                      'On 2 Aug the President said he had called off what would have been '
                      '‘the biggest attack since World War II’ on Iran and announced a new '
                      'round of negotiations beginning Monday 3 Aug, mediated by Oman with '
                      'Saudi Arabia, the UAE and Qatar involved. He set no deadline. He had '
                      'said on 1 Aug that ‘the perimeters of a deal’ included ‘immediate, '
                      'complete and total opening of the Hormuz Strait’ and an end to Iran’s '
                      'nuclear threat. Saudi Crown Prince Mohammed bin Salman phoned Trump '
                      'the same weekend urging de-escalation; Pakistani and Qatari '
                      'intermediaries were reported as cautiously optimistic. No Tier 1 '
                      'outlet reported a new CENTCOM or Israeli strike on Iran between 31 Jul '
                      'and 3 Aug.',
                      'Al Jazeera / Bloomberg / France 24 / ABC News / CNN'],
                     ['Iran rejects the framing — and describes a different negotiation',
                      'Tehran denied asking Trump to hold off and denied that any Hormuz deal '
                      'had been agreed, calling the claim ‘a new lie.’ Foreign Minister '
                      'Araghchi said talks with OMAN are ‘on the way to being finalised’ and '
                      'spokesman Baghaei said the two sides expect to agree a NEW route — '
                      'neither the existing northern nor the southern corridor — respecting '
                      '‘the sovereign rights of both sides.’ That is a bilateral '
                      'corridor-management negotiation, not the reopening the US described. '
                      'President Pezeshkian on 3 Aug urged Washington to ‘remain committed’ '
                      'to the June MoU. Al Jazeera assesses the strait as still effectively '
                      'blocked.',
                      'Al Jazeera / Times of Israel / ABC News'],
                     ['The waterway stayed hostile through the diplomacy',
                      'The LNG carrier Gaslog Shanghai, laden with Qatari cargo, was struck '
                      'by a projectile while transiting near the western entrance off Oman on '
                      '31 Jul; UKMTO reported no environmental impact. On 2 Aug UKMTO '
                      'received a report of an explosion in close proximity to a tanker about '
                      '20 nautical miles north-east of Khasab. Kuwait’s defence ministry said '
                      'on 31 Jul it intercepted hostile drones over Kuwaiti territory, with '
                      'Iran claiming it had targeted Ahmad al-Jaber Air Base. The IRGC '
                      'claimed on 31 Jul to have stopped two US-escorted tankers in the '
                      'strait (Tier 3, no Tier 1 corroboration).',
                      'Bloomberg / UKMTO / Al Jazeera / CBS News / IRNA-Tasnim (Tier 3)'],
                     ['OPEC+ delivers September barrels; energy infrastructure unchanged',
                      'Eight OPEC+ producers agreed on 2 Aug to raise September quotas by '
                      '188,000 b/d, completing the rollback of the 1.65 mb/d voluntary '
                      'tranche. A fourth-quarter pause was briefed to Reuters by sources but '
                      'was NOT written into the communiqué; the next meetings are 6 Sep and 4 '
                      'Oct, and the JMMC used the occasion to stress ‘safeguarding '
                      'international maritime shipping lanes.’ The physical picture is '
                      'unchanged from Friday: Aramco’s 400k b/d Jizan complex stays offline '
                      'to about mid-August, satellite imagery still shows burn scars on four '
                      'of six Abqaiq spheroids with no Aramco comment, and Damietta’s '
                      'operational status after the 29–30 Jul drone strike remains '
                      'unreported. The Red Sea and Bab al-Mandeb were described as relatively '
                      'calm on 2 Aug.',
                      'CNBC / Reuters / Al Arabiya / Maritime Executive / Al Jazeera']]},
 'analysis': {'intro': 'The shock holds at 26/30 and the two halves of the tape have '
                       'separated. On Friday, after the Singapore snapshot had closed, the US '
                       'bond market set three war records in a single session: the 30Y at '
                       '5.2724%, the 10Y at 4.7347% and 5Y5Y forward inflation at 2.3597%, '
                       'with MOVE up 5.93 to 83.02. Stage-4 Threshold B is satisfied on a '
                       'third consecutive close and the 30Y is now 22.24 bp above the May '
                       'auction stop with the quarterly refunding calendar landing this week. '
                       'Over the weekend the geopolitical track went the other way: a planned '
                       'US strike package was cancelled, talks were announced for today with '
                       'Oman mediating, and no Tier 1 outlet reported a new strike on Iran in '
                       'the window. Crude has taken that at face value — Brent front-month is '
                       '$81.56 this morning, down $6.37 and the largest one-day fall since 25 '
                       'May, helped by OPEC+ approving a final +188k b/d for September. The '
                       'escalation channel is therefore, for the first time since 9 July, '
                       'holding a live downgrade candidate rather than an unusable maximum. '
                       'It is not taken this edition, for the same reason the US-inflation '
                       'upgrade was not taken on 30 July: the evidence is one session old, '
                       'the principals disagree about what was agreed, and the waterway was '
                       'still being shot at while the announcement was made.',
              'bondYieldNote': '3 Aug yields are intraday; the 31 Jul close is confirmed and '
                               'every trigger runs off it. No channel moved. Score holds at '
                               '26/30, with the escalation downgrade now live and '
                               'deliberately deferred.',
              'bondYield': [{'title': '(i) Treasury — held at 5, and Friday made the '
                                      'downgrade look further away, not closer.',
                             'text': 'The 30Y closed at 5.2724% on 31 Jul, the highest of the '
                                     'war, 7.59 bp above my morning snapshot and 22.24 bp '
                                     'above the 13 May auction stop of 5.050%. The 10Y closed '
                                     'at 4.7347%, also a war record. Both downgrade legs now '
                                     'fail comprehensively: the 30Y is 27.24 bp above the '
                                     '5.00% line on the close and 23.70 bp above it intraday, '
                                     'and MOVE at 83.02 is 8.02 pts above the 75 leg after '
                                     'rising 5.93 in a session. This morning gives back a few '
                                     'basis points across the curve — 2Y –4.6 bp, 5Y –4.6 bp, '
                                     '10Y –4.1 bp, 30Y –3.5 bp — but that is a partial '
                                     'retracement of a 10 bp weekly move in the long end, and '
                                     'the curve continued to steepen through it: 2s10s at '
                                     '+44.6 bp is the steepest since 26 May. The character '
                                     'has not changed since the FOMC: a bear steepener with '
                                     'breakevens up and the dollar down to its lowest since '
                                     '16 June. What makes this edition different from the '
                                     'last is the calendar. Treasury publishes its quarterly '
                                     'marketable borrowing estimates today and the refunding '
                                     'statement on Wednesday 5 August, with the 30Y refunding '
                                     'leg auctioning in the week of 10 August, into a long '
                                     'end that has just set a war high.'},
                            {'title': '(ii) US inflation impulse — held at 5 (max), and '
                                      'confirmed rather than faded.',
                             'text': '5Y5Y forward inflation closed at 2.3597% on 31 Jul, the '
                                     'highest reading of the war and a fourth consecutive '
                                     'close above the 2.30% trigger that fired this channel '
                                     '4→5 on Friday. The upgrade taken last edition is not '
                                     'resting on a marginal pair of closes: the series has '
                                     'now printed 2.3302%, 2.3303%, 2.3597% and 2.3367% '
                                     'across four sessions, the last of them intraday. The '
                                     '10Y breakeven has moved with it, closing at 2.2846% on '
                                     '31 Jul, its highest since 3 July, and printing 2.2787% '
                                     'this morning — back above the 2.2569% pre-war anchor '
                                     'after touching it exactly a session earlier. That is a '
                                     'meaningful change from Friday’s reading, when spot '
                                     'compensation sat on its anchor while only the forward '
                                     'was elevated: now both are above pre-war, which narrows '
                                     'the case that this is purely a terminal-rate story and '
                                     'widens the case that near-term inflation compensation '
                                     'is rebuilding too. Note what is NOT doing the work. '
                                     'June core PCE, released 30 July, was +0.1% m/m against '
                                     'a +0.2% consensus. OPEC+ has just added barrels. Crude '
                                     'is $13.44 below the $95 trigger. Breakevens rose '
                                     'anyway, through a cool core print and a falling oil '
                                     'price, which is close to a controlled experiment in '
                                     'what markets think the Fed will tolerate. The downgrade '
                                     '— 5Y5Y sustained at or below the 2.142% anchor — is '
                                     '21.8 bp away on the last close and is not in play. At '
                                     '5/5 the channel can only subtract.'},
                            {'title': '(iii) Oil — held at 2, and this is the channel the '
                                      'weekend actually moved.',
                             'text': 'The last confirmed close is $87.93 (31 Jul), $7.07 '
                                     'below the $95 upgrade trigger and $1.05 above the '
                                     'Thursday close — Friday’s US session bought crude back, '
                                     '$1.97 above my morning print. Then the weekend '
                                     'happened. Brent front-month opens the week at $81.56, '
                                     'down $6.37, the largest single-session decline since 25 '
                                     'May and the lowest level since 10 July; WTI is $78.42, '
                                     'back under $80; the Brent–WTI spread has collapsed from '
                                     '$6.44 on Friday’s close to $3.14, which says the market '
                                     'is unwinding a Hormuz-specific premium rather than '
                                     'repricing global demand. Two causes, both dated 2 '
                                     'August: the cancelled strike package with talks '
                                     'announced for today, and OPEC+ approving a final +188k '
                                     'b/d for September that completes the unwind of the 1.65 '
                                     'mb/d voluntary tranche. The counter-argument is that '
                                     'neither cause changes a barrel of physical supply. '
                                     'Effective OPEC+ spare capacity was roughly 0.17 mb/d on '
                                     'the IEA’s July estimate, so September’s increment is a '
                                     'quota, not a cargo. Jizan’s 400k b/d is still out to '
                                     'mid-August. Abqaiq still shows unexplained burn scars. '
                                     'The strait is still closed on day ~157, still running '
                                     'at roughly a tenth of normal traffic, and an LNG '
                                     'carrier was still hit in it on 31 July. The channel '
                                     'stays at 2 because $87.93 is not $95; but the risk to '
                                     'that score is now genuinely two-sided for the first '
                                     'time since early July, and the downgrade leg — a '
                                     'mediated pause AND a close at or below $72.48 — has '
                                     'acquired a live first condition even though the price '
                                     'leg is $9.08 away.'},
                            {'title': '(iv) Political — held at 4, and it is now one print '
                                      'from firing.',
                             'text': 'AUTMUSAG backfilled 30 July at $4.76 — the first print '
                                     'ABOVE the $4.75 trigger and the highest since 10 June — '
                                     'after four consecutive sessions exactly on the line. '
                                     'Then the series went dark for 31 July and 3 August. The '
                                     'upgrade rule requires a sustained break, which this '
                                     'monitor has consistently read as two consecutive '
                                     'confirmed closes; there is one. The channel therefore '
                                     'holds at 4 with the upgrade armed rather than fired, '
                                     'which is exactly the position the US-inflation channel '
                                     'occupied on 30 July before it fired the next day. The '
                                     'corroborating evidence is genuinely mixed. AAA’s '
                                     'separately published regular-grade national average was '
                                     '$4.098 on 30 July against $4.091 a week earlier, '
                                     'seven-tenths of a cent, which reads as a stall. But '
                                     'on-highway diesel rose 17.9 cents in the week to 27 '
                                     'July against gasoline’s 9.5 cents, and on 1 August both '
                                     'Exxon and Chevron told the market that refining, not '
                                     'crude, is the binding constraint — roughly a tenth of '
                                     'global refining capacity is offline, Chevron’s chief '
                                     'executive called middle distillates ‘the real pain '
                                     'point’ and expects upward pressure on product prices '
                                     'into the third quarter. That is a mechanism by which '
                                     'the pump can keep rising even as Brent falls $6, and it '
                                     'is why a $6 fall in crude this morning should not be '
                                     'read as taking the political channel off its trigger. '
                                     'No federal intervention — SPR release, export limit, '
                                     'waiver or gouging action — is confirmable in the '
                                     'window.'}],
              'stage4Note': 'Stage 4 is a credit/auction event. Threshold B is now satisfied '
                            'on three consecutive confirmed closes and the dated supply test '
                            'arrives this week.',
              'stage4': [{'title': 'Threshold A · 13 May 30Y auction, cleared 5.050%.',
                          'text': 'Historical benchmark; the 9 July re-opening cleared 5.06% '
                                  'with a 0.3 bp stop-through. The 31 July close of 5.2724% '
                                  'is 22.24 bp above the May stop, the widest margin of the '
                                  'war, up from 16.35 bp a session earlier. The supply test '
                                  'is no longer prospective: Treasury publishes its quarterly '
                                  'marketable borrowing estimates on Monday 3 August (evening '
                                  'Singapore time, and not yet released at this snapshot) and '
                                  'the refunding statement on Wednesday 5 August at 8:30am '
                                  'ET, with the 30Y refunding leg auctioning in the week of '
                                  '10 August. The standing baseline is the 4 May projection '
                                  'of $671bn privately-held net marketable borrowing for '
                                  'July–September against a $950bn end-September cash '
                                  'balance, and the 6 May refunding held sizes at 3Y $58bn / '
                                  '10Y $42bn / 30Y $25bn with guidance to keep nominal coupon '
                                  'sizes unchanged ‘for at least the next several quarters.’ '
                                  'Any deviation from that guidance meets a long end that has '
                                  'just printed a war high.'},
                         {'title': 'Threshold B · 30Y above 5.20% with 10Y above 4.65% — '
                                   'SATISFIED on three consecutive confirmed closes.',
                          'text': '29 July: 5.2007% / 4.6773%. 30 July: 5.2135% / 4.6733%. 31 '
                                  'July: 5.2724% / 4.7347%, both war records. The persistence '
                                  'question raised last edition has been answered in the '
                                  'affirmative, and answered by the widest margin yet: '
                                  'Friday’s 30Y was 7.24 bp through its leg and the 10Y 8.47 '
                                  'bp through its own, against 1.35 bp and 0.33 bp on '
                                  'Thursday. This morning’s intraday prints of 5.2370% and '
                                  '4.6939% keep both legs satisfied on a fourth session. The '
                                  'qualification that belongs with it is unchanged: the '
                                  'threshold is a warning that the long end is repricing in a '
                                  'way that historically precedes an auction or credit event, '
                                  'not a Stage-4 event in itself. Stage 4 requires this to '
                                  'show up in a failed or heavily tailed auction, and the '
                                  'calendar now supplies the test within nine days. The '
                                  'mechanism arming it remains domestic monetary credibility, '
                                  'not a Hormuz headline — which is why the weekend’s '
                                  'de-escalation moved crude $6 and did not move the long end '
                                  'at all.'},
                         {'title': 'Threshold C · MOVE above 130. Far off, but moving the '
                                   'wrong way.',
                          'text': 'The index closed at 83.02 on 31 July, up 5.93 on the '
                                  'session and the highest since 19 May. That leaves 46.98 '
                                  'pts to the threshold and it remains well under the 115.02 '
                                  'war high of 26 March, so C is not close. Two things are '
                                  'worth recording anyway: rates volatility has now risen in '
                                  'three of the last four sessions and is 9.64 pts above its '
                                  'pre-war level, and at 83.02 it is 8.02 pts above the 75 '
                                  'line that forms the second leg of the Treasury downgrade, '
                                  'so the same reading that keeps C remote keeps that '
                                  'downgrade unavailable. There is no 3 August print; the '
                                  'number is flagged and not carried as fresh.'}],
              'crossAsset': 'The cross-asset signature has split in two, and the split is the '
                            'story of this edition. The bond market spent Friday doing '
                            'damage: the 30Y closed at a war-record 5.2724%, the 10Y at a '
                            'war-record 4.7347%, 5Y5Y at a war-record 2.3597%, the 10Y '
                            'breakeven at its highest since 3 July, MOVE up 5.93 to 83.02 and '
                            '2s10s steepening to +43.94 bp. The dollar did not rally on any '
                            'of it — DXY closed 99.914 and prints 99.592 this morning, the '
                            'lowest since 16 June and down 1.94 on the week. The energy '
                            'complex spent the weekend doing the opposite: Brent front-month '
                            'down $6.37 to $81.56, WTI back under $80, TTF at €56.30 and its '
                            'lowest since 16 July, Asia LNG turning lower to ¥3,440 on '
                            'Friday. Equity volatility went with energy rather than with '
                            'rates, VIX closing 15.99, its lowest since 15 July and nearly '
                            'four points below pre-war. Two markets, two views: equities and '
                            'crude are pricing a war that ends at a negotiating table in '
                            'Oman, while the long end is pricing a central bank that has lost '
                            'the inflation argument and a Treasury that has to fund itself on '
                            'Wednesday. Henry Hub at $2.766 remains 9.7% BELOW pre-war, so '
                            'the routing signature is intact and this is still not a '
                            'global-energy shock. If the talks that opened today hold, the '
                            'oil channel and the escalation channel can both fall. Nothing in '
                            'Oman fixes the 30-year.'},
 'channels': [{'name': 'Maritime denial',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 (max). Strait closed to commercial traffic, day ~157. '
                            'Kpler counted 10 commodity transits on 31 Jul against a pre-war '
                            'baseline above 100 a day; Windward, on an all-vessel basis, '
                            'logged 5 against roughly 140 pre-crisis and 66 GPS-jammed '
                            'vessels in the Gulf. Lloyd’s List has inbound Gulf traffic down '
                            'more than 90% and 70% of transits untraceable on AIS. An LNG '
                            'carrier laden with Qatari cargo was struck in transit on 31 Jul '
                            'and UKMTO logged an explosion beside a tanker off Khasab on 2 '
                            'Aug. Trump says a deal would deliver ‘immediate, complete and '
                            'total opening’; Iran says the negotiation is about a NEW '
                            'corridor with Oman and denies any deal.',
               'upgrade': 'at max.',
               'downgrade': 'verified reopening (escorted convoys) with traffic above 25% of '
                            'normal for 10 sessions → to 3–4. A signed corridor agreement '
                            'starts that clock; an announcement does not.'},
              {'name': 'Oil price shock',
               'score': 2,
               'state': 'live',
               'rationale': 'Held at 2. Last confirmed close $87.93 (31 Jul), $7.07 below the '
                            '$95 trigger; intraday $81.56, $13.44 below it and down $6.37 on '
                            'the day — the largest single-session fall since 25 May and the '
                            'lowest print since 10 Jul. Drivers are the cancelled US strike '
                            'package with talks announced for 3 Aug, and the OPEC+ decision '
                            'of 2 Aug to add a final 188k b/d for September. Physical supply '
                            'is unchanged: effective spare capacity ~0.17 mb/d, Jizan out to '
                            'mid-August, Abqaiq unexplained.',
               'upgrade': 'Brent above $95 sustained → to 3.',
               'downgrade': 'mediated pause + close at/below the $72.48 anchor → to 1. The '
                            'pause leg is live for the first time since early July; the price '
                            'leg is $9.08 away.'},
              {'name': 'US inflation impulse',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 (max), and confirmed. 5Y5Y closed 2.3597% on 31 Jul, '
                            'the highest of the war and a FOURTH consecutive close above the '
                            '2.30% trigger that fired this channel 4→5 last edition; 2.3367% '
                            'intraday. The 10Y breakeven closed 2.2846%, its highest since 3 '
                            'Jul, and is back above its 2.2569% pre-war anchor. Compensation '
                            'rose through a cool June core PCE, an OPEC+ supply increase and '
                            'a $6 fall in crude.',
               'upgrade': 'at max.',
               'downgrade': '5Y5Y sustained at/below the 2.142% pre-war anchor → to 4 (21.8 '
                            'bp away on the last close).'},
              {'name': 'Treasury stress',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 (max). The 30Y closed 5.2724% and the 10Y 4.7347% on '
                            '31 Jul, both war records; the 30Y is 22.24 bp above the 13 May '
                            'auction stop, the widest margin recorded, and MOVE rose 5.93 to '
                            '83.02, its highest since 19 May. Intraday 5.2370% / 4.6939% '
                            'keeps both Stage-4 legs satisfied on a fourth session. 2s10s at '
                            '+44.6 bp is the steepest since 26 May while the dollar sits at a '
                            'seven-week low.',
               'upgrade': 'at max.',
               'downgrade': '30Y close under 5.00% with MOVE under 75 sustained → to 4. Both '
                            'legs fail by 23.70 bp and 8.02 pts.'},
              {'name': 'Political stress',
               'score': 4,
               'state': 'live',
               'rationale': 'Held at 4 — but ARMED. AUTMUSAG backfilled 30 Jul at $4.76, the '
                            'first print above the $4.75 trigger and the highest since 10 '
                            'Jun, after four sessions exactly on the line; 31 Jul and 3 Aug '
                            'are blank, flagged and not carried. One close above a trigger is '
                            'not a sustained break. Diesel rose 17.9c in the week to 27 Jul '
                            'against gasoline’s 9.5c, and Exxon and Chevron said on 1 Aug '
                            'that refining, not crude, is the binding constraint — so a '
                            'falling Brent does not disarm this channel.',
               'upgrade': 'gasoline above $4.75 sustained (a second consecutive close) → to '
                          '5.',
               'downgrade': 'toward the $3.52 pre-war level → to 3.'},
              {'name': 'Escalation risk',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 (max), with a live downgrade candidate for the first '
                            'time since 9 Jul. Trump cancelled a strike package he called '
                            '‘the biggest attack since World War II’ and announced talks for '
                            '3 Aug with Oman mediating; no Tier 1 outlet reported a new '
                            'strike on Iran between 31 Jul and 3 Aug. Against that: Iran '
                            'denies any deal and calls the claim ‘a new lie’; a Qatari-laden '
                            'LNG carrier was struck on 31 Jul and UKMTO logged a blast near a '
                            'tanker on 2 Aug; Kuwait intercepted Iranian drones on 31 Jul; '
                            'the State Department told Americans to leave more than a dozen '
                            'countries; and the Iraqi militia deadline to Baghdad is still '
                            'pending.',
               'upgrade': 'at max.',
               'downgrade': 'mediated stand-down + talks resume → to 4–3. Requires the talks '
                            'to convene AND hold, with no new strikes, across a sustained '
                            'window — not an announcement.'}],
 'scoreTotal': 'CRISIS band — UNCHANGED, the highest reading since 12 June. No channel moved, '
               'but the composition of the risk did. The bond market set three war records on '
               'Friday and Stage-4 Threshold B is satisfied on a third consecutive close '
               'going into a refunding week; the geopolitical track produced a cancelled '
               'strike package and an announced negotiation. For the first time in the war '
               'the monitor is carrying a live downgrade candidate (escalation) and a live '
               'upgrade candidate (political) at the same time. Four of six channels remain '
               'maxed, so only oil (2/5) and political (4/5) can raise the number.',
 'whatsChanged': {'title': "4 · What's changed since the last edition (31 Jul AM → 3 Aug AM)",
                  'items': ['Score holds at 26/30. Three war records set on the 31 Jul close. '
                            'A US strike package cancelled and talks announced. OPEC+ adds '
                            'September barrels. Brent breaks $6 lower. Source: Bloomberg '
                            'unless stated.',
                            'Friday’s US session set three war records that the morning '
                            'snapshot had missed. The 31 Jul closes: 30Y 5.2724%, 10Y 4.7347% '
                            'and 5Y5Y forward inflation 2.3597% — each the highest of the war '
                            '— with the 10Y breakeven at 2.2846%, its highest since 3 July, '
                            '2s10s steepening to +43.94 bp and MOVE up 5.93 to 83.02, its '
                            'highest since 19 May. My Friday-morning prints were 7.59 bp, '
                            '8.16 bp and 3.68 bp below the eventual closes respectively. This '
                            'is the single largest reconciliation gap in the long end the '
                            'monitor has recorded. Source: Bloomberg.',
                            'Stage-4 Threshold B is satisfied on a third consecutive '
                            'confirmed close, by the widest margin yet. The 31 July close '
                            'cleared the 5.20% leg by 7.24 bp and the 4.65% leg by 8.47 bp, '
                            'against 1.35 bp and 0.33 bp on 30 July. This morning’s intraday '
                            '5.2370% / 4.6939% keeps both satisfied on a fourth session. The '
                            '30Y is now 22.24 bp above the 13 May auction stop, the widest of '
                            'the war, and the dated supply test arrives this week. Source: '
                            'Bloomberg.',
                            'Trump cancelled a planned strike package and announced talks '
                            'beginning today, with Oman mediating. On 2 August the President '
                            'said he had called off what would have been ‘the biggest attack '
                            'since World War II’ and announced a new round of negotiations '
                            'for Monday 3 August involving Saudi Arabia, the UAE and Qatar, '
                            'with no deadline set. On 1 August he had said the ‘perimeters of '
                            'a deal’ included ‘immediate, complete and total opening of the '
                            'Hormuz Strait’ and an end to Iran’s nuclear threat. Saudi Crown '
                            'Prince Mohammed bin Salman phoned him urging de-escalation. No '
                            'Tier 1 outlet reported a new CENTCOM or Israeli strike on Iran '
                            'between 31 July and 3 August. Source: Al Jazeera / Bloomberg / '
                            'France 24 / ABC News / CNN.',
                            'Iran rejected the framing and described a different negotiation '
                            'entirely. Tehran denied asking for the pause and denied any '
                            'Hormuz agreement, calling it ‘a new lie.’ Araghchi said talks '
                            'with OMAN are ‘on the way to being finalised’ and spokesman '
                            'Baghaei said the two sides expect to agree a NEW route, neither '
                            'the existing northern nor the southern corridor. President '
                            'Pezeshkian on 3 August urged Washington to remain committed to '
                            'the June MoU. The gap between ‘immediate, complete and total '
                            'opening’ and ‘a new corridor co-managed with Oman’ is the whole '
                            'negotiation. Source: Al Jazeera / ABC News / Times of Israel.',
                            'OPEC+ approved a final +188k b/d for September and left the '
                            'fourth-quarter pause out of the communiqué. Eight producers '
                            'agreed on 2 August, completing the rollback of the 1.65 mb/d '
                            'voluntary tranche. Sources briefed Reuters before the meeting '
                            'that a Q4 pause would follow, but no such language appeared in '
                            'the statement. Next meetings 6 September and 4 October. The '
                            'IEA’s July estimate put effective OPEC+ spare capacity at '
                            'roughly 0.17 mb/d, so the increment is a quota rather than an '
                            'incremental cargo. Source: CNBC / Reuters / Al Arabiya / IEA.',
                            'Brent broke $6 lower — the largest single-session decline since '
                            '25 May. Front-month prints $81.56 this morning against the '
                            '$87.93 close, the lowest since 10 July; WTI $78.42; the '
                            'Brent–WTI spread has halved to $3.14, which is a Hormuz premium '
                            'unwinding rather than a demand repricing. TTF fell to €56.30, '
                            'its lowest since 16 July. The energy complex is trading the '
                            'diplomacy; the long end did not move on it at all. Source: '
                            'Bloomberg.',
                            'The waterway stayed hostile through the diplomacy. The LNG '
                            'carrier Gaslog Shanghai, laden with Qatari cargo, was struck by '
                            'a projectile while transiting near the western entrance off Oman '
                            'on 31 July; UKMTO logged an explosion beside a tanker 20 nm '
                            'north-east of Khasab on 2 August; Kuwait intercepted hostile '
                            'drones on 31 July with Iran claiming it had targeted Ahmad '
                            'al-Jaber Air Base; and the State Department urged Americans to '
                            'leave more than a dozen Middle East countries on 1 August. Kpler '
                            'counted 10 commodity transits on 31 July. Source: Bloomberg / '
                            'UKMTO / Al Jazeera / CNN / Kpler via The National.',
                            'AUTMUSAG backfilled 30 July at $4.76 — the first print through '
                            'the political trigger. After four consecutive sessions exactly '
                            'on $4.75, the scored series printed $4.76, its highest since 10 '
                            'June. The series is then blank for 31 July and 3 August, flagged '
                            'and not carried. One close above a trigger arms the upgrade; it '
                            'does not fire it. The channel is now in the position US '
                            'inflation occupied on 30 July. Source: Bloomberg.',
                            'The pump constraint is refining, not crude — which is why a $6 '
                            'fall in Brent may not disarm the political channel. On 1 August '
                            'Exxon and Chevron both told the market that refining capacity is '
                            'the binding constraint, with roughly a tenth of global capacity '
                            'offline; Chevron’s chief executive called middle distillates '
                            '‘the real pain point’ and expects upward product pressure into '
                            'the third quarter. EIA has on-highway diesel up 17.9 cents in '
                            'the week to 27 July against gasoline’s 9.5 cents, with refinery '
                            'utilisation at 97.2% and gasoline stocks 7% below the five-year '
                            'average. Source: Fortune / EIA.',
                            'Correction: the Iraqi militia deadline is sourced as 7 August, '
                            'not 6 August, and only at Tier 3. The 31 July edition carried a '
                            '6 August deadline from Kataib Hezbollah to the Iraqi government. '
                            'On re-verification the only sourcing available is Press TV, '
                            'Middle East Monitor and Shafaq News reporting the ‘Iraqi Islamic '
                            'Resistance’ setting a 7 August deadline for Baghdad to respond '
                            'to the US–Saudi strikes of 29 July. No Tier 1 outlet '
                            'corroborates either the date or the attribution to Kataib '
                            'Hezbollah specifically, and no new attacks on US positions in '
                            'Iraq were reported in the window. The item is retained as a '
                            'dated risk but demoted to Tier 3. Source: Press TV / Middle East '
                            'Monitor / Shafaq News (all Tier 3).']},
 'scenarios': [{'name': 'Return to full war',
                'p': 34,
                'desc': 'Lower, and the first fall in this line since 27 Jul. A strike '
                        'package described by the President himself as the largest since the '
                        'Second World War was cancelled rather than launched, and no Tier 1 '
                        'outlet reported a new strike on Iran across four days. The path '
                        'stays modal-adjacent because nothing was signed, US and Israeli '
                        'planning for a campaign against Iranian civilian energy '
                        'infrastructure was reported on 1 Aug as awaiting authorisation, and '
                        'the Iraqi militia deadline is still pending.',
                'path': 'Brent $105–140; MOVE above 90; oil to 3–4, political to 5; score '
                        '28–30.'},
               {'name': 'Deal collapse — talks stall on terms',
                'p': 27,
                'desc': 'Higher, and now the modal path. There are finally talks to collapse. '
                        'The two sides have stated incompatible objectives in public: '
                        'Washington describes ‘immediate, complete and total opening’ of the '
                        'strait, Tehran describes a new co-managed corridor with Oman and '
                        'denies any deal exists. No deadline has been set and the IMO has no '
                        'standing over either routeing plan.',
                'path': 'Brent $92–108; oil to 3; 30Y sustained above 5.20% with the 10Y '
                        'above 4.65%, i.e. Stage-4 B persisting; score 27–28.'},
               {'name': 'Contained but violent — blockaded stalemate',
                'p': 15,
                'desc': 'Higher. The strait stays shut and dangerous — an LNG carrier hit on '
                        '31 Jul, a blast beside a tanker on 2 Aug — while the strike tempo '
                        'falls and the parties talk past each other. This is the path where '
                        'the score sits at 26 for weeks because both event channels are '
                        'pinned at 5 and neither market channel is triggered.',
                'path': 'Brent $78–92; MOVE 78–88; risk premium $6–18/bbl; score holds 26.'},
               {'name': 'Mediated pause — the ceasefire sticks',
                'p': 12,
                'desc': 'Higher, and materially so: this is the largest single shift in the '
                        'map since the June MoU. A cancelled strike package, a Saudi royal '
                        'intervention, Pakistani and Qatari intermediaries, and Iran–Oman '
                        'corridor talks described by Araghchi as near-final are the most '
                        'substantive de-escalation inputs since early July. It stays a '
                        'minority path because Iran denies the American account of it.',
                'path': 'Brent $72–84; MOVE under 75; escalation→4 then 3, maritime→3–4 on '
                        'verified traffic; score falls toward 20–22.'},
               {'name': 'Regional relapse — Gulf energy infrastructure hit',
                'p': 12,
                'desc': 'Lower. The immediate strike wave was called off and the Red Sea and '
                        'Bab al-Mandeb were described as relatively calm on 2 Aug. The '
                        'underlying exposure is unchanged: Jizan out to mid-August, Abqaiq '
                        'burn scars on four of six spheroids with no Aramco comment, Damietta '
                        'status unreported, effective spare capacity ~0.17 mb/d.',
                'path': 'Brent $150+; emergency policy response; HY spreads above 500 bp; '
                        'score 29–30.'}],
 'scenarioShift': 'Probability shifts from the 31 Jul edition: full war −7 (41→34) on the '
                  'cancelled strike package and four days without a Tier 1-confirmed strike; '
                  'mediated pause +5 (7→12), the largest single shift since the June MoU, on '
                  'the announced talks, the Saudi intervention and Araghchi’s ‘near-final’ '
                  'Oman corridor negotiation; deal collapse +3 (24→27), which now becomes the '
                  'modal path because a negotiation must exist before it can fail and the two '
                  'sides have stated incompatible objectives; contained-but-violent +2 '
                  '(13→15) as the strike tempo falls while the strait stays shut and '
                  'dangerous; regional relapse −3 (15→12) on the called-off wave and a calm '
                  'Red Sea, with the underlying infrastructure exposure unchanged. '
                  'Probabilities sum to 100.',
 'watchlist': ['Do the talks convene, and do they hold? This is the escalation channel’s '
               'first live downgrade since 9 July. The downgrade requires a mediated '
               'stand-down AND talks resuming, sustained. An announcement is not a '
               'stand-down. The specific things to verify: that a session actually took place '
               'on 3 August; that Oman confirms it as mediator; that Iran stops calling the '
               'American account ‘a new lie’; and that no new strike is reported. If those '
               'hold for several sessions the channel moves 5→4, which would be the first '
               'downgrade of any channel since the oil move of 3 July and would take the '
               'score to 25.',
               'Treasury’s borrowing estimates tonight and the refunding statement on '
               'Wednesday, into a war-high long end. The 31 July 30Y close of 5.2724% is '
               '22.24 bp above the 13 May auction stop. Treasury’s quarterly marketable '
               'borrowing estimates are due 3 August US time and the refunding statement on 5 '
               'August at 8:30am ET, against the 4 May baseline of $671bn for July–September '
               'and the 6 May guidance to hold coupon sizes at 3Y $58bn / 10Y $42bn / 30Y '
               '$25bn. An increase, or any softening of that guidance, meets a market that '
               'has just repriced 10 bp in a week. The 30Y refunding leg auctions in the week '
               'of 10 August.',
               'AUTMUSAG’s next print — one more close above $4.75 fires political to 5 and '
               'the score to 27. The scored series printed $4.76 on 30 July, its first '
               'reading through the trigger, then went blank for two sessions. A second '
               'consecutive confirmed close above $4.75 is the sustained break the rule '
               'requires. Note that Brent falling $6 does not settle this: the pass-through '
               'constraint is refining capacity, diesel is running ahead of gasoline, and the '
               'DOE weekly print due 3 August will corroborate or contradict.',
               'Whether crude’s $6 break holds, or reverses the way the 29 July bounce did. '
               'Brent fell $3.79 on 28 July and rallied $6.01 the next day. The market has '
               'been trading each headline in full and reversing it within 48 hours. The '
               'upgrade trigger is $95, $13.44 above this morning’s print; the downgrade '
               'needs $72.48, $9.08 below it. Neither is close, but the distance to the '
               'downgrade is now the shortest of the war and its first condition — a mediated '
               'pause — has stopped being hypothetical.',
               'The dated calendar: payrolls 7 August, CPI 12 August, the 30Y auction the '
               'week of 10 August, and the Iraqi militia deadline. July payrolls land on 7 '
               'August and July CPI on 12 August, both before the 15–16 September FOMC where '
               'CME FedWatch had roughly 61% odds on a HIKE as of 29 July. The Iraqi deadline '
               'to Baghdad over the 29 July US–Saudi strikes is reported as 7 August, but '
               'only by Press TV, Middle East Monitor and Shafaq News; no Tier 1 outlet '
               'corroborates it and the 31 July edition’s 6 August date is corrected here.',
               'Two data series to re-verify fresh, and one to watch for a second week of '
               'blackout. JGLA (Asia LNG) has no 3 August print and closed lower at ¥3,440 on '
               'Friday, its first decline in three sessions; it is never carried forward. '
               'AUTMUSAG is blank for two sessions. SOFR is now blank for two sessions as '
               'well, having last printed 3.65 on 30 July — a new gap, and the third series '
               'in this extract running dark at once.'],
 'sourceLog': {'tier1Market': 'Bloomberg Terminal extract (US Iran BBG Data.xlsx, 152 data '
                              'rows × 99 columns, restated front-month continuation series). '
                              'Tickers: CO2/CL2 Comdty (front-month; last confirmed close '
                              '$87.93 / $81.49 on 31 Jul, intraday $81.56 / $78.42 with a '
                              'Brent high of 82.05 and low of 79.83); COA/CLA Comdty (active, '
                              'unscored — $84.12 / $80.77, the September Brent contract '
                              'having expired on 31 Jul); NGA ($2.766), TZTA (€56.300) and '
                              'JGLA (¥3,440 on the 31 Jul close, down ¥87; no 3 Aug print, '
                              'flagged not carried); USGG2YR/5YR/10YR/20YR/30YR (30Y closed '
                              '5.2724% and 10Y 4.7347% on 31 Jul, both war records; 5.2370% / '
                              '4.6939% intraday); USYC2Y10 (+44.621, steepest since 26 May); '
                              'USGGBE10 (2.2846 close, highest since 3 Jul; 2.2787 intraday); '
                              'USGG5Y5Y (2.3597 close, war record and a fourth consecutive '
                              'close above the 2.30% trigger; 2.3367 intraday); SOFRRATE '
                              '(blank 31 Jul and 3 Aug; last print 3.65 on 30 Jul, flagged '
                              'not carried); MOVE (83.02 on the 31 Jul close, +5.93 and the '
                              'highest since 19 May; no 3 Aug print) and VIX (15.99, lowest '
                              'since 15 Jul; no 3 Aug print); DXY (99.914 close, 99.592 '
                              'intraday, lowest since 16 Jun); AUTMUSAG (AAA all-grades pump '
                              '— score reference; $4.76 on 30 Jul, the first print above the '
                              '$4.75 trigger and the highest since 10 Jun, with 31 Jul and 3 '
                              'Aug blank) and USRFRUSA (DOE regular spot, weekly — '
                              'corroboration; $4.096 for the week of 27 Jul, the 3 Aug print '
                              'not yet in the extract). Data-integrity note: the stale-row '
                              'check clears. The 31 Jul row has refreshed and differs '
                              'materially from the intraday values published for it (Brent '
                              '$87.93 against $85.96; 30Y 5.2724% against 5.1965%; MOVE 83.02 '
                              'against a carried 77.09), so it is a true close and every '
                              'trigger test in this edition runs off it. Three series are '
                              'dark: JGLA, AUTMUSAG and now SOFR. The 27 Feb 2026 anchor was '
                              're-verified field by field and is unchanged.',
               'tier1News': 'Al Jazeera, Bloomberg, France 24, ABC News and CNN (Trump’s 2 '
                            'Aug statement that he cancelled ‘the biggest attack since World '
                            'War II’ and announced talks for 3 Aug with Oman mediating and no '
                            'deadline set; his 1 Aug ‘perimeters of a deal’ including '
                            '‘immediate, complete and total opening of the Hormuz Strait’; '
                            'the Saudi Crown Prince’s call urging de-escalation; the State '
                            'Department advisory to leave more than a dozen Middle East '
                            'countries); Al Jazeera and ABC News (Araghchi’s ‘on the way to '
                            'being finalised’ Oman talks, spokesman Baghaei on a NEW route '
                            'acceptable to both sides, Tehran’s denial of any deal as ‘a new '
                            'lie’, and President Pezeshkian’s 3 Aug call for Washington to '
                            'honour the June MoU); Bloomberg via Yahoo Finance and UKMTO (the '
                            'LNG carrier Gaslog Shanghai struck in transit off Oman on 31 '
                            'Jul; the 2 Aug explosion reported 20 nm north-east of Khasab); '
                            'Kuwait’s defence ministry via Al Jazeera and CBS News (drones '
                            'intercepted over Kuwait on 31 Jul); Kpler via The National (10 '
                            'commodity transits on 31 Jul, 4 on 30 Jul, 15 on 29 Jul; Bab '
                            'al-Mandeb 31 on 31 Jul), Windward (5 all-vessel transits and 66 '
                            'GPS-jammed vessels on 31 Jul) and Lloyd’s List Intelligence (39 '
                            'transits in the week to 26 Jul against 82 the week before, 70% '
                            'of traffic untraceable on AIS, inbound Gulf traffic down more '
                            'than 90%, war-risk cover 7.5–10% of hull value); CNBC, Reuters '
                            'and Al Arabiya (the 2 Aug OPEC+ decision to add 188k b/d for '
                            'September, completing the 1.65 mb/d rollback, with no Q4 pause '
                            'in the communiqué and next meetings on 6 Sep and 4 Oct); IEA Oil '
                            'Market Report of 10 July (effective OPEC+ spare capacity ~0.17 '
                            'mb/d) and the 19 March collective-action confirmation (426 mb of '
                            'contributions, US share 172.2 mb); EIA Weekly Petroleum Status '
                            'Report of 29 July for the week to 24 July (crude 404.5 mb and '
                            '~6% below the five-year average, gasoline 211.3 mb and 7% below, '
                            'distillate ~10% below, refinery utilisation 97.2%, SPR 307.7 mb '
                            'after a 3.7 mb draw) with the next release due 5 August; EIA '
                            'Gasoline and Diesel Fuel Update (regular $4.096 and on-highway '
                            'diesel $5.313 for the week to 27 July, +9.5c and +17.9c); AAA '
                            '(national regular average $4.098 on 30 July against $4.091 a '
                            'week earlier); Fortune reporting Exxon and Chevron on 1 August '
                            '(refining the binding constraint, roughly a tenth of global '
                            'capacity offline, middle distillates ‘the real pain point’); US '
                            'Treasury (the 4 May borrowing projection of $671bn for '
                            'July–September, the 6 May refunding at 3Y $58bn / 10Y $42bn / '
                            '30Y $25bn with unchanged-size guidance, and the 3 and 5 August '
                            'calendar); Federal Reserve (the 29 July hold at 3.50–3.75%, 9–3 '
                            'with three dissents for a hike) with CME FedWatch (~61% odds on '
                            'a September hike as of 29 July); Maritime Executive and Reuters '
                            'via Industrial Info (Jizan offline to mid-August, Abqaiq '
                            'spheroid imagery); CNBC and Al Jazeera (the 29–30 July Damietta '
                            'strike, operational status since unreported); AP-NORC (64% say '
                            'the war has not been worth fighting, fielded 23–27 July).',
               'tier3': 'The IRGC claim of 31 July to have ‘struck and stopped’ two '
                        'US-escorted tankers in the strait, with four more vessels reversing '
                        'course, originates with IRNA and Tasnim and has no Tier 1 '
                        'corroboration; it is recorded and not used. Fars reported ships '
                        'stuck in the northern corridor on 2 August; Al Jazeera carried it as '
                        'a Tier 3 attribution. Iranian state media reported the return to '
                        'Iran of the bodies of five IRGC members killed in the 29 July '
                        'US–Saudi strikes in Iraq. Correction carried forward: the 31 July '
                        'edition reported a 6 August Kataib Hezbollah deadline to the Iraqi '
                        'government; on re-verification the only available sourcing is Press '
                        'TV, Middle East Monitor and Shafaq News describing the ‘Iraqi '
                        'Islamic Resistance’ setting a 7 August deadline, with no Tier 1 '
                        'corroboration of the date or of the attribution to Kataib Hezbollah '
                        'specifically. The claim attributed in the 31 July edition to '
                        'Gharibabadi — that the strait ‘will never return to its pre-war '
                        'state’ — could not be corroborated by a Tier 1 outlet on '
                        're-verification, and the same line is separately attributed to '
                        'Speaker Ghalibaf by other regional outlets; the substance is '
                        'consistent with Tehran’s stated position but the attribution is '
                        'contested and it is not relied on in this edition. Al Jazeera’s 1 '
                        'August report that US and Israeli officials were planning a roughly '
                        'two-week campaign against Iranian civilian energy infrastructure, '
                        'awaiting presidential authorisation, is a single-outlet report of '
                        'unnamed officials and is treated as such.'},
 'protocol': [{'step': 'Refresh the Bloomberg extract',
               'detail': 'Parse the latest dated row (3 Aug, Monday) as intraday; re-map '
                         'columns via the robust scan (front-month CO2/CL2; note the DXY '
                         'ticker now resolves as DXY Index in this extract). The stale-row '
                         'integrity check CLEARS: the 31 Jul row has refreshed with true '
                         'closes and differs materially from the intraday values published '
                         'for it, so 31 Jul is a confirmed close. Three series are dark and '
                         'are flagged, not carried: JGLA (no 3 Aug print; ¥3,440 on 31 Jul), '
                         'AUTMUSAG (blank 31 Jul and 3 Aug; $4.76 on 30 Jul) and SOFR (blank '
                         '31 Jul and 3 Aug; 3.65 on 30 Jul). MOVE and VIX printed for 31 Jul '
                         'but not for 3 Aug.'},
              {'step': 'Recompute deltas',
               'detail': 'd/d vs the 31 Jul close; w/w vs the close five trading sessions '
                         'back (27 Jul this edition); vs-pre-war against the 27 Feb 2026 '
                         'anchor, re-verified field by field and unchanged.'},
              {'step': 'Re-evaluate the six channels',
               'detail': 'Market channels move on confirmed closes only. No channel moved; '
                         'score holds at 26/30. Oil held at 2 (last close $87.93, $7.07 below '
                         '$95). US inflation held at 5 (5Y5Y closed 2.3597%, a war record and '
                         'a fourth consecutive close above 2.30%). Treasury held at 5 (30Y '
                         '5.2724% and 10Y 4.7347%, both war records; MOVE 83.02). Political '
                         'held at 4 and ARMED (AAA $4.76 on 30 Jul, one close above the '
                         'trigger, then two blanks). Maritime and escalation are event-based '
                         'and both maxed; the escalation downgrade is live for the first time '
                         'since 9 Jul and is deferred pending evidence that the announced '
                         'talks convene and hold.'},
              {'step': 'Reconcile against the prior edition',
               'detail': 'Friday’s US session ran well ahead of the Singapore-morning '
                         'snapshot in BOTH directions of the tape. My 31 Jul intraday Brent '
                         '$85.96 versus the $87.93 close (+$1.97); WTI $79.88 vs $81.49 '
                         '(+$1.61); 30Y 5.1965% vs 5.2724% (+7.59 bp); 10Y 4.6531% vs 4.7347% '
                         '(+8.16 bp); 2Y 4.2354% vs 4.2912% (+5.58 bp); 2s10s +41.57 vs '
                         '+43.94 bp; BE10 2.2566% vs 2.2846% (+2.80 bp); 5Y5Y 2.3229% vs '
                         '2.3597% (+3.68 bp); DXY 100.163 vs 99.914 (−0.249); MOVE a carried '
                         '77.09 vs an actual 83.02 (+5.93); VIX 17.09 vs 15.99. The long-end '
                         'gaps are the largest the monitor has recorded.'},
              {'step': 'Update scenarios and watchlist',
               'detail': 'Re-rank catalysts: whether the announced talks convene and hold '
                         'replaces Threshold B persistence as the nearest live channel move; '
                         'Treasury’s borrowing estimates (3 Aug) and refunding statement (5 '
                         'Aug) are the dated supply test, with the 30Y leg in the week of 10 '
                         'Aug; AUTMUSAG’s next print decides political; payrolls 7 Aug and '
                         'CPI 12 Aug precede the 15–16 Sep FOMC. Full war 41→34, deal '
                         'collapse 24→27 and now modal, mediated pause 7→12, '
                         'contained-but-violent 13→15, regional relapse 15→12.'}],
 'methodology': {'scale': 'Six transmission channels (maritime denial, oil, US inflation '
                          'impulse, Treasury stress, political stress, escalation risk), each '
                          '0–5, summed to 0–30. Bands: 0–7 watch · 8–14 stress · 15–21 '
                          'systemic-risk watch · 22–30 crisis. Market channels move only on a '
                          'confirmed close through a trigger; escalation-risk and maritime '
                          'denial are event-based. Hysteresis: upgrades fire on a sustained '
                          'break, downgrades only on a sustained reversal past a wider '
                          'threshold, deliberately, to avoid whipsawing. This edition applies '
                          'that rule twice and in both directions, which is unusual. '
                          'Political stress printed $4.76 on 30 July, its first reading above '
                          'the $4.75 trigger, and holds at 4 because one close is not a '
                          'sustained break — the identical position the US-inflation channel '
                          'occupied on 30 July before firing on 31 July. Escalation risk '
                          'holds at 5 despite a cancelled US strike package and an announced '
                          'negotiation, because an announcement is not a stand-down, the '
                          'principals publicly disagree about what was agreed, and an LNG '
                          'carrier was struck in the strait on 31 July. The precedent that '
                          'governs is 25–26 June, when an oil downgrade was taken on one '
                          'session’s evidence and had to be reversed the next day.',
                 'scaleCap': 'Maritime and escalation have been pinned at 5/5 since 10 and 9 '
                             'July, and US inflation and Treasury joined them at the ceiling '
                             'on 31 July and 14 July. Four of six channels are maxed, so only '
                             'oil (2/5) and political stress (4/5) can raise the number — '
                             'four points of range in a 30-point scale. The novelty this '
                             'edition is that the cap now also hides improvement: a genuine '
                             'de-escalation began over the weekend and the score could not '
                             'fall either, because the escalation channel needs a sustained '
                             'stand-down before it can move off its maximum. Readers should '
                             'treat a flat number from here as evidence that the scale is '
                             'saturated in both directions, not as evidence that nothing '
                             'changed.',
                 'integrity': 'The stale-row check clears. The extract’s 31 July row '
                              'refreshed properly and its closes differ materially from the '
                              'intraday values published for it (Brent $87.93 against $85.96, '
                              '30Y 5.2724% against 5.1965%, 5Y5Y 2.3597% against 2.3229%), so '
                              '31 July is a confirmed close and every trigger test runs off '
                              'it. Three series are currently dark and each is flagged rather '
                              'than carried: JGLA has no 3 August print, AUTMUSAG is blank '
                              'for 31 July and 3 August, and SOFR is blank for the same two '
                              'sessions — a new gap. MOVE and VIX printed for 31 July but not '
                              'for 3 August, so their readings are labelled as Friday closes '
                              'throughout. The DXY series resolves under a different ticker '
                              'suffix in this extract than in earlier ones and was re-mapped '
                              'by the column scan rather than hardcoded. Where third-party '
                              'sources disagree materially — Hormuz transit counts on '
                              'different vessel universes, the Iraqi militia deadline date, '
                              'the attribution of Iran’s ‘never return to its pre-war state’ '
                              'line — the disagreement is reported rather than resolved by '
                              'preference, and the Bloomberg extract governs for every scored '
                              'series.',
                 'gasoline': 'Political stress is scored on AUTMUSAG (AAA all-grades retail '
                             'pump; pre-war $3.52, peak $5.18, latest confirmed print $4.76 '
                             'on 30 July — the first print above the $4.75 trigger and the '
                             'highest since 10 June — with 24, 27, 28 and 29 July all '
                             'printing exactly $4.75 and 31 July and 3 August blank). '
                             'USRFRUSA (DOE regular spot; pre-war ~$2.94, peak $4.50, latest '
                             '$4.096 for the week of 27 July) is tracked alongside as '
                             'corroboration only; its next weekly print is due 3 August US '
                             'time and is not yet in the extract. Neither series is re-based. '
                             'AAA’s separately published regular-grade national average '
                             '($4.091 a week earlier, $4.098 on 30 July) is used only as an '
                             'external cross-read; EIA’s on-highway diesel series, up 17.9 '
                             'cents in the week to 27 July, is noted because the binding '
                             'constraint on the pump is refining capacity rather than crude.',
                 'anchor': 'Brent $72.48; WTI $67.02; 2Y 3.375%; 5Y 3.502%; 10Y 3.938%; 30Y '
                           '4.611%; 2s10s +55.64 bp; 5Y5Y 2.142%; 10Y BE 2.257%; MOVE 73.38; '
                           'VIX 19.86; DXY 97.608; gasoline (AAA) $3.52; Henry Hub $3.06; TTF '
                           '€31.23; Asia LNG ¥1,669. (Re-verified field by field — '
                           'unchanged.) Brent +12.5%, WTI +17.0%, TTF +80.3%, Asia LNG '
                           '+106.1%; the 30Y (+62.6 bp), 10Y (+75.6 bp), 5Y5Y (+19.5 bp), 10Y '
                           'breakeven (+2.2 bp), MOVE (+9.64) and DXY (+1.98) sit above their '
                           'anchors; VIX (−3.87) and Henry Hub (−9.7%) remain below pre-war.',
                 'intraday': 'The latest dated row is a Singapore-AM snapshot and US hours '
                             'set the close. Friday is the clearest illustration the monitor '
                             'has recorded: the eventual close was $1.97 above my Brent print '
                             'and 7.59 bp above my 30Y print, with MOVE 5.93 higher than the '
                             'value carried. The usual pattern is that the energy print leads '
                             'and the long end lags; on Friday both ran the same way and both '
                             'ran hard. Recent Brent gaps between my snapshot and the '
                             'subsequent close: +$0.60, +$3.10, −$1.81, −$2.01, −$3.32, '
                             '−$0.84, +$1.97. CL2 remains an artifact against active CLA, and '
                             'with the September Brent contract expired the '
                             'front-month/active gap has widened to $2.56 in this morning’s '
                             'snapshot; the scored CO2 continuation series is unaffected. '
                             'Triggers are evaluated on confirmed closes; escalation-risk and '
                             'maritime denial are event-based. Restated-series levels are not '
                             'comparable with pre-restatement editions, though the '
                             'directional analysis is continuous.'}}

# ======================================================================
# 2026-08-04 (latest)
# ======================================================================
EDITIONS['2026-08-04'] = {'label': '4 Aug 2026',
 'editionLine': 'Daily edition · 4 Aug 2026 intraday · Bloomberg · Singapore 4 Aug AM update',
 'score': '27',
 'band': 'CRISIS',
 'sequencing': '26 → 26 → 27',
 'sessionNote': 'Political stress fires 4→5 on the two-close rule · the announced 3 Aug talks '
                'did not convene · Treasury raises Q3 borrowing by $68bn',
 'headline': 'Note: 4 Aug figures are intraday prints; the last confirmed close is Monday 3 '
             'Aug. The integrity check clears — the 3 Aug row has refreshed with true closes, '
             'and four series that were dark in the last edition have backfilled. Score RISES '
             'to 27/30 — political stress fires 4→5 on the two-close rule, the highest '
             'reading since 31 May and the first upgrade since 31 July. The trigger fired on '
             'a backfill rather than on a new print: AUTMUSAG, the scored AAA pump series, '
             'was blank for 31 July when the last edition went out, and the extract has now '
             'filled it at $4.76 — a second consecutive confirmed close above the $4.75 '
             'threshold after the $4.76 of 30 July. That is the sustained break the rule '
             'requires, and it is the same mechanism that fired US inflation on 31 July. The '
             "second development runs the other way and cancels yesterday's optimism. The "
             "talks announced for 3 August did not convene. Iran's foreign ministry spokesman "
             "Esmaeil Baghaei said flatly on Monday that 'we are not negotiating with the "
             "United States at this time'; US officials told CBS News that no new "
             'negotiations are planned, contradicting the President, who said the same day '
             "that talks were under way 'at the request of Iran' and called it Iran's 'last "
             "chance' before what he termed decapitation. No venue, no attendee list, no "
             'readout and no Omani confirmation could be sourced from any outlet. The '
             'escalation downgrade candidate that this monitor carried for one edition is '
             'therefore revoked, not merely deferred — which is precisely why hysteresis '
             'governs event channels as well as market channels. Baghaei also said the strait '
             "'will in no way return to the status it was before February 28th', a line this "
             'monitor could not corroborate last week under a different attribution and can '
             'now source at Tier 1. Third, the dated supply test landed and it landed hard: '
             'Treasury raised its July–September net marketable borrowing estimate to $739bn '
             'from the $671bn projected on 4 May, an increase of $68bn, with the refunding '
             'statement due Wednesday and the 30Y leg the week of 10 August, into a long end '
             '17.74 bp above the May auction stop. Crude did not follow the diplomacy back '
             'up: Brent front-month prints $81.92, up $0.83 but still $0.16 below last '
             'Tuesday. Five of six channels are now maxed. Only oil, at 2/5, can raise this '
             'number further. Sequencing 26 → 26 → 27.',
 'tape': {'note': '4 Aug 2026 readings are intraday prints from the Singapore morning. The 3 '
                  'Aug row has refreshed and is a confirmed close; the integrity check '
                  'clears. d/d is 4 Aug intraday vs the 3 Aug close; w/w is vs the 28 Jul '
                  'close (five sheet-rows back); vs-pre-war is against the 27 Feb 2026 close. '
                  'Restated continuation series (front-month CO2/CL2) in force. With the '
                  'September Brent contract expired, the active COA references a new contract '
                  'and the front-month/active gap remains wide; the scored CO2 continuation '
                  'series is unaffected.',
          'oilGasHeader': ['Benchmark',
                           'Intraday 4 Aug',
                           '∆ d/d',
                           '∆ vs pre-war close (27 Feb)',
                           'BBG ticker'],
          'oilGas': [['Brent front-month',
                      '$81.92 /bbl (H 82.00 / L 81.26)',
                      '+$0.83 (–$0.16 w/w)',
                      'from $72.48 (+13.0%) — a $9.44/bbl premium. A very narrow intraday '
                      'range of 74 cents against Monday’s $2.24 and Friday’s $6.74: the '
                      'market stopped trading headlines the moment the announced talks failed '
                      'to produce one. Active COA prints $84.63',
                      'CO2 Comdty (Close)'],
                     ['Brent · 3 Aug close (last confirmed)',
                      '$81.09 /bbl',
                      '–$6.84 vs the 31 Jul close $87.93',
                      '$13.91 below the $95 trigger on a close basis; $8.61 above the $72.48 '
                      'downgrade anchor, the narrowest gap of the war since 10 Jul. The '
                      'largest single-session decline since 25 May, and the lowest close '
                      'since 10 Jul. Monday’s close ran $0.47 BELOW my Monday-morning '
                      'snapshot — a small gap, and the opposite of Friday’s record.',
                      'CO2 Comdty (Close)'],
                     ['WTI front-month',
                      '$78.66 /bbl',
                      '+$0.76 (+$1.49 w/w)',
                      'from $67.02 (+17.4%) — the CL2 artifact against the active contract '
                      'persists, CLA prints $81.06 against CL2’s $78.66',
                      'CL2 Comdty (Close)'],
                     ['Brent–WTI spread',
                      '$3.26 /bbl',
                      'wider by $0.07 on the day',
                      '$3.57 on the active contracts (COA $84.63 / CLA $81.06). The spread '
                      'has stayed near $3 for two sessions after halving from $6.44 on '
                      'Friday’s close — the Hormuz-specific premium that came out on the '
                      'announcement has not gone back in, even though the announcement did '
                      'not hold',
                      'derived'],
                     ['Henry Hub natural gas',
                      '$2.768 /MMBtu',
                      '–$0.013 (+$0.067 w/w)',
                      'from $3.06 (–9.6%) — US gas still BELOW pre-war after twenty-two weeks '
                      'of war; the Hormuz/LNG-routing signature is intact and this remains a '
                      'routing shock, not a global-energy shock',
                      'NGA Comdty (Close)'],
                     ['TTF Dutch gas (active)',
                      '€58.260 /MWh',
                      '+€0.755 (+€0.452 w/w)',
                      'from €31.23 (+86.6%) — European gas has now risen in two of the last '
                      'three sessions and sits €5.39 below the 24 Jul war record of €63.65. '
                      'TTF gave back less of the de-escalation trade than crude did and has '
                      'taken more of it back since',
                      'TZTA Comdty (Close)'],
                     ['Japan/Asia LNG (3 Aug close — no 4 Aug print)',
                      '¥3,421',
                      '–¥19 vs the 31 Jul ¥3,440',
                      'from ¥1,669 (+105.0%) — the 3 Aug print has BACKFILLED at ¥3,421, '
                      'resolving the blackout flagged last edition; there is no 4 Aug print, '
                      'flagged and NOT carried forward. Hormuz still moves roughly a fifth of '
                      'global LNG',
                      'JGLA Comdty (Close)']],
          'ustNote': '4 Aug 2026 yields are intraday. The 3 Aug close is confirmed and is the '
                     'reading on which every trigger and Stage-4 test below is judged. d/d is '
                     'vs the 3 Aug close; w/w vs 28 Jul. Monday’s US session tracked the '
                     'morning snapshot closely — the reconciliation in section 4 is the '
                     'smallest the monitor has recorded in a fortnight.',
          'ustHeader': ['Tenor',
                        'Yield (%) — intraday 4 Aug',
                        '∆ d/d (bp)',
                        '∆ w/w (bp)',
                        '∆ vs pre-war (bp)',
                        'BBG ticker'],
          'ust': [['2-year UST',
                   '4.25',
                   '+1.2',
                   '–3.7',
                   '+87.5 (from 3.37%) — the front end is flat while the long end holds its '
                   'war highs',
                   'USGG2YR Index'],
                  ['5-year UST',
                   '4.40',
                   '+0.9',
                   '+2.6',
                   '+89.4 (from 3.50%)',
                   'USGG5YR Index'],
                  ['10-year UST',
                   '4.69',
                   '+1.0',
                   '+8.0',
                   '+74.8 (from 3.94%) — the 3 Aug close of 4.6755% keeps the 4.65% Stage-4 '
                   'leg satisfied on a fourth consecutive close; this morning’s 4.6858% is '
                   '3.58 bp above it on a fifth session. The war record is the 4.7347% of 31 '
                   'Jul',
                   'USGG10YR Index'],
                  ['30-year UST',
                   '5.23',
                   '+0.5',
                   '+14.4',
                   '+62.2 (from 4.61%) — the 3 Aug close of 5.2274% is 17.74 bp above the 13 '
                   'May auction stop and keeps the 5.20% Stage-4 leg satisfied on a fourth '
                   'consecutive close. This morning’s 5.2327% is 3.27 bp above that leg and '
                   '23.27 bp above the 5.00% downgrade line. The war record is the 5.2724% of '
                   '31 Jul',
                   'USGG30YR Index'],
                  ['2s10s spread',
                   '+43.4 bp',
                   '–0.0',
                   '+11.7',
                   '–12.2 (still flatter than pre-war) — but holding within a basis point of '
                   'Friday’s post-May steepest and 19.2 bp off the 24 Jun war low of +24.25 '
                   'bp. The bear steepener has stalled rather than reversed',
                   'USYC2Y10 Index'],
                  ['10Y breakeven inflation',
                   '2.260',
                   '–0.2',
                   '+6.5',
                   '+0.3 (from 2.2569%) — spot compensation has come back to sit almost '
                   'exactly on its pre-war anchor after the 2.2846% close of 31 Jul, its '
                   'highest since 3 Jul. The forward has not followed it down',
                   'USGGBE10 Index'],
                  ['5Y5Y forward inflation',
                   '2.338',
                   '0.0',
                   '+7.1',
                   '+19.6 (from 2.14%) — the 3 Aug close of 2.3376% is a FIFTH consecutive '
                   'close above the 2.30% trigger that fired this channel 4→5 on 31 Jul, and '
                   'this morning prints the identical 2.3376%. Long-run inflation '
                   'compensation has not given back any of the war-record 2.3597%',
                   'USGG5Y5Y Index'],
                  ['SOFR (blank 3 and 4 Aug)',
                   '3.66',
                   '—',
                   'no print',
                   'the 31 Jul print has BACKFILLED at 3.66, up 1 bp from 30 Jul; 3 and 4 Aug '
                   'are blank, flagged and NOT carried as fresh',
                   'SOFRRATE Index']],
          'crossHeader': ['Gauge', 'Latest', 'As of', '∆ vs pre-war', 'Interpretation'],
          'cross': [['DXY',
                     '100.01',
                     '4 Aug intraday',
                     '+2.40 (from 97.61)',
                     'Up 0.11 this morning and back above 100 for the first time since 29 '
                     'July, having closed 99.897 on Monday. The dollar has stabilised exactly '
                     'as the diplomatic track failed, which is consistent with the '
                     'fortnight’s pattern: the currency sold off while a deal looked possible '
                     'and firmed when it stopped looking possible. It remains 1.41 below last '
                     'Tuesday.'],
                    ['MOVE',
                     '80.48',
                     '3 Aug close (no 4 Aug print)',
                     '+7.10 (from 73.38)',
                     'Down 2.54 from Friday’s 83.02, giving back part of the largest one-day '
                     'rise of the past month. Rates volatility is still 7.10 pts above '
                     'pre-war and 5.48 pts ABOVE the 75 line that forms the second leg of the '
                     'Treasury downgrade, so that downgrade remains unavailable. It is 49.52 '
                     'pts below the 130 Stage-4 Threshold C and well under the 115.02 war '
                     'high of 26 March. There is no 4 August print.'],
                    ['VIX',
                     '15.86',
                     '3 Aug close (no 4 Aug print)',
                     '–4.00 (from 19.86)',
                     'Down 0.13 to its lowest since 10 July and now a full four points BELOW '
                     'pre-war, while rates volatility sits 7.10 points above it. The '
                     'divergence survived the failure of the talks intact, which is the more '
                     'remarkable fact: equity volatility did not react at all to a '
                     'negotiation that both governments now describe differently.'],
                    ['AAA gasoline',
                     '$4.76 /gal',
                     '31 Jul print (3–4 Aug blank)',
                     '+$1.24 (from $3.52, +35.2%)',
                     'Political-stress score reference. The 31 Jul print has BACKFILLED at '
                     '$4.76 — a SECOND consecutive close above the $4.75 trigger, following '
                     'the $4.76 of 30 Jul and four straight sessions exactly on the line. '
                     'That is the sustained break the rule requires and the political channel '
                     'fires 4→5 this edition. The series is blank for 3 and 4 Aug, flagged '
                     'and not carried.'],
                    ['DOE gasoline',
                     '$4.096 /gal',
                     '27 Jul weekly print',
                     '+$1.16 (from ~$2.94, +39.4%)',
                     'Corroboration only; the weekly print due 3 Aug has not appeared in the '
                     'extract or on the EIA release page, which still shows the week to 27 '
                     'Jul. GasBuddy’s independent national average was $4.05 on 3 Aug, down '
                     '0.8c on the week, while its diesel average rose 7.1c to $5.326 — the '
                     'same gasoline-stalls, diesel-runs divergence the EIA series showed to '
                     '27 Jul.']],
          'gasChartNote': 'AUTMUSAG (AAA all-grades retail pump, daily) is the '
                          'political-stress score reference (pre-war $3.52, peak $5.18, '
                          'latest confirmed print $4.76 on 31 Jul; 3 and 4 Aug blank); '
                          'USRFRUSA (DOE regular-grade retail spot, weekly) is the '
                          'complementary gauge (pre-war ~$2.94, peak $4.50, latest $4.096 for '
                          'the week of 27 Jul). The dotted line is the $4.75 political→5 '
                          'threshold. The scored series printed exactly $4.75 on 24, 27, 28 '
                          'and 29 Jul, then $4.76 on 30 Jul and $4.76 again on 31 Jul on this '
                          'extract’s backfill — two consecutive closes through the line, '
                          'which fires the channel. GasBuddy’s separately published national '
                          'average was $4.05 on 3 Aug against $4.058 a week earlier, so the '
                          'corroborating retail series is stalling while diesel runs: '
                          'GasBuddy has diesel up 7.1 cents on the week and EIA had '
                          'on-highway diesel up 17.9 cents in the week to 27 Jul.',
          'straitHeader': ['Indicator', 'Current reading', 'Source'],
          'strait': [['Strait closed · day 156',
                      'Closed since 28 Feb. Traffic remains at crisis levels and the trackers '
                      'are not directly comparable. On an all-crossings basis Kpler counted '
                      '106 crossings by 96 distinct vessels in the week to 2 Aug against 98 '
                      'the week before, up 8%, with 11 on 1 Aug and 9 on 2 Aug; 43 of the '
                      'week’s crossings, about 41%, were classed ‘route undetermined’ against '
                      'roughly 49% the week before. Windward, on 1 Aug, logged 19 crossings '
                      'of which 6 were dark and none sanctioned, and recorded 1,130 '
                      'GPS-jammed vessels in the Gulf, up 173% on the seven-day average. '
                      'Lloyd’s List Intelligence has not published since 29 Jul; its last '
                      'brief put the week to 26 Jul at 39 transits against 82, with 70% '
                      'untraceable on AIS and inbound Gulf traffic down more than 90%. IMF '
                      'PortWatch’s latest record is 23 Jul at 10 vessels against an 88/day '
                      'baseline. War-risk cover is quoted at 7.5–10% of hull value against '
                      '1–3% pre-escalation.',
                      'Kpler via Foreign Policy Journal / Windward / Lloyd’s List '
                      'Intelligence / IMF PortWatch via straits.live'],
                     ['THE ANNOUNCED 3 AUGUST TALKS DID NOT CONVENE — THE TWO GOVERNMENTS NOW '
                      'CONTRADICT EACH OTHER',
                      'No outlet could source a session, a venue, an attendee list, a readout '
                      'or an Omani confirmation. Iran’s foreign ministry spokesman Esmaeil '
                      'Baghaei said at his Monday press conference: ‘We are not negotiating '
                      'with the United States at this time,’ adding that the Iranian '
                      'delegation ‘is not going anywhere, and is not expecting anyone to '
                      'visit’; Foreign Minister Araghchi was in Iraq for Arbaeen. US '
                      'officials separately told CBS News that no new negotiations with Iran '
                      'are planned. President Trump said the same day that ‘we’re talking, '
                      'and we’re talking at the request of Iran, backed by Saudi Arabia, '
                      'backed by UAE and backed by Qatar,’ called it ‘a last chance for them '
                      'to sign a good document’, said he was under no time constraint, and '
                      'said he wanted to give Iran ‘every last chance before decapitation.’ '
                      'He also said the strait could be ‘open literally by tomorrow, '
                      'completely open.’',
                      'CBS News / Euronews / The National / ABC News / CNN / Bloomberg / The '
                      'Hill'],
                     ['Iran hardens the terms: the strait ‘will in no way return’ to its '
                      'pre-war status',
                      'Baghaei said the Strait ‘will in no way return to the status it was '
                      'before February 28th’; that the Oman track concerns a TEMPORARY route '
                      'and is ‘a necessary but not sufficient condition’ for reopening; and '
                      'that reopening requires mechanisms protecting Iranian sovereignty. ABC '
                      'News describes the concept as a single transit corridor replacing the '
                      'divided northern and southern routes, with the toll — who levies it '
                      'and at what rate — still disputed. Note: the 31 Jul edition attributed '
                      'a similar line to Gharibabadi and the 3 Aug edition withdrew it as '
                      'uncorroborated; it is now sourced at Tier 1 to Baghaei on 3 Aug and is '
                      'used on that basis. No Iran–Oman corridor agreement has been signed; '
                      'the only instrument on record is the 23 Jun joint statement '
                      'establishing a working group.',
                      'The National / ABC News / Oman Ministry of Foreign Affairs'],
                     ['No new confirmed strike, but the strike option is documented and on '
                      'the table',
                      'CENTCOM has issued no strike release since 29 Jul, and no Tier 1 '
                      'outlet reported a new US or Israeli strike on Iran on 3 or 4 Aug. The '
                      'planning is now corroborated beyond a single outlet: CBS News reported '
                      'on 31 Jul that the US and Israel were preparing strikes on Iranian '
                      'power plants and refineries, potentially including electricity systems '
                      'across Tehran, with Pentagon spokesman Sean Parnell on the record that '
                      'the department is ‘locked and loaded, ready to execute the President’s '
                      'directives’ and the President yet to give final go orders. The '
                      '‘roughly two-week campaign’ duration carried in earlier editions is '
                      'NOT corroborated — CBS describes a weekend-scale window. UKMTO’s '
                      'report of an explosion beside a tanker about 20 nm north-east of '
                      'Khasab appears in Gulf outlets dated 3 Aug with the same particulars '
                      'as the 2 Aug report; it is treated as ONE incident, not two.',
                      'CENTCOM / CBS News / The Hill / Jerusalem Post / Sharjah24 / UKMTO'],
                     ['Treasury raises Q3 borrowing by $68bn; OPEC+ delivers September '
                      'barrels',
                      'The US Treasury said on 3 Aug it expects to borrow $739bn of net '
                      'marketable debt in July–September, $68bn above the $671bn projected on '
                      '4 May, and $628bn in October–December, assuming cash balances of '
                      '$950bn at end-September and $850bn at end-December; excluding a higher '
                      'starting balance the underlying increase is $87bn. The refunding '
                      'statement follows on Wednesday 5 Aug. On the physical side, the OPEC+ '
                      'eight confirmed the September increase of 188k b/d with a country '
                      'split (Saudi +62k, Russia +62k, Iraq +26k, Kuwait +16k, Kazakhstan '
                      '+10k, Algeria +6k, Oman +5k); the 67th JMMC of 2 Aug ‘emphasised the '
                      'importance of protecting maritime routes and energy infrastructure '
                      'from attacks.’ Aramco’s 400k b/d Jizan complex is targeted to restart '
                      'about 15 Aug; Abqaiq and Damietta remain unreported since late July. '
                      'ISM manufacturing for July came in at 55.6 against 54.0 expected, with '
                      'the prices index easing to 71.1.',
                      'Reuters / MT Newswires / US Treasury / OPEC / Rigzone / Reuters via '
                      'IIR / ISM']]},
 'analysis': {'intro': 'The shock rises to 27/30 on a single channel move, and the move came '
                       'from a backfill rather than from a new print. AUTMUSAG, the AAA pump '
                       'series that carries political stress, was blank for 31 July when the '
                       'last edition was written; this extract fills it at $4.76, a second '
                       'consecutive confirmed close above the $4.75 trigger, and the channel '
                       'fires 4→5 on exactly the two-close rule that fired US inflation on 31 '
                       'July. Everything else in the market tape was quiet: Monday’s closes '
                       'came in within a basis point or two of the Singapore-morning snapshot '
                       'across the curve, Brent closed 47 cents below its morning print, and '
                       'Tuesday’s intraday range in Brent is 74 cents. The news, by contrast, '
                       'was not quiet. The negotiations announced for Monday did not take '
                       'place; Iran’s foreign ministry said on the record that it is not '
                       'negotiating with the United States; US officials told CBS that no '
                       'talks are planned; and the President said talks were under way and '
                       'described the alternative as decapitation. That is not an ambiguous '
                       'readout, it is an absence of one, and the escalation downgrade '
                       'candidate opened last edition is closed. Against that, the dated '
                       'supply test arrived: Treasury raised its Q3 borrowing estimate by '
                       '$68bn into a long end sitting 17.74 bp above the May auction stop, '
                       'with the refunding statement tomorrow.',
              'bondYieldNote': '4 Aug yields are intraday; the 3 Aug close is confirmed and '
                               'every trigger runs off it. One channel moved: political '
                               'stress 4→5. Score rises to 27/30.',
              'bondYield': [{'title': '(i) Political stress — UPGRADED 4→5, the trigger fired '
                                      'by a backfill.',
                             'text': 'This is the move of the edition and it needs to be '
                                     'stated precisely, because it was decided by data that '
                                     'arrived rather than by data that changed. AUTMUSAG '
                                     'printed exactly $4.75 on 24, 27, 28 and 29 July, then '
                                     '$4.76 on 30 July — its first reading through the $4.75 '
                                     'threshold and its highest since 10 June. On 31 July the '
                                     'series went blank and the 3 August edition held the '
                                     'channel at 4, ARMED, because one close above a trigger '
                                     'is not a sustained break. This extract has backfilled '
                                     '31 July at $4.76. That is a second consecutive '
                                     'confirmed close above the trigger, which is the '
                                     'definition of a sustained break this monitor has '
                                     'applied consistently — it is the identical construction '
                                     'that fired US inflation 4→5 on 31 July after two '
                                     'consecutive closes above 2.20%, and the discipline that '
                                     'stopped the oil channel whipsawing on 25–26 June. The '
                                     'channel therefore moves to 5/5 and the score to 27/30. '
                                     'Two qualifications belong with it. First, the series is '
                                     'blank again for 3 and 4 August, so the upgrade rests on '
                                     '30 and 31 July and not on anything more recent. Second, '
                                     'the corroborating retail series is stalling rather than '
                                     'accelerating: GasBuddy’s national average was $4.05 on '
                                     '3 August, down 0.8 cents on the week. What is NOT '
                                     'stalling is diesel — GasBuddy has it up 7.1 cents on '
                                     'the week to $5.326 and EIA had on-highway diesel up '
                                     '17.9 cents in the week to 27 July against gasoline’s '
                                     '9.5. The pass-through constraint remains refining '
                                     'rather than crude, which is why Brent at $81 does not '
                                     'disarm this channel. No federal intervention — SPR '
                                     'release, export limit, waiver or gouging action — is '
                                     'confirmable in the window.'},
                            {'title': '(ii) Escalation risk — held at 5 (max), and the '
                                      'downgrade candidate is REVOKED rather than deferred.',
                             'text': 'The 3 August edition opened the first live downgrade '
                                     'candidate this channel has had since 9 July, on the '
                                     'strength of a cancelled US strike package and an '
                                     'announced negotiation, and deliberately did not take it '
                                     'because an announcement is not a stand-down. That '
                                     'judgment is now vindicated by the outcome rather than '
                                     'by the reasoning. The talks did not convene. Iran’s '
                                     'foreign ministry spokesman said on the record that '
                                     'Tehran is not negotiating with Washington and that its '
                                     'delegation is going nowhere; the foreign minister was '
                                     'in Iraq; US officials told CBS News that no '
                                     'negotiations are planned; and no outlet could source a '
                                     'venue, an attendee list, a readout, or a confirmation '
                                     'from Oman. The President’s own account — that talks '
                                     'were under way at Iran’s request — is contradicted by '
                                     'his own officials and by Tehran simultaneously, and he '
                                     'paired it with an explicit threat of decapitation. Two '
                                     'further facts push the same way. CBS News independently '
                                     'corroborated the reporting that the US and Israel are '
                                     'preparing strikes on Iranian power plants and '
                                     'refineries, with a named Pentagon spokesman on the '
                                     'record that the department is ‘locked and loaded’ and '
                                     'only the final order outstanding — so what was a '
                                     'single-outlet Al Jazeera item is now a multi-outlet '
                                     'one, though the ‘two-week campaign’ duration is not '
                                     'corroborated. And Iran hardened its terms: Baghaei said '
                                     'the strait ‘will in no way return to the status it was '
                                     'before February 28th’ and that an Oman route deal is '
                                     'necessary but not sufficient to reopen it. The channel '
                                     'stays pinned at its maximum and the path to a downgrade '
                                     'is now longer than it was 24 hours ago.'},
                            {'title': '(iii) Treasury — held at 5 (max), and the supply test '
                                      'has arrived.',
                             'text': 'The 30Y closed 5.2274% on 3 August and the 10Y 4.6755%, '
                                     'keeping both Stage-4 legs satisfied on a fourth '
                                     'consecutive close; this morning’s 5.2327% and 4.6858% '
                                     'carry them to a fifth session. Both downgrade legs '
                                     'continue to fail: the 30Y is 22.74 bp above the 5.00% '
                                     'line on the close, and MOVE at 80.48 is 5.48 pts above '
                                     'the 75 leg even after giving back 2.54 from Friday’s '
                                     'spike. The material development is fiscal, not '
                                     'monetary. Treasury said on Monday it now expects to '
                                     'borrow $739bn of net marketable debt in July–September, '
                                     '$68bn more than the $671bn it projected on 4 May, and '
                                     '$628bn in October–December, on assumed cash balances of '
                                     '$950bn at end-September and $850bn at end-December; '
                                     'Reuters reports that stripping out a '
                                     'higher-than-assumed starting balance leaves an '
                                     'underlying increase of $87bn, attributed to lower '
                                     'projected cash flows. The second quarter closed with '
                                     '$190bn borrowed and a $919bn cash balance, $1bn above '
                                     'plan. The refunding statement follows at 8:30am ET on '
                                     'Wednesday 5 August against 6 May guidance holding '
                                     'coupon sizes at 3Y $58bn / 10Y $42bn / 30Y $25bn ‘for '
                                     'at least the next several quarters’, and the 30Y leg '
                                     'auctions in the week of 10 August. A long end 17.74 bp '
                                     'above the May auction stop now has a quantified '
                                     'increase in supply to absorb, and the question the '
                                     'auction answers is no longer hypothetical.'},
                            {'title': '(iv) US inflation impulse — held at 5 (max), and still '
                                      'not fading.',
                             'text': '5Y5Y forward inflation closed at 2.3376% on 3 August, a '
                                     'fifth consecutive close above the 2.30% trigger, and '
                                     'prints the identical 2.3376% this morning. The series '
                                     'has now run 2.3302%, 2.3303%, 2.3597%, 2.3376% and '
                                     '2.3376% across five sessions; it gave back 2.21 bp from '
                                     'the war record and no more. The 10Y breakeven has '
                                     'behaved differently and the difference is informative: '
                                     'after closing 2.2846% on 31 July, its highest since 3 '
                                     'July, it closed 2.2622% on Monday and prints 2.2603% '
                                     'now, back to within a third of a basis point of its '
                                     '2.2569% pre-war anchor. Near-term compensation has '
                                     'normalised while the forward has not, which is the '
                                     'signature of a market pricing a persistent '
                                     'policy-credibility problem rather than a transitory '
                                     'energy shock — and it is worth noting that this '
                                     'happened while Brent fell nearly $7 on Monday and the '
                                     'ISM prices index eased to 71.1 from 73.0. The '
                                     'downgrade, 5Y5Y sustained at or below the 2.142% '
                                     'anchor, is 19.56 bp away and not in play. At 5/5 the '
                                     'channel can only subtract.'},
                            {'title': '(v) Oil — held at 2, and this is the only channel left '
                                      'that can raise the score.',
                             'text': 'The last confirmed close is $81.09 (3 August), $13.91 '
                                     'below the $95 upgrade trigger and $8.61 above the '
                                     '$72.48 downgrade anchor — the narrowest that downgrade '
                                     'gap has been since 10 July. This morning Brent prints '
                                     '$81.92, up $0.83, in a 74-cent range. What is notable '
                                     'is what did not happen: the diplomacy that took $6.84 '
                                     'out of Brent on Monday turned out not to exist, and '
                                     'Brent recovered 83 cents. The $6.44 Brent–WTI spread '
                                     'that collapsed to $3.14 on the announcement has stayed '
                                     'near $3. The market has priced the OPEC+ September '
                                     'increment and the removal of the immediate strike risk, '
                                     'and has not re-priced the failure of the talks. The '
                                     'physical case for a higher number is unchanged and '
                                     'arguably firmer: effective OPEC+ spare capacity was '
                                     'roughly 0.17 mb/d on the IEA’s July estimate, so '
                                     'September’s 188k b/d is a quota rather than a cargo; '
                                     'Jizan’s 400k b/d is out to about 15 August; Abqaiq '
                                     'still shows unexplained burn scars; Damietta’s status '
                                     'since the 29–30 July strike is still unreported; and '
                                     'the strait is closed on day 156 with route-undetermined '
                                     'traffic at roughly 41% of crossings. The channel stays '
                                     'at 2 because $81.09 is not $95. But with five of six '
                                     'channels now maxed, oil is the only one that can move '
                                     'this score up, and the downgrade leg it acquired last '
                                     'edition — a mediated pause — has just been withdrawn.'},
                            {'title': '(vi) Maritime denial — held at 5 (max).',
                             'text': 'The strait is closed on day 156 and Iran has now stated '
                                     'at Tier 1 that it will not return to its pre-war '
                                     'status. Kpler’s all-crossings series shows the week to '
                                     '2 August at 106 crossings by 96 vessels against 98 the '
                                     'week before, an 8% rise, with route-undetermined '
                                     'traffic easing from about 49% to about 41%; that is a '
                                     'marginal improvement from a crisis baseline and nothing '
                                     'like the 25%-of-normal-for-ten-sessions the downgrade '
                                     'requires. Windward logged 19 crossings on 1 August with '
                                     '6 dark, against roughly 140 a day pre-crisis, and 1,130 '
                                     'GPS-jammed vessels in the Gulf, up 173% on its '
                                     'seven-day average. No corridor agreement has been '
                                     'signed; the only instrument on record remains the 23 '
                                     'June Oman–Iran joint statement establishing a working '
                                     'group.'}],
              'stage4Note': 'Stage 4 is a credit/auction event. Threshold B is satisfied on '
                            'four consecutive confirmed closes and the supply number is now '
                            'published rather than assumed.',
              'stage4': [{'title': 'Threshold A · 13 May 30Y auction, cleared 5.050% — the '
                                   'test is now quantified.',
                          'text': 'Historical benchmark; the 9 July re-opening cleared 5.06% '
                                  'with a 0.3 bp stop-through. The 3 August close of 5.2274% '
                                  'is 17.74 bp above the May stop, narrower than Friday’s '
                                  'war-widest 22.24 bp but still the second-widest week of '
                                  'the war. On Monday Treasury published the number this '
                                  'monitor has been waiting for: net marketable borrowing of '
                                  '$739bn for July–September against the $671bn projected on '
                                  '4 May, an increase of $68bn, with $628bn guided for '
                                  'October–December and assumed cash balances of $950bn at '
                                  'end-September and $850bn at end-December. Reuters '
                                  'attributes the rise to lower projected cash flows only '
                                  'partly offset by a higher starting balance, and puts the '
                                  'underlying increase at $87bn. April–June closed with '
                                  '$190bn borrowed and a $919bn end-June balance, $1bn above '
                                  'the May assumption. The refunding statement lands at '
                                  '8:30am ET on Wednesday 5 August; the 6 May guidance held '
                                  'coupon auction sizes at 3Y $58bn / 10Y $42bn / 30Y $25bn '
                                  'and promised no increase ‘for at least the next several '
                                  'quarters.’ If that guidance survives a $68bn upgrade to '
                                  'the quarter’s borrowing need, the bill market absorbs it; '
                                  'if it does not, the 30Y leg in the week of 10 August is '
                                  'the first coupon auction of a larger programme into a long '
                                  'end already at war highs. That is the specific sequence '
                                  'that would make Threshold A live rather than historical.'},
                         {'title': 'Threshold B · 30Y above 5.20% with 10Y above 4.65% — '
                                   'SATISFIED on four consecutive confirmed closes.',
                          'text': '29 July: 5.2007% / 4.6773%. 30 July: 5.2135% / 4.6733%. 31 '
                                  'July: 5.2724% / 4.7347%, both war records. 3 August: '
                                  '5.2274% / 4.6755%. Monday cleared the legs by 2.74 bp and '
                                  '2.55 bp, against 7.24 bp and 8.47 bp on Friday — a '
                                  'narrower but still unambiguous pass, and the point of a '
                                  'persistence threshold is persistence rather than margin. '
                                  'This morning’s 5.2327% and 4.6858% keep both satisfied on '
                                  'a fifth session. The qualification is unchanged: the '
                                  'threshold warns that the long end is repricing in a way '
                                  'that historically precedes an auction or credit event; it '
                                  'is not a Stage-4 event in itself. What has changed is that '
                                  'the event it warns about now has a date and a size. The '
                                  'mechanism arming it remains domestic fiscal and monetary '
                                  'credibility rather than a Hormuz headline — which is why a '
                                  'failed negotiation moved crude 83 cents and moved the 30Y '
                                  'half a basis point.'},
                         {'title': 'Threshold C · MOVE above 130. Far off, and it eased this '
                                   'session.',
                          'text': 'The index closed at 80.48 on 3 August, down 2.54 from '
                                  'Friday’s 83.02, its highest since 19 May. That leaves '
                                  '49.52 pts to the threshold and it remains well under the '
                                  '115.02 war high of 26 March, so C is not close. Two '
                                  'observations belong with it anyway. First, at 80.48 the '
                                  'index is still 5.48 pts above the 75 line that forms the '
                                  'second leg of the Treasury downgrade, so the same reading '
                                  'that keeps C remote keeps that downgrade unavailable. '
                                  'Second, a fall in rates volatility on the session before a '
                                  'refunding statement is not obviously reassurance; it is '
                                  'the market declining to pre-position. There is no 4 August '
                                  'print, and the number is flagged rather than carried as '
                                  'fresh.'}],
              'crossAsset': 'The cross-asset signature this session is stillness in the '
                            'market and rupture in the news, which is close to the inverse of '
                            'Friday. Monday’s closes landed within two basis points of the '
                            'Singapore-morning snapshot everywhere on the curve: the 30Y at '
                            '5.2274% against 5.2370% published, the 10Y at 4.6755% against '
                            '4.6939%, 5Y5Y at 2.3376% against 2.3367%. MOVE eased 2.54 to '
                            '80.48, VIX 0.13 to 15.86 and its lowest since 10 July, and the '
                            'dollar firmed back above 100 for the first time since 29 July. '
                            'Brent closed $81.09, 47 cents below its morning print, and this '
                            'morning trades in a 74-cent range at $81.92 — a market with '
                            'nothing to price. Yet in the same 24 hours the announced US–Iran '
                            'negotiation failed to materialise and the two governments issued '
                            'mutually exclusive accounts of whether it exists, Iran stated '
                            'that the strait will not return to its pre-war status, and the '
                            'US Treasury told the market it needs to borrow $68bn more this '
                            'quarter than it said in May. Equity and rates volatility both '
                            'fell through that. Henry Hub at $2.768 remains 9.6% BELOW '
                            'pre-war, so the routing signature is intact and this is still '
                            'not a global-energy shock. The reading to take is not that the '
                            'news stopped mattering; it is that the market has stopped '
                            'trading Hormuz headlines and started waiting for Wednesday.'},
 'channels': [{'name': 'Maritime denial',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 (max). Strait closed to commercial traffic, day 156. '
                            'Kpler’s all-crossings series has the week to 2 Aug at 106 '
                            'crossings by 96 vessels against 98 the week before (+8%), with '
                            'route-undetermined traffic easing from ~49% to ~41%; 11 '
                            'crossings on 1 Aug and 9 on 2 Aug. Windward logged 19 crossings '
                            'on 1 Aug (6 dark) against ~140 a day pre-crisis and 1,130 '
                            'GPS-jammed vessels in the Gulf, +173% on its 7-day average. '
                            'Baghaei said on 3 Aug the strait ‘will in no way return to the '
                            'status it was before February 28th’. No corridor agreement '
                            'signed.',
               'upgrade': 'at max.',
               'downgrade': 'verified reopening (escorted convoys) with traffic above 25% of '
                            'normal for 10 sessions → to 3–4. A signed corridor agreement '
                            'starts that clock; an announcement does not.'},
              {'name': 'Oil price shock',
               'score': 2,
               'state': 'live',
               'rationale': 'Held at 2 — and now the ONLY channel that can raise the score. '
                            'Last confirmed close $81.09 (3 Aug), $13.91 below the $95 '
                            'trigger and $8.61 above the $72.48 anchor, the narrowest since '
                            '10 Jul; intraday $81.92, up $0.83 in a 74-cent range. Monday’s '
                            '$6.84 fall priced a negotiation that did not take place, and '
                            'only 83 cents of it has come back. Physical supply unchanged: '
                            'effective spare capacity ~0.17 mb/d, Jizan out to ~15 Aug, '
                            'Abqaiq unexplained.',
               'upgrade': 'Brent above $95 sustained → to 3.',
               'downgrade': 'mediated pause + close at/below the $72.48 anchor → to 1. The '
                            'pause leg is WITHDRAWN this edition — the talks did not '
                            'convene.'},
              {'name': 'US inflation impulse',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 (max). 5Y5Y closed 2.3376% on 3 Aug, a FIFTH '
                            'consecutive close above the 2.30% trigger that fired this '
                            'channel 4→5 on 31 Jul, and prints the identical 2.3376% '
                            'intraday. It has given back 2.21 bp from the 2.3597% war record '
                            'and no more. The 10Y breakeven, by contrast, has returned to '
                            'within 0.3 bp of its 2.2569% pre-war anchor: near-term '
                            'compensation normalising while the forward holds is a '
                            'credibility signature, not an energy one.',
               'upgrade': 'at max.',
               'downgrade': '5Y5Y sustained at/below the 2.142% pre-war anchor → to 4 (19.56 '
                            'bp away on the last close).'},
              {'name': 'Treasury stress',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 (max). The 30Y closed 5.2274% and the 10Y 4.6755% on 3 '
                            'Aug, keeping both Stage-4 legs satisfied on a FOURTH consecutive '
                            'close; intraday 5.2327% / 4.6858% carries them to a fifth '
                            'session. The 30Y is 17.74 bp above the 13 May auction stop. '
                            'Treasury raised its Q3 net marketable borrowing estimate to '
                            '$739bn from $671bn, with the refunding statement on 5 Aug and '
                            'the 30Y leg the week of 10 Aug. MOVE eased 2.54 to 80.48.',
               'upgrade': 'at max.',
               'downgrade': '30Y close under 5.00% with MOVE under 75 sustained → to 4. Both '
                            'legs fail by 22.74 bp and 5.48 pts.'},
              {'name': 'Political stress',
               'score': 5,
               'state': 'max',
               'rationale': 'UPGRADED 4→5. AUTMUSAG has BACKFILLED 31 Jul at $4.76 — a second '
                            'consecutive confirmed close above the $4.75 trigger after the '
                            '$4.76 of 30 Jul and four sessions exactly on the line. That is '
                            'the sustained break the rule requires, on the identical '
                            'construction that fired US inflation on 31 Jul. 3 and 4 Aug are '
                            'blank, flagged and not carried. Corroboration is mixed: '
                            'GasBuddy’s national average fell 0.8c on the week to $4.05 while '
                            'its diesel average rose 7.1c to $5.326 — refining, not crude, '
                            'remains the binding constraint.',
               'upgrade': 'at max.',
               'downgrade': 'sustained retreat toward the $3.52 pre-war level → to 4 then 3. '
                            '$1.24 above the anchor.'},
              {'name': 'Escalation risk',
               'score': 5,
               'state': 'max',
               'rationale': 'Held at 5 (max) — and the downgrade candidate opened last '
                            'edition is REVOKED, not deferred. The talks announced for 3 Aug '
                            'did not convene: Baghaei said ‘we are not negotiating with the '
                            'United States at this time’ and that Iran’s delegation is going '
                            'nowhere; US officials told CBS no negotiations are planned; '
                            'Trump said talks were under way at Iran’s request and called it '
                            'a last chance before ‘decapitation’. CBS corroborated US/Israeli '
                            'planning for strikes on Iranian power plants and refineries with '
                            'the Pentagon on the record as ‘locked and loaded’.',
               'upgrade': 'at max.',
               'downgrade': 'mediated stand-down + talks resume → to 4–3. Requires a session '
                            'to actually take place, be confirmed by the mediator, and hold '
                            'across a sustained window with no new strikes.'}],
 'scoreTotal': 'CRISIS band — UP one point, the highest reading since 31 May. Political '
               'stress fired 4→5 on the two-close rule when AUTMUSAG backfilled 31 Jul at '
               '$4.76. FIVE of six channels are now maxed and only oil, at 2/5, can raise '
               'this number further — a three-point range in a thirty-point scale. The one '
               'live downgrade candidate the monitor carried has been withdrawn because the '
               'negotiation it rested on did not happen.',
 'whatsChanged': {'title': "4 · What's changed since the last edition (3 Aug AM → 4 Aug AM)",
                  'items': ['Score rises to 27/30 on the political-stress upgrade. The '
                            'announced talks did not convene. Treasury raises Q3 borrowing by '
                            '$68bn. Four dark series backfill. Source: Bloomberg unless '
                            'stated.',
                            'AUTMUSAG backfilled 31 July at $4.76 — the second consecutive '
                            'close through the political trigger, and the channel fires 4→5. '
                            'The scored AAA pump series printed exactly $4.75 on 24, 27, 28 '
                            'and 29 July, $4.76 on 30 July — its first reading through the '
                            '$4.75 threshold and its highest since 10 June — and was blank '
                            'for 31 July when the last edition went out. This extract fills '
                            '31 July at $4.76. Two consecutive confirmed closes above a '
                            'trigger is the sustained break the rule requires, and it is the '
                            'same construction that fired US inflation 4→5 on 31 July. '
                            'Political stress moves to 5/5 and the score to 27/30. Source: '
                            'Bloomberg.',
                            'The talks announced for 3 August did not convene, and the two '
                            'governments now contradict each other in public. Iran’s foreign '
                            'ministry spokesman Esmaeil Baghaei told his Monday press '
                            'conference: ‘We are not negotiating with the United States at '
                            'this time,’ adding that Iran’s delegation ‘is not going '
                            'anywhere, and is not expecting anyone to visit’; Foreign '
                            'Minister Araghchi was in Iraq for Arbaeen. US officials told CBS '
                            'News that no new negotiations are planned. President Trump said '
                            'the same day that talks were under way ‘at the request of Iran, '
                            'backed by Saudi Arabia, backed by UAE and backed by Qatar’, '
                            'called it ‘a last chance for them to sign a good document’ and '
                            'said he wanted to give Iran ‘every last chance before '
                            'decapitation’. No venue, attendee list, readout or Omani '
                            'confirmation could be sourced. Source: CBS News / The National / '
                            'Euronews / ABC News / CNN / The Hill.',
                            'The escalation downgrade candidate is revoked — the first time '
                            'this monitor has opened and closed one in consecutive editions. '
                            'The 3 August edition opened the channel’s first live downgrade '
                            'since 9 July and deliberately did not take it, on the ground '
                            'that an announcement is not a stand-down. The talks did not '
                            'happen. Had the channel been moved on the announcement, it would '
                            'have had to be reversed within a session — the 25–26 June error '
                            'repeated in the opposite direction. The rule that prevented it '
                            'is recorded in section 9. Source: as above.',
                            'Treasury raised its July–September borrowing estimate to $739bn, '
                            '$68bn above the May projection. The estimate published Monday 3 '
                            'August puts net marketable borrowing at $739bn for '
                            'July–September against the $671bn projected on 4 May, and $628bn '
                            'for October–December, assuming cash balances of $950bn at '
                            'end-September and $850bn at end-December. Reuters attributes the '
                            'increase to lower projected cash flows only partly offset by a '
                            'higher starting balance and puts the underlying rise at $87bn. '
                            'April–June closed with $190bn borrowed and a $919bn end-June '
                            'balance. The refunding statement follows at 8:30am ET on '
                            'Wednesday 5 August; the 30Y leg auctions the week of 10 August. '
                            'Source: Reuters / MT Newswires / US Treasury.',
                            'Iran hardened its terms on the strait, and the line this monitor '
                            'withdrew last week is now sourceable at Tier 1. Baghaei said on '
                            '3 August that the Strait ‘will in no way return to the status it '
                            'was before February 28th’, that the Oman track concerns a '
                            'temporary route and is ‘a necessary but not sufficient '
                            'condition’ for reopening, and that reopening requires mechanisms '
                            'protecting Iranian sovereignty. The 31 July edition attributed a '
                            'similar line to Gharibabadi and the 3 August edition withdrew it '
                            'as uncorroborated; it is restored here on a Tier 1 attribution '
                            'to Baghaei. ABC News describes the corridor concept as a single '
                            'transit route replacing the divided northern and southern '
                            'corridors, with the toll still disputed. Source: The National / '
                            'ABC News.',
                            'Four dark series backfilled — and one of them decided the score. '
                            'The 3 August edition flagged JGLA, AUTMUSAG and SOFR as running '
                            'dark, with MOVE and VIX carried as Friday closes. This extract '
                            'fills AUTMUSAG for 31 July at $4.76, SOFR for 31 July at 3.66, '
                            'JGLA for 3 August at ¥3,421, and MOVE and VIX for 3 August at '
                            '80.48 and 15.86. AUTMUSAG and SOFR remain blank for 3 and 4 '
                            'August and JGLA for 4 August. This is the second consecutive '
                            'month in which a §9.8-flagged blackout has resolved on backfill '
                            'within two sessions. Source: Bloomberg.',
                            'The strike option is corroborated beyond a single outlet, with '
                            'the Pentagon on the record. CBS News reported on 31 July that '
                            'the US and Israel were preparing strikes on Iranian power plants '
                            'and refineries, potentially including electricity systems across '
                            'Tehran, with Pentagon spokesman Sean Parnell stating the '
                            'department is ‘locked and loaded, ready to execute the '
                            'President’s directives’ and the President yet to give final go '
                            'orders. The Hill and the Jerusalem Post carried the same '
                            'reporting. The ‘roughly two-week campaign’ duration carried in '
                            'earlier editions is NOT corroborated — CBS describes a '
                            'weekend-scale window — and that qualifier is corrected here. '
                            'Source: CBS News / The Hill / Jerusalem Post.',
                            'Correction: the Iraqi militia deadline is corroborated above '
                            'Tier 3, and there are two dates, not one. The 3 August edition '
                            'demoted this item to Tier 3. Rudaw reported on 29 July that the '
                            'Islamic Resistance in Iraq set 7 August for Iraqi government '
                            'bodies to act on disarmament demands, with any response deferred '
                            'until after Arbaeen; Ynetnews reported the same day that Kataib '
                            'Hezbollah gave Baghdad until 6 August. Both are above Tier 3 and '
                            'appear to be related but distinct ultimatums. The trigger event '
                            'is confirmed: US–Saudi strikes on Popular Mobilization Forces in '
                            'Diyala killed 20 including Iranian advisers, and CENTCOM issued '
                            'a release on 28 July. Source: Rudaw / Ynetnews / CENTCOM.',
                            'Monday’s reconciliation was the smallest in a fortnight — the '
                            'opposite of Friday’s record gap. The 3 August close came in '
                            'within two basis points of the Singapore-morning snapshot across '
                            'the curve and 47 cents below it in Brent. Friday’s gaps were '
                            '$1.97 and 7.59 bp. The lesson is not that the snapshot is '
                            'reliable but that its error is regime-dependent: it is large '
                            'when the US session has news to trade and small when it does '
                            'not. Source: Bloomberg.',
                            'OPEC+ published the September country split; ISM manufacturing '
                            'beat; the EIA weekly is still to come. The 188k b/d September '
                            'increase breaks down as Saudi +62k, Russia +62k, Iraq +26k, '
                            'Kuwait +16k, Kazakhstan +10k, Algeria +6k, Oman +5k; the 67th '
                            'JMMC of 2 August emphasised ‘protecting maritime routes and '
                            'energy infrastructure from attacks’ and the next meetings are 6 '
                            'September and 4 October. ISM manufacturing for July printed 55.6 '
                            'against 54.0 expected, with production at 58.5 (highest since '
                            'November 2021), employment at 52.8 (first expansion in 33 '
                            'months) and prices easing to 71.1. No new EIA Weekly Petroleum '
                            'Status Report has been released — the next is due 5 August, and '
                            'the 24 July print stands with SPR at 307.7 mb after a 3.7 mb '
                            'draw. Source: Rigzone / OPEC / ISM / EIA.']},
 'scenarios': [{'name': 'Return to full war',
                'p': 40,
                'desc': 'Higher, and decisively the modal path again. The negotiation that '
                        'justified last edition’s fall never took place; the President paired '
                        'his account of it with an explicit threat of ‘decapitation’ and a '
                        '‘last chance’ framing; and US/Israeli planning for strikes on '
                        'Iranian power plants and refineries is now corroborated by CBS News '
                        'with a named Pentagon spokesman saying the department is ‘locked and '
                        'loaded’ and only the final order outstanding.',
                'path': 'Brent $105–140; MOVE above 90; oil to 3–4; score 28–29 (political '
                        'already at max).'},
               {'name': 'Deal collapse — talks stall on terms',
                'p': 26,
                'desc': 'Marginally lower only because part of this path has already been '
                        'realised: the announced round did not convene. What survives is the '
                        'bilateral Iran–Oman corridor negotiation, which Araghchi called '
                        'near-final on 2 Aug and which Baghaei on 3 Aug described as '
                        'temporary, sovereignty-conditioned and ‘necessary but not '
                        'sufficient’. The stated objectives remain incompatible — ‘immediate, '
                        'complete and total opening’ against a strait that ‘will in no way '
                        'return’ to its pre-war status.',
                'path': 'Brent $92–108; oil to 3; 30Y sustained above 5.20% with the 10Y '
                        'above 4.65%; score 28.'},
               {'name': 'Contained but violent — blockaded stalemate',
                'p': 16,
                'desc': 'Higher. This is the path the tape itself is pricing: VIX at its '
                        'lowest since 10 Jul, MOVE easing, Brent in a 74-cent range, while '
                        'the strait stays shut on day 156 and no strike is launched. It is '
                        'also the path where the score sits at 27 for weeks, because five of '
                        'six channels are pinned at 5 and only oil can move.',
                'path': 'Brent $78–92; MOVE 75–85; risk premium $6–14/bbl; score holds 27.'},
               {'name': 'Regional relapse — Gulf energy infrastructure hit',
                'p': 13,
                'desc': 'Marginally higher. The exposure is unchanged and the intent is now '
                        'better documented: Jizan out to about 15 Aug, Abqaiq burn scars on '
                        'four of six spheroids with no Aramco comment, Damietta status still '
                        'unreported since the 29–30 Jul strike, effective spare capacity '
                        '~0.17 mb/d, and the Iraqi militia deadlines of 6 and 7 Aug pending.',
                'path': 'Brent $150+; emergency policy response; HY spreads above 500 bp; '
                        'score 29–30.'},
               {'name': 'Mediated pause — the ceasefire sticks',
                'p': 5,
                'desc': 'Sharply lower, and the largest single fall in the map since it was '
                        'rebuilt. The entire case for this line last edition was a cancelled '
                        'strike package and an announced negotiation. The negotiation did not '
                        'happen and Iran denies one is under way. What remains is the Oman '
                        'corridor track, which is about managing a closed strait rather than '
                        'ending a war.',
                'path': 'Brent $72–84; MOVE under 75; escalation→4 then 3, maritime→3–4 on '
                        'verified traffic; score falls toward 21–23.'}],
 'scenarioShift': 'Probability shifts from the 3 Aug edition: mediated pause −7 (12→5), the '
                  'largest single fall in the map, because the announced talks did not '
                  'convene and Iran’s foreign ministry stated on the record that it is not '
                  'negotiating with Washington; full war +6 (34→40) and modal again, on the '
                  'failed negotiation, the ‘decapitation’ framing and CBS’s corroboration of '
                  'strike planning against Iranian power plants and refineries with the '
                  'Pentagon ‘locked and loaded’; contained-but-violent +1 (15→16), the path '
                  'the tape is actually pricing; regional relapse +1 (12→13) on unchanged '
                  'exposure and two pending Iraqi militia deadlines; deal collapse −1 '
                  '(27→26), lower only because part of it has already happened. Probabilities '
                  'sum to 100.',
 'watchlist': ['The refunding statement, Wednesday 5 August at 8:30am ET — the single most '
               'consequential scheduled event on the calendar. Treasury raised its '
               'July–September net marketable borrowing estimate to $739bn on Monday, $68bn '
               'above the 4 May projection of $671bn, with $628bn guided for '
               'October–December. The 6 May refunding held coupon sizes at 3Y $58bn / 10Y '
               '$42bn / 30Y $25bn and promised no increase ‘for at least the next several '
               'quarters.’ Whether that guidance survives the upgrade is the question. The '
               '30Y refunding leg auctions in the week of 10 August into a long end that '
               'closed 17.74 bp above the 13 May auction stop and has satisfied Stage-4 '
               'Threshold B on four consecutive closes.',
               'AUTMUSAG’s next print — the upgrade has fired, so the question is now whether '
               'it holds. The channel moved on 30 and 31 July at $4.76. The series is blank '
               'for 3 and 4 August. A backfill materially below $4.75 would not reverse the '
               'upgrade (hysteresis requires a sustained reversal past a wider threshold) but '
               'it would change the read on how durable the break is. Watch GasBuddy '
               'alongside it: its national average fell 0.8 cents on the week to $4.05 on 3 '
               'August while diesel rose 7.1 cents to $5.326, and Patrick De Haan attributes '
               'the product strength to Ukrainian strikes on Russian refining rather than to '
               'Hormuz.',
               'Whether any US–Iran session actually takes place, and whether Oman confirms '
               'it. The escalation downgrade is now further away than it was, and reopening '
               'it requires more than another announcement: a session that demonstrably '
               'convened, mediator confirmation, an end to Tehran’s public denial that talks '
               'exist, and no new strike, sustained across several sessions. Note the '
               'asymmetry — CENTCOM has issued no strike release since 29 July, so the '
               'absence of strikes is real; it is the presence of a negotiation that cannot '
               'be sourced.',
               'The EIA Weekly Petroleum Status Report, Wednesday 5 August — and the SPR line '
               'in particular. No weekly has been released since the 29 July print for the '
               'week to 24 July: crude 404.5 mb and about 6% below the five-year average, '
               'gasoline 211.3 mb and 7% below, distillate about 10% below, refinery '
               'utilisation 97.2%, and SPR 307.7 mb after a 3.7 mb draw. Refinery utilisation '
               'at 97.2% with distillate 10% below average is the mechanism that keeps the '
               'political channel elevated independent of crude.',
               'July payrolls on 7 August and July CPI on 12 August, into a market pricing a '
               'September HIKE. The FOMC held on 29 July at 3.50–3.75% by 9–3 with all three '
               'dissents FOR a hike. Polymarket had roughly 60% on a 25 bp September hike as '
               'of 2 August; no live CME FedWatch reading for 3–4 August could be sourced. '
               'Payrolls consensus is around +88k with unemployment at 4.2%. JOLTS for June '
               'is due today. Both prints land before the 15–16 September meeting, and 5Y5Y '
               'at 2.3376% says the market does not believe the inflation argument has been '
               'won.',
               'The 6 and 7 August Iraqi militia deadlines, and three series to re-verify. '
               'Ynetnews reported Kataib Hezbollah giving Baghdad until 6 August; Rudaw '
               'reported the Islamic Resistance in Iraq setting 7 August, with any response '
               'deferred until after Arbaeen. Both are above Tier 3 and both follow the 28–29 '
               'July US–Saudi strikes in Diyala. On the data side: JGLA has no 4 August print '
               'and is never carried forward; AUTMUSAG and SOFR are blank for 3 and 4 August; '
               'MOVE and VIX printed for 3 August but not 4 August.'],
 'sourceLog': {'tier1Market': 'Bloomberg Terminal extract (US Iran BBG Data.xlsx, 153 data '
                              'rows × 99 columns, restated front-month continuation series). '
                              'Tickers: CO2/CL2 Comdty (front-month; last confirmed close '
                              '$81.09 / $77.90 on 3 Aug, intraday $81.92 / $78.66 with a '
                              'Brent high of 82.00 and low of 81.26); COA/CLA Comdty (active, '
                              'unscored — $84.63 / $81.06); NGA ($2.768), TZTA (€58.260) and '
                              'JGLA (¥3,421 on the 3 Aug close, backfilled from the blackout '
                              'flagged last edition; no 4 Aug print, flagged not carried); '
                              'USGG2YR/5YR/10YR/20YR/30YR (30Y closed 5.2274% and 10Y 4.6755% '
                              'on 3 Aug, a fourth consecutive close satisfying both Stage-4 '
                              'legs; 5.2327% / 4.6858% intraday); USYC2Y10 (+43.407 close, '
                              '+43.404 intraday); USGGBE10 (2.2622 close, 2.2603 intraday, '
                              'within 0.3 bp of the pre-war anchor); USGG5Y5Y (2.3376 close, '
                              'a fifth consecutive close above the 2.30% trigger; 2.3376 '
                              'intraday); SOFRRATE (31 Jul backfilled at 3.66; blank 3 and 4 '
                              'Aug, flagged not carried); MOVE (80.48 on the 3 Aug close, '
                              '−2.54; no 4 Aug print) and VIX (15.86, lowest since 10 Jul; no '
                              '4 Aug print); DXY (99.897 close, 100.011 intraday, back above '
                              '100 for the first time since 29 Jul); AUTMUSAG (AAA all-grades '
                              'pump — score reference; 31 Jul BACKFILLED at $4.76, a second '
                              'consecutive close above the $4.75 trigger, which fires the '
                              'political channel 4→5; blank 3 and 4 Aug) and USRFRUSA (DOE '
                              'regular spot, weekly — corroboration; $4.096 for the week of '
                              '27 Jul, the 3 Aug print not yet in the extract or on the EIA '
                              'release page). Data-integrity note: the stale-row check '
                              'clears. The 3 Aug row has refreshed and differs from the '
                              'intraday values published for it (Brent $81.09 against $81.56; '
                              '30Y 5.2274% against 5.2370%; MOVE an actual 80.48 against a '
                              'carried 83.02), so it is a true close and every trigger test '
                              'in this edition runs off it. Four previously dark series '
                              'backfilled this extract: AUTMUSAG and SOFR for 31 Jul, and '
                              'JGLA, MOVE and VIX for 3 Aug. The 27 Feb 2026 anchor was '
                              're-verified field by field and is unchanged.',
               'tier1News': 'CBS News, The National, Euronews, ABC News, CNN, Bloomberg and '
                            'The Hill (the announced 3 Aug talks; Baghaei’s ‘we are not '
                            'negotiating with the United States at this time’ and that Iran’s '
                            'delegation ‘is not going anywhere’; US officials telling CBS '
                            'that no new negotiations are planned; Trump’s account that talks '
                            'were under way ‘at the request of Iran, backed by Saudi Arabia, '
                            'backed by UAE and backed by Qatar’, his ‘last chance to sign a '
                            'good document’, ‘no time constraint’ and ‘every last chance '
                            'before decapitation’ remarks, and his claim the strait could be '
                            'open ‘literally by tomorrow’); The National and ABC News '
                            '(Baghaei on 3 Aug that the strait ‘will in no way return to the '
                            'status it was before February 28th’, that the Oman route is '
                            'temporary and ‘necessary but not sufficient’, and that the '
                            'corridor concept is a single transit route replacing the '
                            'northern and southern ones, with the toll disputed); Al Jazeera '
                            '(Araghchi on 2 Aug that Iran–Oman negotiations are in ‘final '
                            'stages’; Pezeshkian on 3 Aug urging Washington to honour the '
                            'June MoU); Oman Ministry of Foreign Affairs (the 23 Jun joint '
                            'statement establishing a working group — the only signed '
                            'instrument on record); CBS News, The Hill and the Jerusalem Post '
                            '(US/Israeli preparation of strikes on Iranian power plants and '
                            'refineries, Pentagon spokesman Sean Parnell ‘locked and loaded’, '
                            'final orders not given); CENTCOM (no strike release since the 29 '
                            'Jul IRGC strikes; the 28 Jul US–Saudi strikes in Iraq); UKMTO '
                            'via Sharjah24 (the explosion beside a tanker about 20 nm '
                            'north-east of Khasab, reported 2–3 Aug and treated as one '
                            'incident); Kpler via Foreign Policy Journal (106 Hormuz '
                            'crossings by 96 vessels in the week to 2 Aug against 98 the week '
                            'before, 11 on 1 Aug and 9 on 2 Aug, 43 crossings '
                            'route-undetermined against ~49% the prior week), Windward (19 '
                            'crossings and 6 dark on 1 Aug; 1,130 GPS-jammed vessels in the '
                            'Gulf, +173% on the 7-day average) and Lloyd’s List Intelligence '
                            'of 29 Jul (39 transits in the week to 26 Jul against 82, 70% '
                            'untraceable on AIS, inbound Gulf traffic down more than 90%, '
                            'war-risk cover 7.5–10% of hull value); IMF PortWatch via '
                            'straits.live (23 Jul, 10 vessels against an 88/day baseline); '
                            'Reuters, MT Newswires and the US Treasury (the 3 Aug borrowing '
                            'estimates — $739bn for July–September against $671bn projected '
                            'on 4 May, $628bn for October–December, cash balances of $950bn '
                            'and $850bn, $190bn borrowed in April–June with a $919bn end-June '
                            'balance; the 5 Aug refunding statement and the 6 May guidance of '
                            '3Y $58bn / 10Y $42bn / 30Y $25bn); OPEC and Rigzone (the 2 Aug '
                            'JMMC and the 188k b/d September increase with its country split, '
                            'next meetings 6 Sep and 4 Oct); IEA Oil Market Report of 10 July '
                            '(effective OPEC+ spare capacity ~0.17 mb/d); EIA (no new weekly; '
                            'the 29 July print for the week to 24 July stands — crude 404.5 '
                            'mb and ~6% below the five-year average, gasoline 211.3 mb and 7% '
                            'below, distillate ~10% below, refinery utilisation 97.2%, SPR '
                            '307.7 mb after a 3.7 mb draw — with the next release due 5 '
                            'August; and the Gasoline and Diesel Fuel Update showing regular '
                            '$4.096 and on-highway diesel $5.313 for the week to 27 July); '
                            'GasBuddy (national average $4.05 on 3 Aug, −0.8c on the week, '
                            'diesel $5.326, +7.1c); ISM via PR Newswire (July manufacturing '
                            'PMI 55.6 against 54.0 expected, production 58.5, employment '
                            '52.8, prices 71.1); BLS (payrolls 7 Aug, CPI 12 Aug, JOLTS 4 '
                            'Aug); Federal Reserve (the 29 July hold at 3.50–3.75%, 9–3 with '
                            'three dissents for a hike) with Polymarket (~60% on a September '
                            'hike as of 2 Aug; no live CME FedWatch reading for 3–4 Aug was '
                            'sourceable); Reuters via IIR and Maritime Executive (Jizan '
                            'targeted to restart about 15 August); Rudaw and Ynetnews (the '
                            'Islamic Resistance in Iraq’s 7 August deadline and Kataib '
                            'Hezbollah’s 6 August deadline, both following the 28–29 July '
                            'US–Saudi strikes in Diyala).',
               'tier3': 'Press TV reported on 3 August that Kataib Hezbollah says the '
                        'US–Saudi attack ‘made armed struggle necessary’; TASS carried '
                        'Baghaei’s ‘necessary but not sufficient’ formulation. The IRGC claim '
                        'of 31 July to have stopped two US-escorted tankers in the strait '
                        'remains without Tier 1 corroboration and is recorded, not used. '
                        'Corrections and re-verifications this edition: (i) the line that the '
                        'strait ‘will never return to its pre-war state’, attributed to '
                        'Gharibabadi in the 31 July edition and withdrawn as uncorroborated '
                        'on 3 August, is RESTORED on a Tier 1 attribution to Baghaei speaking '
                        'on 3 August; (ii) the Iraqi militia deadline, demoted to Tier 3 on 3 '
                        'August, is now corroborated above Tier 3 — Rudaw for the Islamic '
                        'Resistance in Iraq’s 7 August date and Ynetnews for Kataib '
                        'Hezbollah’s 6 August date, which appear to be distinct ultimatums '
                        'rather than one misreported date; (iii) the report of US/Israeli '
                        'planning against Iranian civilian energy infrastructure, carried on '
                        '3 August as a single-outlet Al Jazeera item, is now corroborated by '
                        'CBS News with a named Pentagon spokesman, but the ‘roughly two-week '
                        'campaign’ duration is NOT corroborated and is dropped — CBS '
                        'describes a weekend-scale window; (iv) a Jerusalem Post live-blog '
                        'entry of 3 August describing a 900 kg bomb dropped on a house in '
                        'southern Iran could not be dated or corroborated and is not used.'},
 'protocol': [{'step': 'Refresh the Bloomberg extract',
               'detail': 'Parse the latest dated row (4 Aug, Tuesday) as intraday; re-map '
                         'columns via the robust scan (front-month CO2/CL2; DXY resolves as '
                         'DXY Index). The stale-row integrity check CLEARS: the 3 Aug row has '
                         'refreshed with true closes that differ from the intraday values '
                         'published for it. Four previously dark series BACKFILLED — AUTMUSAG '
                         'and SOFR for 31 Jul, JGLA, MOVE and VIX for 3 Aug — and one of '
                         'those backfills fired a channel. Currently dark and flagged, not '
                         'carried: JGLA (no 4 Aug print), AUTMUSAG and SOFR (blank 3 and 4 '
                         'Aug), MOVE and VIX (no 4 Aug print).'},
              {'step': 'Recompute deltas',
               'detail': 'd/d vs the 3 Aug close; w/w vs the close five trading sessions back '
                         '(28 Jul this edition); vs-pre-war against the 27 Feb 2026 anchor, '
                         're-verified field by field and unchanged.'},
              {'step': 'Re-evaluate the six channels',
               'detail': 'Market channels move on confirmed closes only. Political stress '
                         'fires 4→5 on the 31 Jul backfill at $4.76 — a second consecutive '
                         'close above the $4.75 trigger. Score rises to 27/30. Oil held at 2 '
                         '(last close $81.09, $13.91 below $95). US inflation held at 5 (5Y5Y '
                         'closed 2.3376%, a fifth consecutive close above 2.30%). Treasury '
                         'held at 5 (30Y 5.2274%, 10Y 4.6755%, both Stage-4 legs on a fourth '
                         'consecutive close; MOVE 80.48). Maritime and escalation are '
                         'event-based and both maxed; the escalation downgrade candidate '
                         'opened last edition is REVOKED because the announced talks did not '
                         'convene.'},
              {'step': 'Reconcile against the prior edition',
               'detail': 'Monday’s US session tracked the Singapore-morning snapshot closely '
                         '— the smallest reconciliation in a fortnight. My 3 Aug intraday '
                         'Brent $81.56 versus the $81.09 close (−$0.47); WTI $78.42 vs $77.90 '
                         '(−$0.52); 30Y 5.2370% vs 5.2274% (−0.96 bp); 10Y 4.6939% vs 4.6755% '
                         '(−1.84 bp); 2Y 4.2456% vs 4.2373% (−0.83 bp); 2s10s +44.62 vs '
                         '+43.41 bp; BE10 2.2787% vs 2.2622% (−1.65 bp); 5Y5Y 2.3367% vs '
                         '2.3376% (+0.09 bp); DXY 99.592 vs 99.897 (+0.305); TTF €56.300 vs '
                         '€57.505; MOVE a carried 83.02 vs an actual 80.48 (−2.54); VIX a '
                         'carried 15.99 vs an actual 15.86.'},
              {'step': 'Update scenarios and watchlist',
               'detail': 'Re-rank catalysts: the 5 Aug refunding statement replaces the '
                         'borrowing estimates as the dated supply test, with the 30Y leg in '
                         'the week of 10 Aug; AUTMUSAG’s next print now tests durability '
                         'rather than direction; whether any US–Iran session convenes at all '
                         'is the gate on the escalation downgrade; the EIA weekly and its SPR '
                         'line land 5 Aug; payrolls 7 Aug and CPI 12 Aug precede the 15–16 '
                         'Sep FOMC; Iraqi militia deadlines 6 and 7 Aug. Mediated pause 12→5, '
                         'full war 34→40 and modal again, contained-but-violent 15→16, '
                         'regional relapse 12→13, deal collapse 27→26.'}],
 'methodology': {'scale': 'Six transmission channels (maritime denial, oil, US inflation '
                          'impulse, Treasury stress, political stress, escalation risk), each '
                          '0–5, summed to 0–30. Bands: 0–7 watch · 8–14 stress · 15–21 '
                          'systemic-risk watch · 22–30 crisis. Market channels move only on a '
                          'confirmed close through a trigger; escalation-risk and maritime '
                          'denial are event-based. Hysteresis: upgrades fire on a sustained '
                          'break, downgrades only on a sustained reversal past a wider '
                          'threshold, deliberately, to avoid whipsawing. This edition is the '
                          'clearest vindication of that rule the monitor has produced. On the '
                          'upgrade side, political stress held at 4 on 3 August with one '
                          'close above its trigger and fires today only because a second '
                          'consecutive close arrived — the identical two-close construction '
                          'that fired US inflation on 31 July. On the downgrade side, the '
                          'escalation channel was NOT moved on 3 August despite a cancelled '
                          'strike package and an announced negotiation, on the stated ground '
                          'that an announcement is not a stand-down; the negotiation then did '
                          'not take place, and a channel moved on that evidence would have '
                          'had to be reversed within a single session — the 25–26 June error, '
                          'repeated in the opposite direction. Event channels are governed by '
                          'hysteresis exactly as market channels are.',
                 'scaleCap': 'Maritime and escalation have been pinned at 5/5 since 10 and 9 '
                             'July, Treasury since 14 July, US inflation since 31 July, and '
                             'political stress joins them today. Only oil, at 2/5, retains '
                             'any upward range — three points in a thirty-point scale. Two '
                             'consequences follow and readers should hold both. First, '
                             'further geopolitical deterioration cannot raise this score; if '
                             'the strike package that CBS reports as awaiting authorisation '
                             'is executed, the number moves only if Brent closes above $95. '
                             'Second, the cap also hides improvement: a genuine de-escalation '
                             'would not lower the score until it had persisted long enough to '
                             'move an event channel off its maximum. A flat 27 from here '
                             'should be read as a saturated scale, not as a stable situation.',
                 'integrity': 'The stale-row check clears: the extract’s 3 August row '
                              'refreshed properly and its closes differ from the intraday '
                              'values published for it (Brent $81.09 against $81.56, 30Y '
                              '5.2274% against 5.2370%, MOVE an actual 80.48 against a '
                              'carried 83.02), so 3 August is a confirmed close and every '
                              'trigger test runs off it. The more consequential finding is on '
                              'the other side of the §9.8 check, which is a two-way test: '
                              'four series flagged as dark in the last edition have '
                              'BACKFILLED — AUTMUSAG and SOFR for 31 July, and JGLA, MOVE and '
                              'VIX for 3 August — and the AUTMUSAG backfill at $4.76 is what '
                              'fires the political channel. A blackout is not a value; it is '
                              'a pending observation, and yesterday’s caveats must be '
                              're-examined rather than carried. Currently dark and flagged '
                              'rather than carried: JGLA has no 4 August print, AUTMUSAG and '
                              'SOFR are blank for 3 and 4 August, and MOVE and VIX printed '
                              'for 3 August but not 4 August. Where third-party sources '
                              'disagree materially — Hormuz counts on different vessel '
                              'universes (Kpler’s all-crossings series is not comparable with '
                              'its commodity-transit series, and neither is comparable with '
                              'Windward’s), the two Iraqi militia deadline dates, and whether '
                              'the Khasab explosion was one incident or two — the '
                              'disagreement is reported rather than resolved by preference, '
                              'and the Bloomberg extract governs for every scored series.',
                 'gasoline': 'Political stress is scored on AUTMUSAG (AAA all-grades retail '
                             'pump; pre-war $3.52, peak $5.18, latest confirmed print $4.76 '
                             'on 31 July — backfilled in this extract and the second '
                             'consecutive close above the $4.75 trigger, following $4.76 on '
                             '30 July and exactly $4.75 on 24, 27, 28 and 29 July — with 3 '
                             'and 4 August blank). USRFRUSA (DOE regular spot; pre-war '
                             '~$2.94, peak $4.50, latest $4.096 for the week of 27 July) is '
                             'tracked alongside as corroboration only; the weekly print due 3 '
                             'August has not appeared in the extract or on the EIA release '
                             'page. Neither series is re-based. GasBuddy’s independently '
                             'published national average ($4.05 on 3 August, down 0.8 cents '
                             'on the week, with diesel up 7.1 cents to $5.326) is used only '
                             'as an external cross-read, and its attribution of product '
                             'strength to Ukrainian strikes on Russian refining is noted '
                             'because it is a non-Hormuz driver of the same scored series. '
                             'EIA’s on-highway diesel, up 17.9 cents in the week to 27 July '
                             'against gasoline’s 9.5, is noted for the same reason: the '
                             'binding constraint on the pump is refining capacity rather than '
                             'crude.',
                 'anchor': 'Brent $72.48; WTI $67.02; 2Y 3.375%; 5Y 3.502%; 10Y 3.938%; 30Y '
                           '4.611%; 2s10s +55.64 bp; 5Y5Y 2.142%; 10Y BE 2.257%; MOVE 73.38; '
                           'VIX 19.86; DXY 97.608; gasoline (AAA) $3.52; Henry Hub $3.06; TTF '
                           '€31.23; Asia LNG ¥1,669. (Re-verified field by field — '
                           'unchanged.) Brent +13.0%, WTI +17.4%, TTF +86.6%, Asia LNG '
                           '+105.0%; the 30Y (+62.2 bp), 10Y (+74.8 bp), 5Y5Y (+19.6 bp), 10Y '
                           'breakeven (+0.3 bp), MOVE (+7.10) and DXY (+2.40) sit above their '
                           'anchors; VIX (−4.00) and Henry Hub (−9.6%) remain below pre-war.',
                 'intraday': 'The latest dated row is a Singapore-AM snapshot and US hours '
                             'set the close. This edition is the counter-example to the last '
                             'one: Monday’s closes came in 47 cents below my Brent print and '
                             'within two basis points across the curve, where Friday’s had '
                             'been $1.97 and 7.59 bp above it. The error in the snapshot is '
                             'regime-dependent rather than random — it is large when the US '
                             'session has something to trade and small when it does not — so '
                             'a small gap is evidence about the session, not evidence that '
                             'the method has improved. Recent Brent gaps between my snapshot '
                             'and the subsequent close: +$3.10, −$1.81, −$2.01, −$3.32, '
                             '−$0.84, +$1.97, −$0.47. CL2 remains an artifact against active '
                             'CLA, and with the September Brent contract expired the '
                             'front-month/active gap prints $2.71 in this morning’s snapshot; '
                             'the scored CO2 continuation series is unaffected. Triggers are '
                             'evaluated on confirmed closes; escalation-risk and maritime '
                             'denial are event-based. Restated-series levels are not '
                             'comparable with pre-restatement editions, though the '
                             'directional analysis is continuous.'}}


with open("editions.json", "w") as f:
    json.dump(EDITIONS, f, indent=2, ensure_ascii=False)

print("Wrote editions.json with full sections for:", list(EDITIONS.keys()))
