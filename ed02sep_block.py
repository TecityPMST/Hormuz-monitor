# -*- coding: utf-8 -*-
"""Full section-by-section content of the 2 SEPTEMBER 2026 edition.
Copied from that edition's PDF build fragments (build/ed_*02sep.py, build/an_a*_02sep.py).
Edit here, never editions.json."""

ED02SEP = {
"label": "2 Sep 2026",
"editionLine": "Daily edition · 2 Sep 2026 intraday · Bloomberg · Singapore 2 Sep AM update",
"score": 27,
"band": "CRISIS",
"sequencing": " → ".join(["27"]*17),
"sessionNote": "Score held for a seventeenth edition · no channel moved · and the day's finding is that the largest open fact on the board was closed inside twenty-four hours and the instrument could not register the closing. CENTCOM delivered the promised retaliation and published it; Iran answered against three countries in one night; and the only channel with headroom moved toward its trigger just as the trigger stopped being well-defined.",

"headline": (
 "Score HOLDS at 27/30 for a seventeenth consecutive edition. No channel moved. The largest open fact on the board was closed "
 "inside twenty-four hours, and the instrument could not register the closing. "
 "ONE. The retaliation was delivered and it is on the FORMAL record. CENTCOM published a release on 1 September — its first of any "
 "kind in seventeen days and its first on strikes inside Iran in thirty-four — recording a wave against IRGC air-defence, radar, "
 "maritime, mine-laying and communications targets. Iran answered the same night against THREE countries at once: Jordan, Bahrain "
 "and Kuwait. That is a widening of the war's GEOGRAPHY, and the first window in which Bahraini and Kuwaiti authorities have "
 "acknowledged engaging incoming Iranian fire. "
 "TWO. Both sides' own accounts are weaker than their claims. CENTCOM published no target list and no damage assessment; asked about "
 "civilian casualties its spokesman said only that the US military 'never targets civilians', a non-denial, while the Iranian Red "
 "Crescent puts four dead including a child at a wedding in Kuhestak. Jordan's armed forces now concede leakers — 13 engaged, 10 "
 "intercepted, 3 fell — where a day earlier Petra had said eight were intercepted and gave NO launch total. Two attacks, two "
 "counting bases; 8 and 13 are not a pair. "
 "THREE, and it is the most consequential thing here for the monitor itself: the only channel with headroom moved toward its "
 "trigger, and the trigger stopped being well-defined. Brent CO2 closed $91.57, +$3.20, leaving the $95 upgrade $3.43 away — the "
 "second-narrowest of eleven readings. But the ACTIVE contract closed 35 cents short at $94.65 and printed $96.64 on Wednesday "
 "morning, THROUGH the level. On that live mark the trigger sits BETWEEN the two series, and §9.36 forbids reading them as one "
 "across the 31 August roll. That is now the largest open methodological problem in this document (§9.56). "
 "FOUR. A BEAR FLATTENER — the inverse of Monday — took the 2-year to 4.3998%, a war-high close and its first since 23 July, with "
 "the 5-year and 10-year making theirs again. The front end set its record on the day America bombed Iran, and BE10 carried 3.74 bp "
 "of the 10-year's 4.81: compensation, not real yield. A Fed trade wearing a Gulf jacket. Threshold B held a THIRD close at its "
 "widest margins — the 30-year leg PROVISIONAL under §9.35 — and 5y5y went back ABOVE 2.30%, ending the break. "
 "Sequencing 27 → 27 → 27. Five of six channels are at the cap. The score could register NEITHER an American strike wave inside "
 "Iran NOR an Iranian answer against three countries in one night."),

"tape": {
 "note": ("Scoring reference is the 1 September close (Tue); the 2 September row is a Singapore-MORNING mark taken BEFORE the US cash "
   "session and moves no channel. §9.35 FIRES on the 30-year: its 1 September close is IDENTICAL to four decimals to the intraday "
   "this document published for that day, so the field is UNRESOLVED even though the row around it is demonstrably live. §9.8 and "
   "§9.41 CLEAR. The 2 September US session had not begun at the cut: the Beige Book, the WPSR, the 2 Sep cash-management buyback "
   "announcement and any American answer to Tuesday night are PROSPECTIVE, not unobtained. Every row below carries the Bloomberg "
   "ticker it is drawn from; tickers come from the extract's own header scan and are never hardcoded. No price in this document is "
   "taken from the web — screen quotes for 'Brent' on 1–2 September refer to the ACTIVE contract and are not the scored series. "
   "(W) on a cell marks a vendor restatement — here the 31 August COA restatement."),

 "oilGasHeader": ["Series", "BBG ticker", "28 Aug", "31 Aug", "1 Sep close", "2 Sep intr.", "Trigger note"],
 "oilGas": [
  ["Brent, front-month listed — scored", "CO2 Comdty", "88.10", "88.37", "91.57", "93.01",
   "+$3.20, the largest one-day rise since 10 August. $3.43 from the $95 upgrade, NARROWED from $6.63 — the ELEVENTH reading and the SECOND-NARROWEST of the war, behind $3.03 (21 Aug). Seven narrowings in ten transitions. $19.09 above the $72.48 downgrade, WIDENED. The scored rule is written on THIS series."],
  ["Brent, active contract", "COA Comdty", "88.10 (W)", "90.49", "94.65", "96.64",
   "Closed 35 cents SHORT of $95, then went THROUGH it on the 2 Sep mark, $1.64 above — and it is NOT the scored figure. Basis to CO2 is 2.12, 3.08, 3.63: WIDENING, not stepping, so the roll is clean and this is a real term-structure move. On the live mark the $95 trigger sits BETWEEN the two series. §9.36 forbids reading them as one. See §2.1."],
  ["WTI, front-month listed — scored", "CL2 Comdty", "81.83", "84.06", "87.75", "89.18",
   "+$3.69. The two crude legs moved together this session, unlike 31 August. NO trigger is written on WTI; it is corroboration."],
  ["WTI, active contract", "CLA Comdty", "83.40", "85.76", "90.22", "91.86",
   "Basis to CL2 of 1.57, 1.70, 2.47, 2.68 — no sign change, no step, but WIDENING on the same shape as Brent's. Both prompt structures steepened into the strikes."],
  ["Henry Hub natural gas", "NGA Comdty", "2.888", "2.935", "2.904", "2.953",
   "−$0.031. 5.19% BELOW its $3.063 anchor, WIDENED back out from 4.18%. The control in the experiment turned negative again in one session: American gas did NOT follow American crude."],
  ["Dutch TTF natural gas", "TZTA Comdty", "66.979", "69.809", "72.218", "74.685",
   "A NEW WAR-RECORD CLOSE, +€2.409, taking out €69.809 (31 Aug) — the THIRTEENTH of the war and the SECOND on consecutive sessions. +131.3% vs pre-war. The 2 Sep intraday is higher again and is NOT a record."],
  ["Japan/Asia LNG", "JGLA Comdty", "3,785", "3,761", "3,785", "no print",
   "+24, the SECOND-highest close of the war, 8 yen off the 3,793 high of 25 August. +126.8% vs pre-war. No 2 Sep print."],
 ],

 "ustNote": ("Basis points. A BEAR FLATTENER, falling monotonically with tenor — the exact inverse of 31 August. Three new war-high "
   "closes, and the 2-year's is its first since 23 July. The 30-year leg of that shape is contingent: §9.35 leaves its close "
   "unresolved. No trigger is written on the 2-year or the 5-year."),
 "ustHeader": ["Tenor", "BBG ticker", "28 Aug", "31 Aug", "1 Sep close", "2 Sep intr.", "d/d, bp", "Trigger note"],
 "ust": [
  ["2-year", "USGG2YR Index", "4.3434", "4.3415", "4.3998", "4.4060", "+5.83",
   "A NEW WAR-HIGH CLOSE, taking out 4.3470 of 23 July — the only tenor whose prior high still dated from July — and the LARGEST move on the curve. The front end set its record on the day the US bombed Iran. NO trigger is written on the 2-year."],
  ["5-year", "USGG5YR Index", "4.4789", "4.5002", "4.5551", "4.5658", "+5.49",
   "A NEW WAR-HIGH CLOSE for a THIRD consecutive session. NO trigger is written on the 5-year."],
  ["10-year", "USGG10YR Index", "4.7180", "4.7500", "4.7981", "4.8102", "+4.81",
   "A NEW WAR-HIGH CLOSE for a SECOND consecutive session. SATISFIES Threshold B's 4.65% leg by 14.81 bp, its widest of the regime. BE10 carried 3.74 of this 4.81 — compensation, not real yield."],
  ["30-year", "USGG30YR Index", "5.2056", "5.2423", "5.2730", "5.2868", "+3.07",
   "§9.35 UNRESOLVED — identical to four decimals to the published 1 Sep intraday, so both this close and its d/d are provisional. The SMALLEST move on the curve as printed. THIRD-highest close of the war (5.3060, 17 Aug; 5.2826, 18 Aug); the ELEVENTH close above 5.24. CLEARS B's 5.20% by 7.30 bp from 4.23. Downgrade leg fails by 27.30 bp, WIDENED from 24.23."],
  ["2s10s spread", "USYC2Y10 Index", "37.049", "40.635", "39.414", "40.206", "−1.221",
   "A FLATTENING, and it corroborates the curve shape INDEPENDENTLY of the unresolved 30-year. 16.226 bp flatter than the 55.64 anchor. A SEPARATE series, not the difference of the printed generics."],
  ["10-year breakeven", "USGGBE10 Index", "2.3179", "2.3206", "2.3580", "2.3588", "+3.74",
   "10.11 bp above its 2.2569 anchor, WIDENED sharply from 6.37 — the widest since 8 August. It moved the SAME way as the 5y5y this session, having disagreed on 31 August."],
  ["5y5y forward breakeven", "USGG5Y5Y Index", "2.2964", "2.2885", "2.3110", "2.3119", "+2.25",
   "BACK ABOVE the 2.30% firing level by 1.10 bp, ENDING the break at two closes — the last edition asked whether a third would come and it did not. 16.90 bp above the 2.142% downgrade anchor, WIDENED from 14.65. §9.26 no longer engaged here, newly engaged on oil (§9.56)."],
 ],

 "crossHeader": ["Series", "BBG ticker", "31 Aug", "1 Sep close", "vs pre-war", "Note"],
 "cross": [
  ["Treasury volatility (MOVE)", "MOVE Index", "75.32", "77.88", "+4.50 vs 73.38",
   "+2.56, a SECOND consecutive close above 75 and the HIGHEST since 77.92 on 11 August. The Treasury volatility downgrade leg is LOST for a second session and is now moving away rather than lapsing. No 2 Sep print."],
  ["Equity volatility (VIX)", "VIX Index", "14.92", "16.34", "−3.52 vs 19.86",
   "+1.42 — but still 3.52 points BELOW the pre-war anchor. Equities repriced the war on the day of the strikes and remain calmer than before it began. No 2 Sep print."],
  ["US dollar index", "DXY Index", "99.428", "99.677", "+2.07 vs 97.608",
   "+0.249, a third consecutive session of dollar strength into the strikes. The label resolves as DXY Index, NOT DXY Curncy — header scan every edition, never hardcoded."],
  ["SOFR overnight rate", "SOFRRATE Index", "3.68", "no print", "+0.00 vs 3.68",
   "BACKFILLED at 3.68 for 31 August, which the last edition reported DARK. It is the HIGHEST print since 17 August and exactly on the 27 February SOFR fix of 3.68 — a reference used here but not among the seventeen anchor fields. Dark again on 1 and 2 Sep."],
  ["Gasoline, AAA all-grades retail pump — scored", "AUTMUSAG Index", "4.83", "no print", "+1.31 vs 3.52",
   "BACKFILLED UP — the last edition reported 31 Aug DARK with $4.81 (28 Aug) as last resolved. $4.83 equals the 25–26 August prints and is the joint-highest since 5 June; the war high is $5.18 (20 May) and this is nowhere near it. 23 cents above the $4.60 condition and 8 above the $4.75 that fired the upgrade, and moving AWAY."],
  ["Gasoline, DOE regular retail spot — corroboration", "USRFRUSA Index", "4.071", "no print", "+1.13 vs ~2.94",
   "BACKFILLED for the 31 August survey at $4.071, −1.4c on the 24 August $4.085. Weekly, surveyed Monday. The 2 Sep EIA release is PROSPECTIVE."],
 ],

 "gasChartNote": ("AAA all-grades (AUTMUSAG Index, navy, the scored series) against DOE regular retail (USRFRUSA Index, amber, weekly, "
   "corroboration only); the dotted line marks the $4.75 upgrade trigger, NOT the $4.60 downgrade condition. The scored series has "
   "printed at or above $4.75 on every session for which it has printed since 12 August. Both lines now END on 31 August — at $4.83 "
   "and $4.071 respectively, both BACKFILLED this edition — and neither is extrapolated through the dark 1 and 2 September cells. "
   "THREE retail series, never compared: AUTMUSAG last RESOLVED at $4.83; USRFRUSA at $4.071; and AAA's own published headline, read "
   "direct 2 September on a page stamped 'price as of 9/1/26', at regular $4.0954 and diesel $5.6325. The two AAA fuels are diverging "
   "on the WEEK and MONTH, not on the day: both rose on the day, regular +1.47c and diesel +3.23c, but regular is down on the week and "
   "the month while diesel is +27.09c on the month and +$1.9418 on the year. Diesel sits 18.34 cents below its all-time record of "
   "$5.8159 of 19 June 2022 — four years before this war, and never to be called a war high."),

 "straitHeader": ["Strand", "State on 2 September", "Source"],
 "strait": [
  ["UKMTO / incidents / mines",
   "JMIC UPDATE 092 OBTAINED as a primary PDF, ICOD 011500 UTC. The count MOVED for the first time in three issues: 100 incidents since 1 March, THREE since the last report, against 97 and NIL, and two of the three are NAMED. The mine language is materially UNCHANGED but its TAGGING is not: §2B still records 'mine danger areas still active' and §5B continuing clearance, but only §5B carries the '(No change)' flag where 091 flagged BOTH — a change in presentation, NOT in substance, and not written as one. Threat levels UNCHANGED; Hormuz SEVERE. Warnings 125-26 onward NOT FOUND on five varied methods; 124-26 remains the highest corroborated anywhere.",
   "JMIC 092 primary PDF, read 2 Sep; UKMTO Warnings 120-26 to 124-26"],
  ["Transits + blockade",
   "JMIC 092 §4C: 39 US NCAGS-FACILITATED transits over 30–31 Aug (48h) against a stated ~138/day 2025 baseline. Those are DIFFERENT universes; the only like-for-like reading is against 091's own facilitated count, 19.5/day against 21.7/day, so the facilitated series FELL. Its annex, now SPLIT into cargo and tanker tables, totals SEVEN for the identical 48 hours on a non-facilitated denominator — 39 and 7, one publication, not blended. Kpler via Reuters: ~5 vessels on 31 Aug against its own ~14 average, and NO laden liquid tankers. Lloyd's List: 108 transits 17–23 Aug, +27% w/w, cargo vessels over 10,000 dwt — this WITHDRAWS the 114 / +30% previously carried. CENTCOM's 82 / 3 / 2 is STILL data-dated 29 August — a THIRD edition unchanged, pre-dating both the strike wave and Iran's answer.",
   "JMIC 092 §4C and annex; Kpler via Reuters 1 Sep; Lloyd's List brief 27 Aug"],
  ["CENTCOM / kinetic",
   "THE RETALIATION WAS DELIVERED AND ANSWERED INSIDE TWELVE HOURS. CENTCOM public release, 1 Sep: a wave against IRGC air-defence, radar, maritime, mine-laying and communications targets from 12:00 EDT — its FIRST formal release in 17 days and first on Iran in 34. NO target list and NO BDA; impact points are Iranian-sourced (Konarak, Bandar Abbas, Qeshm, Jiroft, Kuhestak). Iranian Red Crescent via AFP: four dead including a child at a wedding in Kuhestak; CENTCOM's Capt. Hawkins answered only that the US 'never targets civilians'. Iran answered against JORDAN, BAHRAIN and KUWAIT. Jordan's armed forces, 2 Sep: 13 engaged, 10 intercepted, 3 fell, no casualties — a DIFFERENT attack from 30–31 Aug, never to be merged with its eight. Two US officials to Reuters: NO American casualties, contradicting the IRGC's Camp Titin claim.",
   "centcom.mil release 1 Sep; JAF via AFP 2 Sep; Reuters, AFP, ABC, Stars and Stripes 1–2 Sep"],
  ["Diplomacy + economic war",
   "IRAN PUT THE STRAIT ON THE TABLE ON THE DAY IT WAS BOMBED, AND WASHINGTON REFUSED IT THE SAME NIGHT. Pezeshkian at the SCO summit, 1 Sep: if the US 'returns to its commitments under the aforementioned memorandum… Iran will immediately reciprocate'. Trump to Fox the same evening: an agreement with Iran 'isn't worth the paper it's written on'. Qatar's MFA confirmed it is working with Oman and Pakistan, and that Iran wants a US return to the June MoU BEFORE any temporary route. Against it, Speaker Ghalibaf: Iranian forces remain 'in complete control of the strait and will not allow it to be opened' and ships taking the southern route 'are being targeted' — TIER 3, recorded and not used to attribute the tanker strikes. NO OFAC action and NO Iran-related Treasury release 29 Aug – 2 Sep; still NO Chinese bank.",
   "Reuters, Al Jazeera, ABC, AFP 1–2 Sep; ofac.treasury.gov and home.treasury.gov read direct 2 Sep"],
 ],
},

"analysis": {
 "intro": ("The scoring reference is the 1 September close; the 2 September row is a Singapore-morning mark taken before the US cash "
   "session and moves no channel. §9.35 fires on the 30-year, so its close, its day-on-day change and Threshold B's margin are all "
   "published as PROVISIONAL — though the B conclusion is bounded by the live 2 September mark."),
 "bondYieldNote": ("Six channels. Five sit at the cap, so the scale can register neither the delivery of a promised American strike wave "
   "inside Iran nor an Iranian answer against three countries in one night. The sixth — oil — is the only one with headroom, and this "
   "edition had to declare its trigger ill-defined."),
 "bondYield": [
  {"title": "(i) Maritime denial — held at 5 (max). The incident count moved for the first time in three issues, and two of the three missing incidents turned out to have names.",
   "text": ("The downgrade requires a verified reopening AND traffic above 25% of normal for ten sessions. Neither leg advanced. JMIC "
     "Update 092, ICOD 011500 UTC and obtained as a primary PDF, keeps the Strait of Hormuz at SEVERE and every other regional threat "
     "level unchanged. One presentational change is worth stating precisely because it is easy to over-read: 091 flagged BOTH its mine "
     "passages '(No change)', while 092 flags only the clearance passage and leaves the 'mine danger areas still active' sentence "
     "untagged. The WORDS are materially the same. That is a change in tagging, not in substance, and nothing is inferred from it. "
     "The count moved, and the reconciliation the last edition could not close has closed itself: 092 records 100 incidents since 1 "
     "March and THREE since the last report, against 97 and NIL. The three are the ones this document was carrying as unreconciled — "
     "the BURGAN, hit on the starboard aft ballast tank and anchored a mile north-west of Jazirat Um Al Ghanam, which is Warning "
     "122-26 given a name for the first time; the vessel behind Advisory 123-26, name withheld, which JMIC classes as 'suspected U.S. "
     "blockade enforcement' after a military aircraft put a round in the water alongside it and ordered it to reverse course; and the "
     "SENEGAL PROSPERITY, struck by three rockets in the engine room and ballast tank, all communications lost, dead in the water, "
     "listing to port and not under command. A second VLCC, the Saudi-flagged Bahri vessel SIDR, was struck minutes earlier per "
     "Marisks and Reuters and is NOT separately itemised in the 100. Each had loaded two million barrels of Saudi crude at Juaymah. "
     "JMIC's date column conflicts with UKMTO's own report times on two of the three; the reading taken here is that JMIC dates the "
     "PRODUCT and UKMTO dates the INCIDENT, and both sets are printed rather than reconciled. The facilitated series FELL: 092 reports "
     "39 US-facilitated transits over the 48 hours of 30–31 August, which is 19.5 a day against the 21.7 a day implied by the 65 over "
     "72 hours in 091 — on the same denominator, the only like-for-like comparison available anywhere in this record. Its own annex "
     "totals seven for the same 48 hours on the non-facilitated denominator, and Kpler has about five on 31 August with no laden liquid "
     "tankers. The monitor does not average them and does not read a facilitated count as safety: it counts vessels the US Navy is "
     "shepherding, which measures escort activity, not a functioning waterway.")},
  {"title": "(ii) Oil price shock — held at 2. The channel came within $3.43 of its upgrade on the scored series and went through the level on the active one. The rule can no longer tell which.",
   "text": ("Brent CO2 closed $91.57 on 1 September, +$3.20 and the largest one-day rise since 10 August, leaving the $95 upgrade $3.43 "
     "away — NARROWED from $6.63. The sequence is now 9.78, 8.43, 5.55, 5.21, 3.03, 7.73, 8.06, 6.48, 6.90, 6.63, 3.43: ELEVEN "
     "readings, SEVEN narrowings and three widenings across ten transitions, and $3.43 is the SECOND-NARROWEST of the war behind $3.03 "
     "on 21 August. The downgrade leg moved the other way to $19.09 above $72.48. And here is the problem. The active contract closed "
     "$94.65, just 35 cents short, and then printed $96.64 on Wednesday morning — THROUGH the level the rule names, and $1.64 above "
     "it, on the same morning the scored continuation sits $1.99 below it. On the live mark the trigger level now sits BETWEEN the two "
     "series. The basis between them ran 2.12, 3.08 and 3.63 across three sessions: it is WIDENING smoothly rather than stepping, "
     "which is the signature of a genuine term-structure move and confirms the 31 August roll was clean. But it means the two series "
     "are now more than three and a half dollars apart and diverging, and §9.36 forbids constructing anything across them. The trigger "
     "says 'Brent above $95 sustained' and, on the live mark, there are now two defensible answers to whether it is being approached "
     "or exceeded. The rule was written when the basis was exactly zero for twenty sessions and the question did not arise. It is NOT "
     "resolved here, and the rule is NOT moved to whichever series would fire it — that is precisely the discipline §9.26 exists to "
     "enforce, and the same discipline that has held the 5y5y rule in place. The channel holds at 2 on the scored continuation. This "
     "is now the largest open methodological problem in the document (§9.56), ahead of the 5y5y gap and ahead of §9.49, and it will be "
     "decided within days rather than weeks. What moved the price: both crude legs moved together for once, WTI +$3.69 against Brent's "
     "+$3.20, on a session whose news was an American strike wave inside Iran and an Iranian answer against three countries. But the "
     "American gas leg went the OTHER way — Henry Hub fell three cents and its discount to pre-war WIDENED back out from 4.18% to "
     "5.19%, while TTF set a thirteenth war-record close at +131.3%. The complex is still pricing a chokepoint rather than a shortage, "
     "and the divergence between the two gas markets is the cleanest evidence in this document that it is doing so.")},
  {"title": "(iii) US inflation impulse — held at 5 (max). The trigger came back, and it came back on the war rather than on the Fed.",
   "text": ("The break ended at two. The 5y5y forward closed 2.3110% on 1 September, +2.25 bp and back ABOVE the 2.30% level whose "
     "sustained break fired this channel 4→5 on 31 July. The last edition asked directly whether a third consecutive close below 2.30% "
     "would come. It did not. The break stands at two closes, 28 and 31 August, and joins the one-session breaks of 13 and 25 August "
     "as an episode rather than a regime. The score holds and the rule was never moved, which is the point. Had this document "
     "redefined the downgrade to the firing level during the two-close break — the thing §9.26 forbids and the thing the last two "
     "editions were under most pressure to do — it would now be unwinding that change. The documented downgrade remains a sustained "
     "close at or below the 2.142% pre-war anchor, and the distance WIDENED to 16.90 bp from 14.65. BE10 moved the SAME way this "
     "session, +3.74 bp to 10.11 bp above its own anchor, having disagreed with the 5y5y on 31 August. The two compensation measures "
     "agreeing is a stronger reading than either alone. And the composition changed. On 28 August the Treasury selloff was real yield "
     "outright — BE10 FELL while nominals rose — and on 31 August compensation contributed only 0.27 bp of the 10-year's 3.20. On 1 "
     "September BE10 carried 3.74 basis points of the 10-year's 4.81, leaving barely a basis point of real yield. That is compensation "
     "rather than real yield — the residual on a nominal, which is not the same thing as term premium and is not called that — and it "
     "arrived on the session the United States bombed Iran and Iran answered against three countries. The physical impulse behind it "
     "is undiminished and pointing the same way: TTF at a war-record close, Asia LNG +126.8%, diesel +$1.9418 year on year and now "
     "diverging from gasoline. The honest statement is that this channel spent two sessions scored at its maximum on a trigger that "
     "had failed, and is no longer in that position. It was not rescued by a rule change.")},
  {"title": "(iv) Treasury stress — held at 5 (max). Three war-high closes, a war high at the front end for the first time since July, and a 30-year the integrity test will not certify.",
   "text": ("§9.35 fires, and it fires on the leg that matters. The 30-year's 1 September close of 5.2730% is IDENTICAL to four decimal "
     "places to the intraday this document published for 1 September. Under §9.35 that field is UNRESOLVED regardless of the row "
     "around it — and the row is demonstrably live, since thirteen of fourteen scored fields moved and MOVE, VIX and Asia LNG all "
     "printed where the snapshot was blank. So the 30-year close, its +3.07 bp change and Threshold B's 7.30 bp margin are all "
     "published as PROVISIONAL. The CONCLUSION is nonetheless bounded and safe: whatever the true close, the 2 September intraday "
     "prints 5.2868%, so the 30-year clears B's 5.20% on both the possibly-stale close and the live mark. What is genuinely contingent "
     "is the CURVE SHAPE — if the true close is higher, the flattener is less pronounced at the long end than printed. The front of it "
     "is not contingent: 2-year +5.83, 5-year +5.49, 10-year +4.81 is monotonic on three clean fields, and the 2s10s series confirms "
     "the flattening independently at −1.221. The war highs: the 2-year closed 4.3998%, taking out 4.3470% of 23 July — its first "
     "war-high close since 23 July, and the largest move on the curve. The 5-year made its THIRD consecutive war-high close and the "
     "10-year its second. The front end setting its record on the day American forces bombed Iran is the single most counter-intuitive "
     "fact in this edition, and it is not a Gulf trade — it is the Fed. Barr was REPORTED as telling an audience the same day that the "
     "Board should be prepared to raise if inflation does not subside — only the dovish conditional is available verbatim — and "
     "Polymarket's September board has a 25 bp hike at 56.5% against a hold at 42.5%, the hike having gained 23 points in a week. The "
     "downgrade is further away on both legs and §9.15 does not fire for a FOURTH consecutive session. MOVE closed 77.88, +2.56, a "
     "SECOND consecutive close above 75 and the highest since 77.92 on 11 August, so the volatility leg is not merely lost but moving "
     "away; the yield leg widened from 24.23 to 27.30 bp, itself PROVISIONAL. Both legs deteriorated together for the fourth session "
     "running — the FIFTH occurrence of that third state and its FOURTH consecutive one. US-inflation is STILL the nearer of the two "
     "market downgrade candidates but the gap NARROWED for the first time in three editions, to 16.90 against 27.30 from 14.65 against "
     "24.23: both moved away, and Treasury moved away faster. The ORDERING is not provisional, because 16.90 is nearer than 24.23 on "
     "either reading.")},
  {"title": "(v) Political stress — held at 5 (max). The scored series backfilled UP to the top of its recent range, and the two retail fuels have come apart on the month.",
   "text": ("The state is RESOLVED and it moved the wrong way for a downgrade. AUTMUSAG's 31 August cell, reported DARK yesterday, has "
     "printed at $4.83 — two cents ABOVE the $4.81 this document was carrying as last resolved, and equal to the $4.83 of 25–26 "
     "August, the joint-highest print since 5 June. It is NOT a war high — $5.18 on 20 May stands — and calling it one would be "
     "exactly the unsorted superlative §9.32 forbids. It did not print on 1 or 2 September. The last resolved value is therefore "
     "$4.83, 23 cents above the named $4.60 downgrade condition and 8 above the $4.75 that fired the upgrade. §9.10 is vindicated a "
     "THIRD time and in the opposite direction to the last: 14 August backfilled UP and destroyed a downgrade case, 1 September "
     "backfilled DOWN by a cent, and this one backfilled UP. None was predictable from the run, which is exactly why §9.30 forbids "
     "reading a trend through dark cells. DOE's weekly series also backfilled, at $4.071 for the 31 August survey, 1.4 cents BELOW the "
     "24 August $4.085. The two retail backfills point OPPOSITE ways on the same week. Neither is the other's check; they are "
     "different surveys of different products. The corroborating series has diverged, and that is the new information. AAA's own page, "
     "read 2 September and stamped 'price as of 9/1/26', has regular at $4.0954 and diesel at $5.6325. Both rose on the day — regular "
     "+1.47c and diesel +3.23c — but regular is DOWN 0.15 cents on the week and 0.59 on the month while diesel is UP 1.26 cents on the "
     "week and 27.09 on the month. The prior-day row on that page reproduces exactly what this document published yesterday, so the "
     "series rolled cleanly and no restatement occurred. Diesel now sits 18.34 cents below its all-time record of $5.8159 of 19 June "
     "2022 — four years before this war, and never to be described as a war high. The political instrument produced nothing. The "
     "President met nearly a dozen refiners and distributors with the Interior and Energy Secretaries on 1 September, closed to press, "
     "on refining capacity and pass-through. No readout, no deliverable and no announced measure could be obtained from eight outlets. "
     "Specifically: no SPR release, no export restriction and no price control. It is recorded because a policy response to the pump is "
     "the transmission this channel exists to detect, and because an announced meeting that produces nothing is itself a reading.")},
  {"title": "(vi) Escalation risk — held at 5 (max). America struck Iran, Iran struck three countries back, and the score moved by zero points.",
   "text": ("The downgrade requires a mediated stand-down and resumed talks. Instead, at 12:00 EDT on 1 September, CENTCOM executed the "
     "wave Trump had promised on 31 August, and published it: IRGC air-defence, radar, maritime, mine-laying and communications "
     "targets. Iran answered within hours against Jordan, Bahrain and Kuwait, with the IRGC spokesman saying Iran 'will no longer "
     "exercise restraint regarding Bahrain and Kuwait'. Jordan's armed forces put the answer on the record at 13 engaged, 10 "
     "intercepted and 3 fallen. The scale is saturated and this is the sharpest case of §9.7 the war has produced. Escalation has been "
     "at 5/5 since 9 July. The delivery of a promised American strike wave inside Iran, the breaking of a seventeen-day silence in "
     "CENTCOM's formal record and a thirty-four-day one on strikes inside Iran, an Iranian answer against three countries in one "
     "night, the first Bahraini and Kuwaiti air-defence engagements of the war to be officially acknowledged, and four Iranian "
     "civilians reported killed at a wedding, together move the total by ZERO. A flat 27 does not mean a stable week. It means the "
     "instrument is at its stop, and the only channel that could move needs a rule this edition has just had to declare ill-defined. "
     "Three disciplines applied. The IRGC's Camp Titin and Prince Hassan casualty claims are Tier 3 and contradicted by two US "
     "officials to Reuters — the JAF's 'no casualties' does NOT reach them, since it speaks to Jordanian casualties, not American "
     "ones, and the contradiction rests on a single outlet. They are not used. The 30–31 August Jordan attack and the 1–2 September "
     "one are DIFFERENT EVENTS on different counting bases — eight INTERCEPTED with no launch total from Petra, and ten intercepted of "
     "thirteen ENGAGED — and any running total that merges them is wrong (§9.13). And against under-reading: Iran offered reciprocity "
     "at the SCO on the day it was bombed, Qatar is mediating with Oman and Pakistan, and the exchange as executed was BOUNDED — one "
     "wave each, both sides declaring it complete. That restraint is real and is why the full-war line moves ten points and not thirty.")},
 ],
 "stage4Note": ("Three thresholds, reported separately from the score. A remains untestable as written; B held a third close at the widest "
   "margins of the regime, with its 30-year leg provisional under §9.35; C is not armed but has reversed direction."),
 "stage4": [
  {"title": "Threshold A · a failed-auction test — UNTESTABLE AS WRITTEN, THEREFORE NOT ARMED ON THE RECORD (§9.39)",
   "text": ("The test needs a when-issued level Treasury does not publish, so it cannot RETURN a state and is carried as unarmed rather "
     "than as satisfied. NO coupon auction CLEARED in the window. Treasury auctioned 4-, 6-, 8-, 17- and 52-week BILLS on 1 September, "
     "which are not a Threshold A input, and their results were NOT RETRIEVED — TreasuryDirect serves them from a client-rendered "
     "page. The five-auction primary-dealer run on competitive-accepted is unchanged at 12.34, 2.09, 10.90, 10.05 and 12.264, and "
     "12.264% remains the SECOND-highest of those five. OPEN FOR A THIRD CONSECUTIVE EDITION: Treasury release SB0607 of 19 August "
     "promised an updated tentative buyback schedule for the $2bn→$4bn regime that starts 9 SEPTEMBER. The live schedule PDF is STILL "
     "stamped 5 August, with the 10 September operation STILL capped at $2 billion. Seven days out, the operating calendar for the "
     "announced regime has not been published on the canonical page, re-fetched this edition. Two CASH-MANAGEMENT buybacks of up to "
     "$12.5bn each sit on the same schedule and are a DIFFERENT instrument in a different sector; see the annex.")},
  {"title": "Threshold B · 30-year above 5.20% WITH 10-year above 4.65% — ARMED, and it HELD a THIRD close at the WIDEST margins of the regime",
   "text": ("30-year 5.2730% clearing by 7.30 bp, from 4.23 and 0.56; 10-year 4.7981% clearing by 14.81 bp, from 10.00 and 6.80. Both "
     "legs widened for a second consecutive session. The ordinals are UNCHANGED and this is NOT a new state: SIX armings and FIVE "
     "lapses, ELEVEN states (six armed, five lapsed) and TEN changes between them since 29 July. §9.35 QUALIFIES THE 30-YEAR LEG: that "
     "close is identical to four decimals to the published intraday and is UNRESOLVED, so the 7.30 bp margin is provisional. The "
     "CONCLUSION is bounded — the 2 September intraday of 5.2868% clears by 8.68 bp, so B is satisfied on both the questioned close "
     "and the live mark. §9.49 — the recorded DEFECT — stays OPEN, and §9.51, the rule for how to record it, governs the entry: B has "
     "now been met by a bear flattener, a bear steepener and a second bear flattener, which is the non-discrimination the original "
     "complaint named.")},
  {"title": "Threshold C · MOVE above 130 — NOT ARMED, but the direction reversed",
   "text": ("77.88 — 52.12 points below C and 37.14 below the 115.02 war high of 26 March. But it is the HIGHEST close since 77.92 on 11 "
     "August and the SECOND consecutive close above 75, so the Treasury volatility downgrade leg is now moving AWAY rather than "
     "lapsing. The two anchor deviations continue to be reported SEPARATELY, as retired-not-updated on 1 September: volatility is 4.50 "
     "points ABOVE its 73.38 anchor and the 30-year 66.24 bp ABOVE its own — that second figure provisional under §9.35 — both on the "
     "same side for a second session. No composite is constructed. The month-long anomaly of a fully normalised expectation of "
     "movement around an un-normalised yield is now closed on both halves, and it closed because volatility rose to meet the yield.")},
 ],
 "crossAsset": ("The 1 September session was BOTH, and for once the two halves are separable. The Gulf half is the strike wave and the "
   "three-country answer. The Fed half is Governor Barr, a voting member, reported as saying the Board should be prepared to raise if "
   "inflation does not subside — though the only VERBATIM available is the dovish conditional, 'If trends in the data give me some "
   "confidence that inflation is moderating on a path to 2%, then I think we can take a bit more time to assess our policy stance', "
   "and his own coverage calls him noncommittal. He named payrolls and CPI as his conditions. The evidence that the Fed half dominated "
   "is the SHAPE: the 2-year made the largest move on the curve and its first war-high close since 23 July, which no Gulf event "
   "explains. Three pricing instruments, three universes, never averaged. POLYMARKET WAS OBTAINED and §9.50 is DISCHARGED — the "
   "JS-rendered page was driven in a real browser to recover the event slug, then read through the structured API: a 25 bp hike at "
   "56.5% against a hold at 42.5%, the hike +23 points on the week and the hold −23, on $74.7m of event volume. CME FedWatch was NOT "
   "OBTAINED (a QuikStrike iframe exposing no text even to a browser read); its nearest dated figure is 66% on 31 August. Kalshi's "
   "last board is 26 August, 67% hold / 33% hike, published only as the pre-Jackson-Hole marker. No trend is read across the three — "
   "33, then 66, then 56.5 is not even monotone — and the only clean direction is WITHIN one instrument. The US data cut against the "
   "hawks and lost. ISM manufacturing came in at 54.6, down 1.0, with new orders down 3.0 to 53.7 — an eighth month of expansion. It "
   "sits WITH Dallas's +11.6 and against Chicago's 47.1, but it does NOT adjudicate between them: three panels with three geographies "
   "cannot be ranked. JOLTS openings were 7.271m against a 7.33–7.36m consensus with June revised DOWN 177,000; construction spending "
   "fell 0.5%. All three were soft and the 2-year still made a war high. GDPNow is reported at 4.8% against 4.6% on 26 August, on a "
   "single aggregator that could not be checked against the Atlanta Fed's own release, and is therefore carried UNRESOLVED. The Beige "
   "Book is due 2 September at 14:00 ET and is PROSPECTIVE — the Board's own index lists that row with NO link where every prior 2026 "
   "edition carries both HTML and PDF, which is positive evidence of non-publication rather than a retrieval failure. Waller speaks 3 "
   "September, the last Board slot before the 5–17 September blackout; payrolls 4 September; FOMC 15–16 September."),
},

"channels": [
 {"name": "Maritime denial", "score": 5, "state": "max",
  "rationale": ("JMIC 092 moves the count to 100, +3, naming two of three — BURGAN and SENEGAL PROSPERITY, with the third classed as "
   "suspected US blockade enforcement and its name withheld. Hormuz stays SEVERE and every regional threat level is unchanged. The "
   "reopening leg did not move; the facilitated transit rate FELL to 19.5/day from 21.7 on the only like-for-like comparison in the "
   "record. VRA Overview No. 5 is due 4 September and is PROSPECTIVE.")},
 {"name": "Oil price shock", "score": 2, "state": "live",
  "rationale": ("Brent CO2 $91.57, +$3.20, the largest one-day rise since 10 August; WTI CL2 +$3.69. TTF a thirteenth war-record close; "
   "Henry Hub's discount to pre-war WIDENED to 5.19%. $3.43 below the $95 upgrade, the SECOND-NARROWEST of eleven readings. The ACTIVE "
   "contract closed 35 cents short and went THROUGH $95 on the 2 September mark, so on the live mark the trigger sits BETWEEN the two "
   "series; §9.36 forbids merging them and §9.56 records the problem. The downgrade leg is $19.09 away and WIDENED.")},
 {"name": "US inflation impulse", "score": 5, "state": "max",
  "rationale": ("5y5y 2.3110%, +2.25 bp and BACK ABOVE the 2.30% that fired the upgrade, ending the break at two closes. BE10 +3.74 and "
   "agreeing with the forward for once. 16.90 bp above the 2.142% anchor, WIDENED from 14.65. Still the nearer of the two market "
   "downgrade candidates, 16.90 against 27.30, though the gap narrowed for the first time in three editions.")},
 {"name": "Treasury stress", "score": 5, "state": "max",
  "rationale": ("A BEAR FLATTENER: 2-year 4.3998%, a war-high close and its first since 23 July; 5-year 4.5551% and 10-year 4.7981%, both "
   "war highs again; the 30-year close UNRESOLVED under §9.35. MOVE 77.88. BOTH downgrade legs are further away — the volatility leg "
   "LOST for a second close and rising, the yield leg WIDENED to 27.30 bp from 24.23, itself provisional.")},
 {"name": "Political stress", "score": 5, "state": "max",
  "rationale": ("AUTMUSAG backfilled UP to $4.83 for 31 August — the joint-highest print since 5 June, and expressly NOT a war high, which "
   "is $5.18 of 20 May — then dark on 1 and 2 September. AAA diesel $5.6325, +27.09c on the month while regular is down on the week "
   "and the month. 23 cents above the $4.60 condition and moving AWAY. The refiners meeting produced no readout and no measure.")},
 {"name": "Escalation risk", "score": 5, "state": "max",
  "rationale": ("CENTCOM delivered the promised wave inside Iran and published it, breaking a seventeen-day silence in its formal record "
   "and a thirty-four-day one on strikes inside Iran; Iran answered against Jordan, Bahrain and Kuwait. Jordan concedes 3 of 13 fell. "
   "Against it: Iran offered reciprocity at the SCO the same day and the exchange was BOUNDED at one wave each.")},
],

"scoreTotal": ("TOTAL 27 / 30 — CRISIS band (22–30), held for a SEVENTEENTH consecutive edition. FIVE of six channels sit at the cap, so "
 "the score cannot register the delivery of a promised American strike wave inside Iran, the breaking of a seventeen-day silence in "
 "CENTCOM's formal record and a thirty-four-day one on strikes inside Iran, an Iranian answer against three countries in one night, "
 "or a thirteenth war-record TTF close. It equally cannot register what cut the other way: the exchange was bounded at one wave each "
 "with both sides declaring it complete, no MILITARY casualties on either side's official account against four Iranian civilians "
 "reported killed at Kuhestak, and an Iranian reciprocity offer made on the day Iran was bombed. The sixth channel — the only one "
 "with headroom — is this edition $3.43 from moving on the scored series, while on Wednesday's mark the trigger sits BETWEEN that "
 "series and the active contract. A flat 27 is an instrument at its stop, and the one dial still free has just been found to be "
 "ambiguously calibrated."),

"whatsChanged": {
 "title": "4 · What has changed since the 1 September edition",
 "items": [
  ("The promised American retaliation was DELIVERED and put on the formal record. CENTCOM published a release on 1 September "
   "recording a wave against IRGC air-defence, radar, maritime, mine-laying and communications targets from 12:00 EDT — its first "
   "release of any kind in 17 days and first on Iran in 34. The largest open fact in the last edition, RESOLVED. But no target list "
   "and no BDA were published, impact points are Iranian-sourced, and the sole casualty figures are Iranian — four dead including a "
   "child at Kuhestak, per the Red Crescent via AFP."),
  ("Iran answered against THREE countries in one night — Jordan, Bahrain and Kuwait — the IRGC spokesman having said Iran 'will no "
   "longer exercise restraint regarding Bahrain and Kuwait'. Both states confirmed air defences engaged. A widening of the war's "
   "GEOGRAPHY, not its intensity, and the first acknowledged Bahraini and Kuwaiti engagements of the war — why regional relapse rises "
   "again on a STRONGER basis than last edition's denied UAE claim."),
  ("Jordan's own account changed shape: 13 engaged, 10 intercepted, 3 fell in remote areas, no casualties — where a day earlier Petra "
   "had said eight were intercepted and gave no launch total. TWO DIFFERENT ATTACKS on different counting bases; any merged total is "
   "wrong (§9.13). The significance is that the JAF now concedes leakers in its own words, which only ABC's two Jordanian security "
   "sources had said of the earlier salvo."),
  ("The oil channel came within $3.43 of its upgrade on the scored series and went THROUGH the level on the active one. Brent CO2 "
   "$91.57, +$3.20; COA $94.65 at the close — 35c short — and $96.64 Wednesday morning, THROUGH it; the basis ran 2.12, 3.08, 3.63. "
   "THE LARGEST OPEN METHODOLOGICAL PROBLEM IN THIS DOCUMENT (§9.56), ahead of the 5y5y gap and §9.49. The rule was written when the "
   "basis was zero for twenty sessions. It is NOT resolved, and NOT moved to whichever series would fire it (§9.26)."),
  ("Three war-high Treasury closes, and the 2-year's is its FIRST since 23 July. A BEAR FLATTENER falling monotonically with tenor: "
   "2-year +5.83 to 4.3998%, 5-year +5.49, 10-year +4.81, 30-year +3.07 as printed. The front end set its record on the day America "
   "bombed Iran, which no Gulf event explains. BE10 carried 3.74 bp of the 10-year's 4.81 — compensation, not real yield. A Fed trade "
   "wearing a Gulf jacket."),
  ("§9.35 FIRES on the 30-year: its 1 September close of 5.2730% is identical to four decimals to the intraday this document "
   "published for that day, so the close, its d/d and Threshold B's margin are PROVISIONAL. The row is demonstrably live — 13 of 14 "
   "fields moved — which is exactly the case §9.35 was written for after §9.25 cost a war high. The conclusion is bounded: the 2 Sep "
   "mark of 5.2868% clears B independently."),
  ("5y5y went BACK ABOVE 2.30% at 2.3110%, ending the two-close break, and the trigger question the last edition flagged is answered "
   "in the negative. AUTMUSAG backfilled UP to $4.83, the joint-highest since 5 June. Vindication of not moving the rule: had the "
   "downgrade been redefined to the firing level during the break — which §9.26 forbids — this edition would be unwinding it."),
  ("JMIC 092 landed, the count moved to 100 and two of the three missing incidents have names: BURGAN and SENEGAL PROSPERITY, with "
   "the third classed as suspected US blockade enforcement and its name withheld — not under command. A second VLCC, the Saudi SIDR, "
   "is reported struck and is NOT in the 100. A reconciliation the last edition could not close, closed by the issuer. The blockade "
   "tally 82 / 3 / 2 is STILL data-dated 29 August in a 1 September product — a THIRD edition unchanged, pre-dating both the strike "
   "wave and the answer."),
 ],
},

"scenarios": [
 {"name": "Deal collapse — talks stall on terms", "p": 34,
  "desc": "The corridor framework exists on paper and dies over geometry, fees and sovereignty; the blockade and the counter-blockade both continue.",
  "shift": ("−6, and at 34 against 33 the top two lines are a TIE within the resolution of this method. Two things on the same day pull "
   "it apart: Pezeshkian offered reciprocity at the SCO, and Trump answered that an agreement 'isn't worth the paper it's written "
   "on'. A framework needs a counterparty willing to sign one.")},
 {"name": "Return to full war", "p": 33,
  "desc": "Sustained US or Israeli strike campaign inside Iran with Iranian reprisals against US bases and Gulf infrastructure.",
  "shift": ("+10, the largest single-edition move of the war, bringing the top two lines to a TIE. A published American strike WAVE "
   "inside Iran, an Iranian answer against three countries, and the HASC chairman after a CENTCOM briefing saying 'they've got a "
   "plan' and that he would anticipate intensification. +10 and not more because the exchange was BOUNDED at one wave each.")},
 {"name": "Contained but violent", "p": 14,
  "desc": "The present state persists: blockade, counter-blockade, periodic strikes on shipping, no reopening and no general war.",
  "shift": ("−7, the largest cut of the war and its lowest reading. It survived the Larak strike because that was one launcher site; it "
   "does not survive a published multi-target wave answered against three countries. It still describes the MARITIME record but no "
   "longer the state-on-state one.")},
 {"name": "Regional relapse", "p": 16,
  "desc": "The war widens to Gulf states directly — UAE, Saudi, Bahraini, Kuwaiti or Qatari territory or infrastructure struck.",
  "shift": ("+3, and on a STRONGER basis than last edition's +4. Bahraini and Kuwaiti authorities each confirmed engaging incoming "
   "Iranian fire in their own airspace, and the IRGC named both in advance. Those confirmations reach this document as TIER 2 wire "
   "relays of officials, NOT as primary statements — still stronger than last edition's basis, which was an Iranian claim the UAE "
   "DENIED.")},
 {"name": "Mediated pause", "p": 3,
  "desc": "A verified stand-down, resumed talks and a reopening on published terms.",
  "shift": ("UNCHANGED at the lowest reading of the war, and the flat line hides two offsetting facts. FOR: Pezeshkian offered "
   "reciprocity on the record; Qatar is mediating with Oman and Pakistan. AGAINST: Trump refused it the same evening, and no talks "
   "are scheduled by any party.")},
],

"scenarioShift": ("Sums to 100. Deal collapse and full war together carry 67%, UP from 63%, and the three lines involving continued or "
 "widening violence carry 63%, UP from 57%. The structural change is that the top two lines are separated by ONE POINT: 34 against 33 "
 "is inside the resolution of this method, and it is stated as a TIE rather than a lead throughout. The weight behind each shift is "
 "named and stated at the tier it carries. Full war and contained-but-violent move on TIER 1 facts — CENTCOM's own release and the "
 "Jordanian armed forces' own count — with Rogers' 'they've got a plan' alongside at TIER 2. Regional relapse moves on the Bahraini "
 "and Kuwaiti engagements, TIER 2 relays of officials rather than primary statements, still stronger than the denied UAE claim that "
 "moved it last edition. The IRGC's Camp Titin and Prince Hassan casualty claims carry NO weight anywhere. The reading turns on "
 "whether Tuesday was a transaction or an opening. If a second American wave follows inside a week, full war becomes modal outright; "
 "if none follows, this reading is at the top of its range."),

"watchlist": [
 ("Whether a SECOND American wave follows and whether Iran answers again. CENTCOM called Tuesday a 'wave'; Rogers said after Cooper's "
  "briefing that 'they've got a plan'. It decides whether Tuesday was a transaction or an opening, and it is the difference between a "
  "full-war line tied at the top and one clear of it. Both capitals have demonstrated they will strike and stop; neither has "
  "demonstrated it will stop twice."),
 ("Whether Brent CO2 closes above $95 — and how the trigger is to be read if the active contract keeps running ahead. On the 2 "
  "September mark COA is $1.64 through and CO2 $1.99 below, basis 3.63 and widening. The largest open methodological problem in this "
  "document (§9.56). An upgrade on one series and not the other is not a defensible published state, and §9.26 forbids resolving it "
  "toward whichever series fires."),
 ("Whether the 30-year prints a value distinguishable from 5.2730% on the next close, resolving the §9.35 flag, and whether MOVE "
  "holds above 75 a third time. Threshold B's 7.30 bp margin and the 30-year leg of the bear flattener are provisional until it does. "
  "The conclusion is already bounded by the 2 Sep mark, so this resolves a FIGURE, not a finding."),
 ("The 2 September Beige Book at 14:00 ET and the 2 September WPSR; Waller at Reuters on 3 September; payrolls 4 September — all "
  "PROSPECTIVE at the cut. Barr named payrolls and CPI as his conditions and the 2-year made a war-high close the same day. Waller is "
  "the LAST Board slot before the 5–17 September blackout. The WPSR is the next chance at the SPR conflict, EIA 289.7 mn bbl against "
  "DOE 294.1 MMB, both standing."),
 ("The 8 September War Powers expiry into a Senate that does not return until 14 September; the STILL-unpublished buyback schedule "
  "seven days before the $4bn regime starts 9 September; the general licences winding down 8 September; VRA No. 5 on 4 September; "
  "OPEC+ on 6 September. Five dated events inside a week. The buyback gap is THREE editions old, re-verified against the live PDF — "
  "still stamped 5 August, the 10 September operation still capped at $2bn."),
 ("Whether any US, CENTCOM or Jordanian source publishes a BDA, impact points or a casualty figure for either the 1 September strikes "
  "or either Jordan salvo — and JMIC Update 093, whose cadence implies 3–4 September, plus UKMTO Warnings 125-26 onward. The method "
  "must be varied again on CME FedWatch and TreasuryDirect, both of which remain method-bound negatives (§9.50)."),
],

"sourceLog": {
 "tier1Market": ("Tecity Bloomberg extract, US Iran BBG Data.xlsx, 2 September pull, 177 rows to 2 September 2026 — ALL scored prices, "
  "yields, spreads, volatility and both gasoline series. No market figure in this document comes from the web; screen quotes for "
  "'Brent' on 1–2 September refer to the ACTIVE contract and are not the scored series. Every row of the live tape carries the "
  "Bloomberg ticker it is drawn from, taken from the extract's own row-0 header scan and never hardcoded: CO2/COA Comdty (Brent "
  "listed and active), CL2/CLA Comdty (WTI), NGA Comdty (Henry Hub), TZTA Comdty (Dutch TTF), JGLA Comdty (Japan/Asia LNG), "
  "USGG2YR/5YR/10YR/30YR Index, USYC2Y10 Index (2s10s, a separate series and not a difference of the generics), USGGBE10 Index, "
  "USGG5Y5Y Index, SOFRRATE Index, MOVE Index, VIX Index, DXY Index, AUTMUSAG Index (the scored gasoline series) and USRFRUSA Index "
  "(weekly corroboration). The 1 September close is the scoring reference; the 2 September row is intraday and moves nothing."),
 "tier1News": ("Primary documents read directly: the US Central Command public release 'CENTCOM Completes Strikes on IRGC Targets in Iran' "
  "(1 September, TAMPA dateline), for the strike wave, its target categories and its stated cause, and for the ABSENCE of a target "
  "list and of a battle-damage assessment; JMIC Advisory Note UPDATE 092 (ICOD 011500 UTC), obtained as a primary PDF by guessing the "
  "media-path filename from the established naming convention, for the count at 100 / +3, the three incidents, the threat levels, the "
  "mine passages and their tagging, the 39 NCAGS-facilitated and 7 annex transits for 30–31 August, and the CENTCOM blockade tally "
  "with its 29 August data date; the Jordan Armed Forces statement of the early hours of 2 September via AFP, for 13 engaged, 10 "
  "intercepted and 3 fallen; President Pezeshkian at the SCO summit via Reuters and Qatar's MFA spokesman via Al Jazeera, both 1 "
  "September; President Trump's Truth Social post of 1 September, taken from three independent verbatim relays because the platform "
  "is not fetchable; ofac.treasury.gov Recent Actions and home.treasury.gov press releases, both read direct on 2 September, for the "
  "null run 29 August – 2 September; the Treasury tentative buyback schedule PDF, re-fetched and still stamped 5 August; the Senate's "
  "own 2026 legislative schedule; the AAA Daily Fuel Gauge read direct on 2 September; DOE 'SPR Quick Facts', re-read; the EIA WPSR "
  "highlights file, fetched direct and still serving the week ending 21 August; the ISM Manufacturing report, BLS JOLTS and Census "
  "C30, all 1 September; and Polymarket, whose JS-rendered page was driven in a real browser to recover the event slug before the "
  "structured API was read — which is what DISCHARGES §9.50 on a negative published twice."),
 "tier3": ("Tier 2 — reputable wire or press, used for characterisation and for facts no primary source published: Reuters, AFP, ABC News, "
  "Al Jazeera, Stars and Stripes, Jerusalem Post, Times of Israel, Bloomberg and Insurance Journal, 1–2 September, for the Iranian "
  "impact points, the Bahraini and Kuwaiti air-defence engagements, the SIDR and SENEGAL PROSPERITY strikes and their cargoes, the "
  "two US officials on no American casualties, and Trump to Fox on an agreement not being 'worth the paper'; Kpler via Reuters and "
  "the Lloyd's List Strait of Hormuz brief of 27 August, re-fetched, which WITHDRAWS the 114 / +30% this document had been carrying "
  "for 17–23 August and replaces it with 108 / +27% on a universe of cargo-carrying vessels over 10,000 dwt; Marisks via Reuters and "
  "AFP; Ship & Bunker, read 2 September; Bessent with Kudlow at the G20 in Asheville; Barr coverage in CNBC, Bloomberg and American "
  "Banker; and the WSJ relay of Adm. Cooper's HASC briefing and Chairman Rogers' 'they've got a plan'. Tier 3 — Iranian state media "
  "(IRNA, Press TV, Tasnim, Mehr, Fars), RECORDED AND NOT USED for any finding: the Camp Titin and Prince Hassan casualty claims, "
  "contradicted by the JAF and by two US officials; the 50th MQ-9 claim; the 'Saudi tanker stopped' report, which three outlets carry "
  "with the identical 'no Saudi confirmation' qualifier; the IRGC supertanker mine-strike claim, which JMIC 092 does not log; and "
  "Speaker Ghalibaf, correctly tiered 3 as Iranian state media and therefore not used to attribute the tanker strikes. NOT OBTAINED, "
  "each with its method named so a fact about the world can be told from a fact about the fetch: UKMTO Warnings 125-26 onward, on "
  "five varied methods including the filename-convention guess that DID work for JMIC 092; CME FedWatch, whose QuikStrike iframe "
  "exposes no text even to a rendered browser read; TreasuryDirect's 1 September bill results, client-rendered; IMF PortWatch after "
  "23 August; a dated 1–2 September war-risk broker quote, searched by date, by broker name and by publication; the AMARA's status, "
  "searched by name, by IMO and against three trackers; and any US, CENTCOM or Jordanian BDA for the 1 September strikes or either "
  "Jordan salvo. PROSPECTIVE, and therefore not retrieval failures: the 2 September Beige Book and WPSR — in both cases the "
  "non-publication is POSITIVELY evidenced — the 2 September cash-management buyback announcement, the 3 September Lloyd's List brief "
  "and Waller, UKMTO VRA Overview No. 5 and Baltic week 36 on 4 September, payrolls on 4 September and OPEC+ on 6 September."),
},

"protocol": [
 {"step": "Refresh and integrity-check the extract",
  "detail": ("Never build an edition off a stale extract: check the file timestamp AND parse the sheet. This edition the extract carries a "
   "2 September row against the 1 September row the last edition ran on, and the 1 September row has settled into a genuine close. It "
   "is fresh.")},
 {"step": "Parse with a dynamic header scan",
  "detail": ("Column indices move between uploads. Auto-detect the Brent and WTI front month and take whatever label the header scan "
   "returns for DXY. Re-verify the 27 February anchor field by field — done this edition, unchanged on all seventeen anchor fields, "
   "and on SOFR at 3.68, which the tape uses but which is not one of the seventeen.")},
 {"step": "Run all THREE integrity checks",
  "detail": ("Row-level, field-level identical-value at the precision each series is published to, and the continuation-versus-active BASIS "
   "check. This edition §9.8 and §9.41 CLEAR but §9.35 FIRES on the 30-year, whose 1 September close is identical to four decimals to "
   "the intraday this document published for that day. The field is UNRESOLVED even though thirteen of fourteen fields around it "
   "moved — which is exactly the case the rule was written for after its predecessor cost a war high. The Threshold B conclusion is "
   "bounded by the live 2 September mark.")},
 {"step": "Run the backfill check in BOTH directions",
  "detail": ("Yesterday's dark cells must be re-examined, not carried, and a backfill is as likely to run against a trend as with it. This "
   "edition it fired on SIX cells and two were consequential: AUTMUSAG backfilled UP to $4.83, two cents above the value being "
   "carried and the joint-highest since 5 June though NOT a war high, WIDENING the political distance to 23 cents; SOFR backfilled at "
   "3.68, its highest since 17 August. USRFRUSA backfilled DOWN in the same week. MOVE, VIX and Asia LNG also backfilled and changed "
   "nothing. The test has now fired in BOTH directions across three consecutive editions.")},
 {"step": "Compute deltas and test every trigger",
  "detail": ("Day-on-day, week-on-week five rows back, and versus pre-war; explicit trigger tests for the four market channels plus "
   "Stage-4 A, B and C. Run min, max and last-prior-occurrence on the full column before writing ANY superlative — it is what "
   "established THREE war-high closes and the thirteenth war-record TTF close this edition, and what stopped the 30-year being "
   "written as a record when it is third-highest, AAA diesel being called a war high when its record predates the war by four years, "
   "and the gasoline backfill being called a war high when it is not.")},
 {"step": "Verify the news, then QA in three passes",
  "detail": ("Every claim needs a named source and an exact date, and negative claims decay fastest of all. State the method behind every "
   "negative, say NOT OBTAINED rather than estimating, and distinguish NOT OBTAINED from PROSPECTIVE. VARY THE RETRIEVAL METHOD "
   "before repeating a method-bound negative — doing so DISCHARGED the Polymarket negative this edition. Then run a numeric harness "
   "against the dataframe (177 checks, which caught a sign error on the $95 comparison and a false war high), an adversarial PROSE "
   "pass by a reviewer with no access to the source data, run TWICE because fixing introduces defects, and a VISUAL render. The "
   "second pass earned its keep entirely on seams the first round of fixes created.")},
],

"methodology": {
 "scale": ("Shock-score scale. Six transmission channels — maritime denial, oil price shock, US inflation impulse, Treasury stress, "
  "political stress and escalation risk — each scored 0–5 and summed to 0–30. Bands: 0–7 watch, 8–14 stress, 15–21 systemic-risk "
  "watch, 22–30 crisis. Maritime denial and escalation risk are event channels; the other four are market channels and move only on "
  "confirmed closes, never on an intraday print. Upgrades fire on a sustained break of a named level; downgrades require a sustained "
  "reversal past a WIDER threshold, which is the hysteresis that stops a channel whipsawing on one session."),
 "scaleCap": ("The saturated scale, and it fails in BOTH directions. FIVE of the six channels are at the cap, so the total cannot register "
  "the delivery of a promised American strike wave inside Iran, an Iranian answer against three countries in one night, or a "
  "thirteenth war-record TTF close — and it equally cannot register the restraint that cut the other way, an exchange bounded at one "
  "wave each with an Iranian reciprocity offer made on the day Iran was bombed. A flat 27 is an instrument at its stop, not a stable "
  "week. This edition adds a second failure mode: the ONE channel with headroom is scored on a trigger this edition had to declare "
  "ill-defined, so the only free dial is also the ambiguously calibrated one."),
 "integrity": ("Data integrity this edition. Three checks run every time. The row-level check CLEARS decisively — thirteen of the fourteen "
  "scored fields published as a 1 September intraday moved, and MOVE, VIX and Asia LNG all printed where the snapshot was blank. The "
  "basis check CLEARS as a positive result for a second edition: the Brent continuation-to-active basis printed 2.12, 3.08 and 3.63 "
  "across three sessions, WIDENING smoothly without a sign change or a second step, which is what a correctly-rolled pair looks like "
  "under a moving term structure. But the field-level identical-value check FIRES, on one field and the worst one it could have "
  "picked: the 30-year's 1 September close of 5.2730% is identical to four decimal places to the intraday published for that day. "
  "That field is UNRESOLVED regardless of the live row around it, so the close, its day-on-day change and Threshold B's 7.30 bp "
  "margin are all published as PROVISIONAL, and the long-end leg of the bear flattener is contingent. The conclusion is nonetheless "
  "bounded: the 2 September intraday prints 5.2868%, a different value, and clears Threshold B independently."),
 "gasoline": ("Gasoline series, and a denominator warning that covers THREE series rather than two. AUTMUSAG — the AAA all-grades retail "
  "pump average, daily with a one-day lag — is the SCORED reference for political stress and preserves the $3.52 pre-war anchor, the "
  "$4.75 upgrade trigger and the full history; it is never re-based. USRFRUSA — the DOE regular-grade retail spot, weekly and "
  "surveyed on Mondays — is corroboration only. AAA's own published headline, read directly from its page, is a THIRD series and is "
  "never compared with either. This edition the first backfilled UP to $4.83 and the second backfilled DOWN to $4.071 in the same "
  "week; they point opposite ways and neither is the other's check, because they are different surveys of different products on "
  "different cadences."),
 "anchor": ("Pre-war anchor (27 February 2026 close), re-verified field by field this edition and unchanged: Brent $72.48, WTI $67.02, "
  "2-year 3.3749%, 5-year 3.5017%, 10-year 3.9375%, 30-year 4.6106%, 2s10s +55.64 bp, 5y5y 2.142%, 10-year breakeven 2.2569%, MOVE "
  "73.38, VIX 19.86, DXY 97.608, AAA gasoline $3.52, DOE gasoline ~$2.94, Henry Hub $3.063, TTF €31.23, Asia LNG ¥1,669. Seventeen "
  "fields. The 27 February SOFR fix of 3.68 is used in the tape but is not one of them."),
 "intraday": ("Intraday caveat, and the three open methodological items. The 2 September row is a Singapore-morning mark taken before the "
  "US cash session and moves NO channel — including a Brent mark of $93.01 that would put the upgrade under two dollars away, an "
  "active-contract mark of $96.64 that is THROUGH the trigger level, a TTF mark above the record close set the day before, and three "
  "further intraday yield highs. THREE OPEN ITEMS REMAIN DISCLOSED RATHER THAN DECIDED. (1) NEW AND NOW FIRST IN LINE — §9.56, the "
  "oil trigger's ambiguity across the roll: on the 1 September close neither Brent series is through $95 (the continuation $3.43 "
  "below, the active $0.35 below), but on the 2 September mark they STRADDLE it, the continuation $1.99 below and the active $1.64 "
  "above. The rule is held on the scored continuation and is NOT moved to whichever series would fire it. (2) Threshold B's long-end "
  "LEVEL versus long-end CONTRIBUTION question, now three observations deep: B has been met by a bear flattener, a bear steepener "
  "and a second bear flattener, and a test returning the same answer for opposite curve signatures is not discriminating between "
  "them. (3) DOWNGRADED FROM RISING TO DORMANT — the US-inflation channel's firing trigger came back on 1 September, so the gap "
  "between the firing rule and the documented downgrade is no longer live. It is not closed, since the downgrade is still 16.90 bp "
  "lower and the break could resume, but it is no longer the largest problem on the list."),
},
}
