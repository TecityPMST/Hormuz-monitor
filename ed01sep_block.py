# -*- coding: utf-8 -*-
# 1 SEPTEMBER 2026 — full section-by-section block for generate_editions.py
# Content copied from build/build_edition01sep.py and build/build_annex01sep.py.
# Plain text with real Unicode punctuation — no HTML entities, no markup (house convention).

ED01SEP = {
 "label": "1 Sep 2026",
 "editionLine": "Daily edition · 1 Sep 2026 intraday · Bloomberg · Singapore 1 Sep AM update",
 "score": 27,
 "band": "CRISIS",
 "sequencing": "27 → 27 → 27 → 27 → 27 → 27 → 27 → 27 → 27 → 27 → 27 → 27 → 27 → 27 → 27 → 27",
 "sessionNote": (
   "Score held for a sixteenth edition · no channel moved · and the day's finding is that Iran answered the Larak "
   "strike by firing ballistic missiles at American bases in Jordan, with Jordan's own armed forces, Iran's own "
   "foreign ministry and Qatar's own foreign ministry each putting it on the record inside twenty-four hours — "
   "turning the last edition's uncorroborated Tier 3 claim into a Tier 1 event. The scoring reference is the 31 "
   "August close; the 1 September row is a Singapore-morning mark taken before a US cash session that had not begun "
   "at the cut, so every US publication dated 1 September is PROSPECTIVE rather than unobtained."
 ),
 "headline": (
   "Score HOLDS at 27/30 for a sixteenth consecutive edition. No channel moved. Iran answered the Larak strike by "
   "firing ballistic missiles at American bases in JORDAN, and three foreign ministries — Jordan's, Iran's own and "
   "Qatar's — put it on the record inside twenty-four hours, turning the last edition's uncorroborated Tier 3 claim "
   "into a Tier 1 event. "
   "One. What is corroborated is the EVENT, not the damage. Petra reports eight missiles intercepted and destroyed "
   "and gives no launch total, so no interception rate follows from it; Iran's foreign ministry confirms the "
   "targeting; Qatar names Iran, and names the UAE with it. Against that, ABC carries two Jordanian security sources "
   "saying some missiles were NOT intercepted, no US or Jordanian damage assessment or casualty figure was OBTAINED, "
   "and the separate UAE strike claim is Iranian and DENIED by Abu Dhabi. Trump promised retaliation and had not "
   "delivered it at the cut — the largest open fact on the board, and the reason the full-war line moves two points "
   "rather than ten. "
   "Two. The allies would not certify the mine claim. JMIC Update 091, issued after Adm. Cooper declared the "
   "internationally recognised routes free of Iranian mines and on the day of the Larak strike, re-published 'mine "
   "danger areas still active' and continuing clearance operations, both flagged '(No change)'. Four allied "
   "statements inside a week now say the lanes are clear, that no ship has hit a mine, that launchers were loading "
   "fresh ones, and that the danger areas remain. Only the FLOW-not-STOCK reading fits all four, and it rests on "
   "allied paper rather than on this document's inference. "
   "Three. The market half moved in the right shape and cost two downgrade legs. A BEAR STEEPENER rising "
   "monotonically with tenor took the 10-year to 4.7500% and the 5-year to 4.5002%, both NEW WAR-HIGH CLOSES, on "
   "real yield rather than compensation, and Threshold B held a second close with both legs widening. But MOVE "
   "printed 75.32, ending nine consecutive closes below 75, so the Treasury volatility leg is LOST and §9.15 fails "
   "to fire for a THIRD session; and the 5y5y forward closed below 2.30% for a SECOND CONSECUTIVE session, the "
   "first time that break has held. A channel scored at 5 on a trigger that has now failed twice running is the "
   "most adverse fact here for the monitor's own scoring, and §9.26 still forbids moving the rule. "
   "Four, and nobody has priced it: the 60-day War Powers clock from the 10 July notification expires on 8 "
   "SEPTEMBER, into a Senate sitting in pro forma session until 14 September. A statutory expiry arrives six days "
   "before the chamber that would have to act can act. "
   "Sequencing 27 → 27 → 27. Five of six channels are at the cap, so the score can register NEITHER an Iranian "
   "ballistic-missile attack on American bases in a treaty partner NOR two war-high Treasury closes on one day. "
   "Only oil has headroom, and its distance to the upgrade narrowed to $6.63 from $6.90."
 ),

 "tape": {
  "note": (
    "Scoring reference is the 31 August close (Mon); the 1 September row is a Singapore-MORNING mark taken BEFORE "
    "the US cash session and moves no channel. ALL THREE integrity checks CLEAR — the first clean sweep in three "
    "editions — and the two-way backfill test fires on FOUR cells, decisively on MOVE. The 1 September US session "
    "had not begun at the cut: the ISM, JOLTS, construction spending, the GDPNow update and the White House "
    "refiners meeting are PROSPECTIVE, not unobtained (§9.46). Every row below carries the Bloomberg ticker it is "
    "drawn from, one row per series; the tickers are taken from the extract's own header scan and are never "
    "hardcoded (§3). Lumping distinct series onto one line was retired this edition — on 31 August the 10-year "
    "breakeven rose 0.27 bp while the 5y5y forward fell 0.79, and a shared row cannot say so."
  ),
  "oilGasHeader": ["Series", "BBG ticker", "27 Aug", "28 Aug", "31 Aug close", "1 Sep intr.", "Trigger note"],
  "oilGas": [
   ["Brent, front-month listed — scored", "CO2 Comdty", "88.52", "88.10", "88.37", "88.86",
    "+$0.27. $6.63 from the $95 upgrade, NARROWED from $6.90 — the tenth reading, the sixth narrowing. $15.89 above the $72.48 downgrade, WIDENED. The scored rule is written on this series."],
   ["Brent, active contract", "COA Comdty", "88.52 (W)", "88.10 (W)", "90.49", "91.09",
    "(!) NO d/d ACROSS 28→31 AUG — different delivery months (§9.36). (W) = restated to equal CO2; the four prices WITHDRAWN last edition stay withdrawn. $4.51 from $95, NOT the scored figure."],
   ["WTI, front-month listed — scored", "CL2 Comdty", "81.97", "81.83", "84.06", "84.66",
    "+$2.23 — eight times Brent's move and the largest crude move of the window. No trigger is written on WTI; it is corroboration for the crude leg."],
   ["WTI, active contract", "CLA Comdty", "83.53", "83.40", "85.76", "86.56",
    "Basis to CL2 of 1.56, 1.57, 1.70, 1.90 — no sign change and no step since its own 21 Aug roll. WTI is the clean pair; Brent is not."],
   ["Henry Hub natural gas", "NGA Comdty", "2.914", "2.888", "2.935", "2.932",
    "4.18% BELOW its $3.063 anchor, from 5.71%. The control in the experiment is still negative — but it closed four points of discount in six sessions."],
   ["Dutch TTF natural gas", "TZTA Comdty", "68.268", "66.979", "69.809", "70.520",
    "A NEW WAR-RECORD CLOSE, +€2.830, taking out €68.457 (24 Aug) — the twelfth of the war. +123.6% vs pre-war. The 1 Sep intraday is NOT a record (§9.31)."],
   ["Japan/Asia LNG", "JGLA Comdty", "3,687", "3,785", "3,761", "no print",
    "(!) BACKFILLED — the last edition reported no 31 Aug print. −24; THIRD-highest close of the war; +125.3% vs pre-war."],
  ],
  "ustNote": (
    "Basis points. A BEAR STEEPENER, rising monotonically with tenor — the exact inverse of 28 August, which was a "
    "front-end-led bear flattener. Two new war-high closes were set and no trigger is written on either tenor, which "
    "is how a war high can be set twice running without moving a single channel. Breakevens barely moved, so the "
    "long-end move was real yield and term premium rather than compensation."
  ),
  "ustHeader": ["Tenor", "BBG ticker", "27 Aug", "28 Aug", "31 Aug close", "1 Sep intr.", "d/d, bp", "Trigger note"],
  "ust": [
   ["2-year", "USGG2YR Index", "4.2320", "4.3434", "4.3415", "4.3560", "−0.19",
    "The ONLY tenor that fell. Fourth-highest CLOSE of the war; the closing war high is 4.3470% (23 Jul), which the 1 Sep intraday exceeds — but this document ranks CLOSES only."],
   ["5-year", "USGG5YR Index", "4.3996", "4.4789", "4.5002", "4.5232", "+2.13",
    "A NEW WAR-HIGH CLOSE for a SECOND consecutive session. No trigger is written on the 5-year either."],
   ["10-year", "USGG10YR Index", "4.6762", "4.7180", "4.7500", "4.7780", "+3.20",
    "A NEW WAR-HIGH CLOSE, passing 4.7347 (31 Jul) — its first in a month. SATISFIES Threshold B's 4.65% leg by 10.00 bp, its widest of the regime."],
   ["30-year", "USGG30YR Index", "5.1931", "5.2056", "5.2423", "5.2730", "+3.67",
    "The largest move on the curve. CLEARS B's 5.20% by 4.23 bp from 0.56, so B HOLDS. NOT a war high (5.3060, 17 Aug); the TENTH close above 5.24. The downgrade leg fails by 24.23 bp, WIDENED from 20.56."],
   ["2s10s spread", "USYC2Y10 Index", "44.014", "37.049", "40.635", "41.990", "+3.586",
    "A STEEPENING giving back 51.5% of Friday's flattening; 15.005 bp flatter than the 55.64 anchor. (!) A SEPARATE series, not the difference of the printed generics."],
   ["10-year breakeven", "USGGBE10 Index", "2.3335", "2.3179", "2.3206", "2.3231", "+0.27",
    "6.37 bp above its 2.2569 pre-war anchor, WIDENED from 6.10. (!) It moved the OPPOSITE way to the 5y5y forward on the same session, which is itself a reason not to act on either."],
   ["5y5y forward breakeven", "USGG5Y5Y Index", "2.3182", "2.2964", "2.2885", "2.2947", "−0.79",
    "(!) Closed below the 2.30% firing level for a SECOND CONSECUTIVE session — the first time the break has held two closes — and 2.2885 is the LOWEST close since the upgrade fired on 31 July. 14.65 bp above the 2.142% downgrade anchor, NARROWED from 15.44. §9.26: report it, do not move the rule."],
  ],
  "crossHeader": ["Series", "BBG ticker", "28 Aug", "31 Aug close", "vs pre-war", "Note"],
  "cross": [
   ["Treasury volatility (MOVE)", "MOVE Index", "70.97", "75.32", "+1.94 vs 73.38",
    "(!) BACKFILLED, and it is the consequential backfill of the edition. +4.35. The run of NINE closes below 75 (18–28 Aug) is BROKEN — only the second close at or above 75 since 12 Aug. The Treasury volatility leg is LOST, and MOVE is above its pre-war anchor for the first time since 17 Aug."],
   ["Equity volatility (VIX)", "VIX Index", "14.43", "14.92", "−4.94 vs 19.86",
    "+0.49, and still the EIGHTH-lowest close of the war — equities pricing no event risk into a weekend that reopened the air war in both directions."],
   ["US dollar index", "DXY Index", "99.702", "99.428", "+1.82 vs 97.608",
    "−0.274, giving back half of Friday's dollar rally. (!) The label resolves as DXY Index, NOT DXY Curncy — taken from the header scan every edition, never hardcoded (§9.4)."],
   ["SOFR overnight rate", "SOFRRATE Index", "3.65", "no print", "—",
    "(!) BACKFILLED at 3.65 for 28 Aug, which the last edition reported DARK; dark again on 31 Aug and 1 Sep. No trigger is written on SOFR."],
   ["Gasoline, AAA all-grades retail pump — scored", "AUTMUSAG Index", "4.81", "no print", "+1.29 vs 3.52",
    "(!) BACKFILLED DOWN — the last edition reported 28 Aug DARK with $4.82 (27 Aug) as last resolved. DARK on 31 Aug and 1 Sep. 21 cents above the $4.60 condition, 6 above the $4.75 that fired the upgrade (§9.30)."],
   ["Gasoline, DOE regular retail spot — corroboration", "USRFRUSA Index", "no print", "no print", "+1.15 vs ~2.94",
    "Weekly, surveyed Monday. Last print $4.085 (24 Aug); the 2 Sep EIA release carries the 31 Aug survey and is PROSPECTIVE."],
  ],
  "gasChartNote": (
    "AAA all-grades (AUTMUSAG Index, navy, the scored series) against DOE regular retail (USRFRUSA Index, amber, "
    "weekly, corroboration only). The scored series has printed at or above the $4.75 upgrade trigger on every "
    "session since 12 August. Its last two cells, 31 August and 1 September, are dark, so the plotted line ENDS on "
    "28 August at $4.81 and no extrapolation is drawn through the gap. THREE retail series are tracked and never "
    "compared: AUTMUSAG (scored) last RESOLVED at $4.81; USRFRUSA (weekly corroboration) at $4.085; and AAA's own "
    "published headline, read direct on 1 September from a page stamped 'price as of 8/31/26', at regular $4.0807 "
    "and diesel $5.6002. Both AAA series are down on the week; diesel is still +24.74c on the month, CORRECTED from "
    "the +26.4c carried on 31 August because AAA's month-ago row now reads $5.3528 — a comparison window moving, "
    "not a restatement. Diesel stays 21.57c below the all-time record of $5.8159 of 19 June 2022, four years before "
    "this war."
  ),
  "straitHeader": ["Strand", "State on 1 September", "Source"],
  "strait": [
   ["UKMTO / incidents / mines",
    "THE MINE WATCHLIST ITEM IS RESOLVED, AGAINST THE CLEARANCE CLAIM. JMIC Update 091, ICOD 301500 UTC — a FRESH product issued two to three days after Adm. Cooper declared the internationally recognised routes free of Iranian mines, and on the day of the Larak strike — keeps mine danger areas 'still active' and clearance operations continuing, and flags BOTH passages '(No change)'. Against it, CENTCOM on 31 Aug: 'This is FALSE. No ships have hit mines in the Strait of Hormuz.' NEW Warning 124-26: a tanker struck by THREE projectiles 17 nm E of Khasab, 31 Aug, outbound. Warning 122-26 re-sourced as a primary PDF, provenance CORRECTED — issued 30 Aug, source military authorities, vessel inbound. (!) The count stays at 97 with NIL new incidents against a 301500Z cut-off: 122-26 (2053Z, 29 Aug) is INSIDE that window and the count still did not move; 124-26 post-dates it by 29 hours. One unexplained absence, one simply too late.",
    "JMIC 091 and UKMTO Warnings 122-26 / 124-26, primary PDFs, 1 Sep; @CENTCOM via CBS 31 Aug — Tier 1"],
   ["Transits + blockade",
    "THE SHARPEST DISAGREEMENT IS INSIDE ONE DOCUMENT: JMIC 091 reports 65 US NCAGS-FACILITATED transits over 27–29 Aug against a stated ~138/day 2025 baseline, while its own annex totals NINE for the identical three days on a non-facilitated cargo denominator. (!) 65 and 9, one publication, not blended (§9.24). TankerMap: 7 tanker transits over 24–30 Aug, 1.0/day, −30% w/w against ~21/day. IMF PortWatch, RECOVERED after two editions NOT OBTAINED: 3 crossings on 23 Aug = 4% of its own ~85/day median. VRA Overview No. 5 is DUE 4 SEPTEMBER — PROSPECTIVE, not missed. (!) CENTCOM's 82 / 3 / 2 was RE-DATED to 29 Aug by JMIC 091, not incremented; its data date pre-dates the retaliation, so it is evidence about neither strike.",
    "JMIC 091 §4C and annex; TankerMap; IMF PortWatch — Tier 1 and Tier 2"],
   ["CENTCOM / kinetic",
    "THE EXCHANGE WENT BOTH WAYS AND THE RETALIATION IS PROMISED, NOT DELIVERED. After the 30 Aug US strike on two IRGC launchers on LARAK ISLAND, Iran ran operation 'Punishment of the Aggressor': ballistic missiles at the KING HUSSEIN and AL-AZRAQ bases in JORDAN, intercepted early 31 Aug, and a CLAIMED drone attack on AL MINHAD in the UAE. TIER 1 ON THREE SIDES for the Jordan strike: Petra — eight missiles intercepted and destroyed, WITHOUT naming Iran, the targets or any base; Iran's Foreign Ministry, confirming it targeted US bases in Jordan; Qatar's MFA, condemning Iranian attacks on Jordan and the UAE by name. (!) The UAE DENIED Al Minhad was hit while confirming it engaged a UAV approaching from Iran, so the UAE strike claim remains Tier 3 and contradicted. NO US, CENTCOM or Jordanian BDA, casualty figure or interception count was OBTAINED, and ABC reports two Jordanian security sources saying some missiles were NOT intercepted. Trump: 'We're going to hit them hard'; nothing executed at the cut. centcom.mil has published nothing since 15 Aug and no combat release since 29 July.",
    "Petra 31 Aug; Mehr 31 Aug; Qatar MFA 31 Aug; UAE MoD/MoFA; Stars and Stripes, Fox, ABC, CBS 31 Aug — Tier 1 and Tier 2"],
   ["Diplomacy + economic war",
    "BOTH TRACKS STOPPED ON THE SAME DAY AND THE NEGATIVES ARE THE FINDING. Oman's MFA Statements page, read direct 1 Sep, carries NOTHING dated 30 or 31 Aug or 1 Sep; the last Iran text remains the 25 Aug joint statement, which names no geometry, no fee and no revenue share. NO Iranian corridor statement after 29 Aug, NO readout of the Qatari PM's 27 Aug Tehran visit, NO US negotiations statement after Leavitt on 27 Aug, and no trace of Witkoff. (!) Qatar moved from MEDIATOR to CRITIC in four days. NO OFAC action and NO Iran-related Treasury release after 28 Aug. STILL no Chinese bank. The Banque Misr UAE Section 311 action remains a PROPOSED rule with its comment window open. The UAE embargo of 18 Aug is FOURTEEN days old with no decree, resolution or gazette text. NEW dated item: the five Iran-related general licences OFAC suspended on 24 Aug wind down 8 SEPTEMBER.",
    "fm.gov.om, ofac.treasury.gov and home.treasury.gov all read direct 1 Sep; Qatar MFA 31 Aug; FinCEN NPRM — Tier 1"],
  ],
 },

 "analysis": {
  "intro": (
    "The scoring reference is the 31 August close; the 1 September row is a Singapore-AM snapshot and moves no "
    "channel. Six channels, in the order in which the session moved them. Two of them lost ground toward a "
    "downgrade this session and both losses were on the Treasury channel, which is why §9.15 is stated in full "
    "below even though it does not apply."
  ),
  "bondYieldNote": (
    "Six channels. Five sit at the cap, so the scale can register neither the escalation nor the two war-high "
    "Treasury closes; only oil, at 2, has headroom. Read the composition rather than the total."
  ),
  "bondYield": [
   {"title": "(i) Maritime denial — held at 5 (max). The allied maritime authority re-published its mine language unaltered.",
    "text": "The downgrade requires a verified reopening AND traffic above 25% of normal for ten sessions. The traffic evidence did not advance: UKMTO's VRA Overview No. 4 remains the current edition and No. 5 is due Friday 4 September on a weekly Friday cadence, so it is PROSPECTIVE rather than missed. What did advance is the REOPENING leg, and it advanced against a downgrade. JMIC Advisory Note Update 091, ICOD 301500 UTC, states that mine danger areas are 'still active' and that clearance and mine-surveying operations 'continue throughout the Strait of Hormuz' — and flags both passages '(No change)'. The evidence is that a body which issued a FRESH product after the clearance claim left both passages unaltered; that is a re-publication, not a stated refusal, and it is not written as one. But a waterway whose own multinational authority re-publishes active mine danger areas after a clearance declaration is not a verified reopening, whatever any single command says. Two further incidents, and the count that should hold them does not: Warning 124-26 records a tanker struck by three projectiles 17 nm east of Khasab on 31 August, outbound; Warning 122-26, now obtained as a primary document, records one struck 12 nm north of Khasab on 29 August, inbound. JMIC 091's cumulative count stands at 97 with 'NIL incidents since the last report' against a cut-off of 30 August 1500 UTC — so 122-26 is INSIDE that window and the count still did not move, while 124-26 post-dates it by 29 hours. The measurement problem also got worse and it is now INSIDE one document: JMIC 091 reports 65 US-facilitated transits over 27–29 August against a stated ~138/day historical average, while the annex of the SAME document totals NINE for the identical three days on a non-facilitated cargo denominator. These are not commensurable and no range across them is constructed here."},
   {"title": "(ii) Oil price shock — held at 2. The only channel with headroom narrowed toward its upgrade, on a strike rather than on a barrel.",
    "text": "Brent CO2 closed $88.37 on 31 August, +$0.27, leaving the $95 upgrade $6.63 away — NARROWED from $6.90. The edition-over-edition sequence is now 9.78, 8.43, 5.55, 5.21, 3.03, 7.73, 8.06, 6.48, 6.90, 6.63 — TEN readings, six narrowings, three widenings. The downgrade leg moved the other way, to $15.89 above $72.48 from $15.62. The basis check CLEARS for the first time since the roll and that is a real result: Brent's continuation-to-active basis printed 2.12 on 31 August and 2.23 on 1 September, having stepped from twenty sessions of exactly zero. A stable, non-zero, same-signed basis across the roll is what a correctly-rolled pair looks like, and it is the evidence that the 31 August step was the roll this document called it rather than a second restatement. The consequence of §9.36 still binds: 28 August COA and 31 August COA are different delivery months and NO day-on-day change may be constructed across them. What moved the price is the point: the largest crude move in the window was not Brent but WTI, +$2.23 on the scored series, eight times Brent's move, on a session whose news was a US strike on an Iranian island and an Iranian missile attack on two Arab countries. Meanwhile Henry Hub's discount to pre-war NARROWED from 5.71% to 4.18% and TTF set a record close. The complex is still pricing a chokepoint rather than a shortage — but the American legs of it, crude and gas alike, both moved toward the war for the first time in several sessions, and that is worth watching rather than concluding on."},
   {"title": "(iii) US inflation impulse — held at 5 (max). The trigger that fired this channel has now failed on TWO CONSECUTIVE closes, which it has never done before.",
    "text": "The 5y5y forward closed 2.2885% on 31 August, below the 2.30% level whose sustained break fired this channel 4→5 on 31 July — and 28 August had already closed at 2.2964%. That is the first time in the regime that the break has survived a second consecutive close, and 2.2885% is the LOWEST close since the upgrade fired. The two prior breaks, 2.2900% on 13 August and 2.2991% on 25 August, were each retraced inside one session; this one was not, and it went lower rather than merely staying below. The score holds and the rule is not moved: the documented downgrade is a sustained close at or below the 2.142% pre-war anchor, still 14.65 bp lower, though that gap narrowed from 15.44. BE10 moved the OTHER WAY — 6.37 bp above its own 2.2569 anchor, WIDENED from 6.10 — so the two compensation measures disagreed on the session, which is itself a reason not to act on either. §9.26 governs and it is worth restating: do NOT redefine the downgrade to the firing level. But the honest statement of the position is uncomfortable and should be made plainly. This channel is scored at its maximum on the strength of a trigger that has now failed twice running, with the documented downgrade fourteen and a half basis points away. The physical impulse is undiminished — TTF at a record close and +123.6% against pre-war, Asia LNG +125.3%, diesel +$1.90 year on year — so the score is not wrong. But the INSTRUMENT it is written on is being pushed below its firing level by monetary policy, not by the war retreating. A third consecutive close below 2.30% would make the gap between the firing rule and the downgrade rule the largest open methodological problem in the document, ahead of §9.49."},
   {"title": "(iv) Treasury stress — held at 5 (max). The downgrade lost its remaining leg, and Threshold B held a second close in the shape it was actually written to detect.",
    "text": "The downgrade requires a 30-year close below 5.00% WITH MOVE below 75, sustained. MOVE closed 75.32 — ENDING the run of NINE consecutive closes below 75 that ran 18 to 28 August, and only the second close at or above 75 since 12 August. The volatility leg is therefore NOT satisfied, for the first time since 17 August. The 30-year closed 5.2423% and the yield leg fails by 24.23 bp, WIDENED from 20.56. §9.15 does not fire for a THIRD consecutive session, and the third state has hardened: the rule describes ROTATION — one leg approaching while the other retreats — but here both legs deteriorated together for the third session running, and this time the deterioration was categorical rather than marginal, because the volatility leg was not narrowed, it was LOST. That third state was first recorded on 21 August; 31 August is its FOURTH occurrence and its THIRD consecutive one. US-inflation remains the nearer of the two market downgrade candidates and the gap between them WIDENED sharply: 14.65 bp against 24.23, from 15.44 against 20.56. Threshold B held its second close and the SHAPE is the finding: the 30-year now clears by 4.23 bp, from 0.56 at the arming, and the 10-year clears by 10.00 bp, from 6.80 — its widest clearance of the regime. Both legs widened. The ordinals are UNCHANGED: six armings, five lapses, ELEVEN states and TEN changes since 29 July, and this is not a new state."},
   {"title": "(v) Political stress — held at 5 (max). The scored series backfilled DOWN by a cent and then went dark for two sessions.",
    "text": "AUTMUSAG's 28 August cell, reported DARK in the last edition, has printed at $4.81 — one cent BELOW the $4.82 of 27 August that this document had been carrying as the last resolved value. It did not print on 31 August or 1 September. The last resolved value is therefore $4.81, 21 cents above the named $4.60 downgrade condition and 6 cents above the $4.75 that fired the upgrade. §9.10 is vindicated a second time and in the other direction: on 14 August two dark sessions backfilled UP and destroyed a downgrade case; here one backfilled DOWN. Neither was predictable from the run, which is exactly why §9.30 forbids reading a trend through dark sessions in either direction. The corroborating evidence continues to point down and the month-on-month figure is corrected: AAA's own page, read on 1 September and stamped 'price as of 8/31/26', has regular at $4.0807 and diesel at $5.6002, both below their week-ago levels, and the diesel month-on-month gain is CORRECTED to +24.74 cents from the +26.4c carried in the last edition, because AAA's month-ago row now reads $5.3528 — a comparison window moving, not a restatement. The divergence is still the signal and there is now a political instrument attached to it: diesel is +$1.90 year on year against regular's +89.22c, the national average has been above $4 a gallon on every day of August, reported as the first time that has ever happened, and the President convened refiners, distributors, the Interior Secretary and the Energy Secretary for 1 September. That meeting is PROSPECTIVE at the cut and no readout exists; nothing in the reporting signals an SPR release, an export restriction or a price control."},
   {"title": "(vi) Escalation risk — held at 5 (max). Iran fired ballistic missiles at American bases in Jordan and the score could not move a point.",
    "text": "The downgrade requires a mediated stand-down and resumed talks. Instead, following the 30 August US strike on Larak Island, Iran ran operation 'Punishment of the Aggressor': ballistic missiles at the King Hussein and Al-Azraq air bases in Jordan on the night of 30–31 August, and a claimed drone attack on Al Minhad in the UAE. Jordan's armed forces confirmed intercepting and destroying eight missiles; Iran's foreign ministry confirmed the targeting; Qatar's foreign ministry condemned Iranian attacks on Jordan and the UAE by name. The UAE denied Al Minhad was hit while confirming its air force engaged a UAV approaching from Iran. The scale is saturated and this is now the reference case for §9.7: escalation has been at 5/5 since 9 July, and an Iranian ballistic-missile attack on American bases on the territory of a treaty partner, a second claimed attack on a Gulf state, the first Gulf-state attribution of an Iranian strike by name, and a presidential promise of retaliation not yet delivered together move the total by ZERO points. A flat 27 does not mean a stable week; it means the instrument is at its stop. Two disciplines applied against over-reading and one against under-reading: the 'heavy damage' assertion is Tier 3 and contradicted by every non-Iranian source, so it is not used; the ABC report of unintercepted missiles is carried as an unresolved conflict with Petra rather than resolved in either direction; the 28–29 July Jordan attack remains a different event and is not reused. Against under-reading: the retaliation has been PROMISED and NOT DELIVERED, and that is the single most consequential open fact on the board."},
  ],
  "stage4Note": (
    "Three thresholds, reported separately from the score. A remains untestable as written; B is ARMED and held a "
    "second close with both legs widening; C is not armed but its structure changed."
  ),
  "stage4": [
   {"title": "Threshold A · a failed-auction test — NOT ARMED, and UNTESTABLE AS WRITTEN (§9.39)",
    "text": "NO coupon auction CLEARED in the window, so nothing is added to the five-auction record; the primary-dealer run on competitive-accepted is unchanged at 12.34, 2.09, 10.90, 10.05 and 12.264, and 12.264% remains the SECOND-highest. The $44bn 7-year SETTLED on 31 August but was auctioned 27 August and is already in that run; Threshold A turns on a clearing, not on a settlement. Its internals were re-verified against primary Treasury data this edition and reconcile exactly: high yield 4.5120%, coupon 4.500%, bid-to-cover 2.50, allotment at the high yield 97.63%; on COMPETITIVE-ACCEPTED of $43.894bn, primary dealers 12.26%, directs 26.96%, indirects 60.78%; on TOTAL AWARD EX-SOMA of $44.000bn, 12.23%, 26.89%, 60.63%. The two bases are not interchangeable and a figure on one must never be compared with a figure on the other. No tail is asserted: Treasury publishes no when-issued level, so a tail is structurally unobtainable from primary data. Two BILL auctions did clear on 31 August and they are NOT a Threshold A input, but the composition is recorded because it is reachable and nobody prints it: the 13-week ($92bn, high rate 3.770%, cover 2.77) took indirects at 51.98% and dealers at 40.50% on competitive-accepted; the 26-week ($79bn, high rate 3.885%, cover 2.63) took indirects at 47.29% and dealers at 43.42% on the same basis, on the same afternoon. Six months of duration is where the bid thinned."},
   {"title": "Threshold B · 30-year above 5.20% WITH 10-year above 4.65% — ARMED, and it HELD a SECOND close",
    "text": "30-year 5.2423%, clearing by 4.23 bp against 0.56 at the arming; 10-year 4.7500%, clearing by 10.00 bp against 6.80 — its widest clearance of the regime. Both legs widened. The ordinals are UNCHANGED and this is not a new state: SIX armings and FIVE lapses, ELEVEN states and TEN changes since 29 July. §9.49 stays OPEN, and the new §9.51 explains why. B armed on 28 August on a bear FLATTENER in which the 30-year contributed 1.25 bp of an 11.14 bp front-end move, which the last edition recorded as a DEFECT in the test. It held on 31 August on a bear STEEPENER in which the 30-year contributed the largest move on the curve — the exact signature B was written to detect. The temptation is to read the second session as vindication and close §9.49. That would be wrong, and the reason is the whole point: one arming was defective and the next was clean, and the written test was met identically in both cases. A test that returns the same answer for two opposite curve signatures is not discriminating between them, which is precisely the original complaint. A second, cleaner occurrence is not evidence about the test; it is a second observation of the same non-discrimination."},
   {"title": "Threshold C · MOVE above 130 — NOT ARMED, but the structure changed",
    "text": "MOVE 75.32 is 54.68 points below C and 39.70 below the 115.02 war high of 26 March. The nine-close run below 75 ENDED at nine, and MOVE is now 1.94 points ABOVE its 73.38 pre-war anchor while the 30-year sits 63.17 bp above its own. For the first time since 17 August BOTH halves are on the same side of their anchors. THE COMPOSITE FIGURE THIS DOCUMENT HAS BEEN PUBLISHING IS THEREFORE RETIRED RATHER THAN UPDATED: 61.91 on 28 August was the SUM of two deviations in OPPOSITE directions, and that construction is undefined once both sit on the same side. Publishing a successor to it would be arithmetic without a referent. The two deviations are reported separately from here — 63.17 bp and +1.94 — and the finding is that the month-long anomaly of a fully normalised expectation of movement around an un-normalised yield closed because volatility ROSE to meet the yield, not because the yield came back."},
  ],
  "crossAsset": (
   "The 31 August session was read as GULF-DRIVEN, layered on the Fed-driven base Chairman Warsh laid at Jackson "
   "Hole on 28 August. Reuters at 08:38 ET, under the headline 'Wall St set for lower open as Middle East clashes "
   "revive rate-hike speculation': the main US stock indexes were on course to open lower 'after military strikes "
   "between the U.S. and Iran drove up oil prices, fanning inflation worries as the interest-rate outlook turns "
   "more hawkish'. Bloomberg the same day: 'Emerging-Market Stocks Fall as Warsh Stokes Fed Rate-Hike Bets'. "
   "Thomas Kikis of Standard Chartered on the keynote: 'He took any chance of a (rate) cut off the table… he "
   "brought about a level of monetary orthodoxy.' PRESS LEVELS ARE NOT ADOPTED and this edition has a fresh reason "
   "for the rule: one widely-syndicated 31 August market wrap prints a Dow close that does not reconcile with the "
   "same day's intraday quotes elsewhere, and describes the 30-year as having 'climbed 5%' where it plainly means "
   "basis points. This document publishes its own Bloomberg series and cites the press only for characterisation. "
   "SEPTEMBER PRICING — THREE INSTRUMENTS, THREE UNIVERSES, NEVER AVERAGED. CME FedWatch: about 60% at the 31 "
   "August open on Reuters' basis, against '41.4% a week ago', and 66% by late morning on Forbes'; no close was "
   "obtainable. Kalshi: 47% hike / 54% hold on its own primary post — which CORRECTS the 48% this document "
   "published in the last two editions, and note that those two legs of a single binary sum to 101%, printed as "
   "Kalshi prints them and NOT normalised, because normalising would invent a number the venue does not publish. "
   "Polymarket: about 69% for ANY 2026 hike, unrefreshed since 28 August. The 28 August CME level is itself "
   "CONTESTED IN THE RECORD at 55.7% and about 59%, same tool and same day; this document has published the 59% "
   "and neither is now preferred. A '62%' Kalshi and a '56%' Polymarket circulate without a dated source and are "
   "NOT published; the live Polymarket pages are JavaScript-rendered and returned nothing to a fetcher, which is a "
   "retrieval failure and not a reading. Calibration for why these are never merged: on 9 August, after the July "
   "jobs miss, Kalshi priced hold at 65%, Polymarket at 63% and CME FedWatch at 55.6% — the same contract, three "
   "venues, a ten-point spread. "
   "THE DATA. The only US data in the window cut AGAINST Friday's: the Dallas Fed Texas Manufacturing Outlook "
   "Survey, released 31 August, ROSE 10.3 points to +11.6 on general business activity, with new orders +15.6 to "
   "22.0, production 16.1 from 10.1 and company outlook 19.2 from 13.4, while employment FELL to 8.0 from 12.2. "
   "That is ONE SESSION after the Chicago Business Barometer FELL 10.5 points to 47.1 — two regional manufacturing "
   "surveys with overlapping fields, opposite signs and near-equal magnitudes. That is flagged as an integrity "
   "problem and is NOT resolved here; the 1 September ISM is the test and it is PROSPECTIVE. Inside Dallas the war "
   "signature is explicit and it is NOT a growth story: raw-materials prices paid 44.1 against a 27.9 series "
   "average and a 76th consecutive positive month, forward prices paid 53.5 from 45.5, while wages and benefits "
   "DECELERATED 9.7 points to 21.1 — a cost-push and margin-squeeze signature, not a demand signature, which is "
   "precisely the transmission this monitor exists to trace. "
   "THE FED CALENDAR, AND WHY 3 SEPTEMBER MATTERS. NO Fed speech, testimony, press release or FOMC communication "
   "dated 29, 30 or 31 August exists: the speeches feed ends with Warsh's 28 August keynote, the press feed with a "
   "27 August enforcement action, and the Board's own calendar carries exactly one entry across those three days, "
   "the G.20 statistical release. The forward calendar is the finding: Governor Michael Barr speaks at 9:05 ET on 1 "
   "September and Governor Christopher Waller gives a Reuters NEXT newsmaker interview at 8:30 ET on 3 September, "
   "and the blackout runs 5 to 17 September — so those are the ONLY two Board-level speaking slots before the "
   "FOMC, and Waller's is an interview format in which he will be asked directly about a September hike six "
   "calendar days, four business days, after Warsh abolished forward guidance. The Beige Book lands 2 September and "
   "payrolls 4 September. Two additions to the hawkish record: the July FOMC vote was 9–3 with Beth Hammack "
   "(Cleveland), Lorie Logan (Dallas) and Neel Kashkari (Minneapolis) dissenting in favour of a 25 bp hike against "
   "a current target range of 3.50–3.75%, and Hammack told CNBC on 27 August 'I don't want to prejudge anything, "
   "but I believe now is the time to act.' GDPNow is 4.6% as of 26 August and the 1 September update is PROSPECTIVE. "
   "TREASURY SUPPLY, AND A PROMISED DOCUMENT THAT DOES NOT EXIST. Treasury release SB0607 of 19 August announced "
   "that the maximum long-end buyback size rises from $2bn to at least $4bn per operation, effective 9 SEPTEMBER "
   "through 4 November, in the 10-to-20-year and 20-to-30-year nominal sectors, and closed by saying 'An updated "
   "tentative Treasury buyback schedule will be released at a later date.' THAT SCHEDULE HAS NOT BEEN PUBLISHED. "
   "Eight days before the new regime begins, its operating calendar does not exist in the public record. No "
   "buyback operation was conducted, announced or scheduled in the window, and the 4 November quarterly refunding "
   "is PROSPECTIVE. The September coupon block has not been announced either — expected 2 or 3 September on the "
   "usual cadence, so its absence is mechanics rather than an anomaly, and NO calendar is inferred from it. "
   "Treasury release SB0618 of 31 August is the Preliminary Annual Report on US Portfolio Holdings of FOREIGN "
   "Securities at year-end 2025; that is the OUTBOUND leg and is NOT the TIC data on foreign holdings of "
   "Treasuries, and it is not used as if it were. Term-premium context, dated and sourced but not new: CNBC on 21 "
   "August reported long-dated yields rising 'as investor jitters over the Treasury Department's extended debt "
   "repurchase program and soaring national debt continued to hover over markets' — the buyback expansion being "
   "read as a signal of STRESS rather than as relief, the reverse of its intended transmission — and the CBO has "
   "raised its annual deficit projection to $2.1 trillion, $200bn above its February expectation. NO term-premium, "
   "long-end or foreign-demand commentary dated 31 August or 1 September was obtainable; that narrative did not "
   "advance. "
   "WAR POWERS — A STATUTORY EXPIRY INTO AN EMPTY CHAMBER. This is a scheduling fact taken from primary sources and "
   "it corrects a premise this document had been carrying. The President's War Powers notification was dated 10 "
   "JULY 2026, following the 7 July strikes the letter describes as 'defensive' and 'limited'. Sixty days from 10 "
   "July is 8 SEPTEMBER 2026, and the statutory 30-day withdrawal extension would run to 8 October. The Senate is "
   "NOT back: its own published floor schedule of 8 August provides for PRO FORMA SESSIONS ONLY on 31 August, 1, 4, "
   "8 and 10 September, and states that when it adjourns on 10 September it 'will next convene at 3:00pm on Monday, "
   "September 14, 2026'. No business is conducted in a pro forma session, so no privileged war-powers motion can be "
   "made and no floor vote can occur — and 8 September is itself a pro forma day, at 1:15 p.m. The House DID return "
   "on 31 August and took no war-powers action. Senator Schiff's resolution, co-sponsored by Kaine, Kim, Merkley "
   "and Van Hollen, has seen no movement: his press page across 19–31 August carries nothing on Iran or war powers. "
   "For context the Senate has voted eleven times on Iran war-powers measures in 2026, most recently on 23 July "
   "when the motion to discharge S.J.Res.180 FAILED 47–49. The executive therefore reaches a statutory expiry with "
   "the chamber that would have to act mechanically unable to act until six days afterwards. That is a schedule, "
   "not a prediction. "
   "THE SPR — TWO PUBLISHED VALUES, STILL UNRECONCILED, NEITHER WITHDRAWN. The conflict is unchanged for a fourth "
   "edition. EIA's weekly series has the SPR at 289.7 million barrels for the week ending 21 August, released 26 "
   "August — down 3.7 million on the week, 40.6% of the 714 mn bbl authorised capacity, and the lowest since 26 "
   "November 1982; the release was re-fetched on 1 September and is unchanged. The DOE Office of Petroleum Reserves "
   "'SPR Quick Facts' page was re-read on 1 September and its own modified-time metadata still reads 24 August: it "
   "continues to publish 'Crude Oil Inventory by Site (as of August 20, 2026)' totalling 294.1 MMB across 61 "
   "caverns — Bryan Mound 142.5, Big Hill 89.1, Bayou Choctaw 32.0, West Hackberry 30.5, split 101.8 sweet and "
   "192.3 sour. The two dates are ONE DAY apart and the two totals 4.4 MMB apart, which is not a physically "
   "plausible one-day drawdown. They are DIFFERENT MEASUREMENT BASES — site-level physical inventory against "
   "weekly reported stocks — so the correct handling is to publish both with their series, vintages and publishers "
   "named, withdraw neither, and compute NO delta. Context that does NOT reconcile arithmetically and for which no "
   "reconciliation is asserted: 172 million barrels were ordered released in March 2026 and the reserve stood at "
   "411 MMbbl on 31 December 2025, which would imply about 239 MMB against current readings near 290. The 2 "
   "September Weekly Petroleum Status Report is PROSPECTIVE and is the next chance to resolve this; it also carries "
   "the retail survey for the week to 31 August. Elsewhere on the supply calendar: the EIA Short-Term Energy "
   "Outlook is due 9 September; no September IEA Oil Market Report or OPEC Monthly Report has been published; and "
   "the eight-country OPEC+ group meets 6 September, having approved a +188,000 b/d September increase on 2 August "
   "that completed the rollback of the 1.65 mn b/d voluntary cut, with delegates telling Bloomberg the group "
   "expects to hold quotas steady for the remainder of 2026."
  ),
 },

 "channels": [
  {"name": "Maritime denial", "score": 5, "state": "max",
   "rationale": "JMIC Update 091, ICOD 301500 UTC, keeps mine danger areas 'still active' and clearance operations continuing, two to three days after the CENTCOM commander declared the internationally recognised routes clear and on the day of the Larak strike — both passages flagged '(No change)'. Two Khasab strikes in three days: Warning 122-26 (29 Aug, inbound, 12 nm N) and Warning 124-26 (31 Aug, outbound, 17 nm E, three projectiles). The 97 count did not move although the first falls inside 091's own window. UKMTO VRA Overview No. 5 is due 4 September and is PROSPECTIVE.",
   "move": "At the cap. The traffic leg did not advance; the reopening leg moved AWAY, on allied paper rather than on this document's inference."},
  {"name": "Oil price shock", "score": 2, "state": "live",
   "rationale": "Brent CO2 $88.37, +$0.27; WTI CL2 +$2.23, eight times Brent's move and the largest crude move of the window. TTF a war-record close at €69.809, the twelfth of the war; Asia LNG ¥3,761, third-highest close of the war; Henry Hub 4.18% below its pre-war anchor, from 5.71%. The Brent basis cleared for the first time since the roll, printing 2.12 and 2.23 on either side of it.",
   "move": "$6.63 below the $95 upgrade, NARROWED from $6.90 — six narrowings in ten readings. $15.89 above the $72.48 downgrade, WIDENED. The only channel with headroom."},
  {"name": "US inflation impulse", "score": 5, "state": "max",
   "rationale": "5y5y 2.2885% — a SECOND consecutive close below the 2.30% that fired the upgrade on 31 July, and the lowest close since it fired. The two prior breaks, 13 and 25 August, were each retraced inside one session; this one was not. BE10 moved the other way, to 6.37 bp above its anchor from 6.10, so the two compensation measures disagreed on the session. Physical impulse undiminished: TTF +123.6%, Asia LNG +125.3%, diesel +$1.90 y/y.",
   "move": "14.65 bp above the 2.142% downgrade anchor, NARROWED from 15.44 — and still the nearer of the two market candidates, by a WIDENED margin of 14.65 against 24.23."},
  {"name": "Treasury stress", "score": 5, "state": "max",
   "rationale": "A BEAR STEEPENER rising monotonically with tenor: 2-year −0.19 bp, 5-year +2.13, 10-year +3.20, 30-year +3.67. The 10-year closed 4.7500% and the 5-year 4.5002%, both NEW WAR-HIGH CLOSES; the 30-year at 5.2423% is NOT a war high (5.3060, 17 Aug) and is the tenth close above 5.24. MOVE printed 75.32, ending nine consecutive closes below 75.",
   "move": "BOTH LEGS GONE. The volatility leg is LOST for the first time since 17 August and the yield leg WIDENED to 24.23 bp from 20.56 — a third consecutive session of both moving away."},
  {"name": "Political stress", "score": 5, "state": "max",
   "rationale": "AUTMUSAG backfilled DOWN to $4.81 for 28 August, a cent below the $4.82 being carried, then DARK on 31 August and 1 September. AAA regular $4.0807 and diesel $5.6002, both below week-ago; diesel still +24.74c on the month, corrected from +26.4c. The national average has been above $4 every day of August, and the President convened refiners for 1 September — PROSPECTIVE at the cut.",
   "move": "21 cents above the $4.60 condition, UNRESOLVED. No trend is read through dark sessions in either direction (§9.30)."},
  {"name": "Escalation risk", "score": 5, "state": "max",
   "rationale": "Iran fired ballistic missiles at the King Hussein and Al-Azraq air bases in Jordan on 30–31 August under operation 'Punishment of the Aggressor' — Tier 1 corroborated by Jordan's Petra, Iran's own foreign ministry and Qatar's MFA — and separately CLAIMED a drone strike on Al Minhad, which the UAE DENIED while confirming it engaged a UAV approaching from Iran. Trump promised retaliation and had not delivered it at the cut. centcom.mil has published nothing since 15 August and no combat release since 29 July.",
   "move": "At the cap. The downgrade needs a mediated stand-down and resumed talks; Qatar moved from mediator to critic in four days."},
 ],
 "scoreTotal": (
  "TOTAL 27 / 30 — CRISIS band (22–30), held for a SIXTEENTH consecutive edition. FIVE of six channels sit at the "
  "cap, so the score can register NEITHER an Iranian ballistic-missile attack on American bases in a treaty partner "
  "NOR two new war-high Treasury closes on the same day, NOR a war-record TTF close, NOR a Combined Maritime Forces "
  "product re-issued after the clearance claim with its mine language unaltered. It equally cannot register what "
  "cut the other way: no casualties were reported at either Jordanian base, Jordan reported intercepting and "
  "destroying eight missiles, and the promised American retaliation had not been delivered at the cut. None of "
  "those three is a settled finding — the first is an absence of reporting rather than a confirmed nil, and the "
  "second is contested by ABC's two Jordanian security sources. A flat 27 is an instrument at its stop, in both "
  "directions. Read the composition, not the total."
 ),
 "whatsChanged": {
  "title": "4 · What has changed since the 31 August edition",
  "items": [
   "The Jordan claim is corroborated as an EVENT by three Tier 1 sources — Petra on eight missiles intercepted and destroyed, Iran's foreign ministry confirming the targeting, Qatar's MFA condemning attacks on Jordan and the UAE by name. The largest open fact in the last edition, RESOLVED in part. The remaining core is narrow: ABC has two Jordanian security sources saying some missiles were NOT intercepted, and no US or Jordanian BDA or casualty figure was obtained.",
   "JMIC Update 091 landed and does NOT endorse the clearance claim. A fresh product issued 30 August, two to three days after the Cooper declaration and on the day of the Larak strike, keeping mine danger areas 'still active' and clearance operations continuing, both flagged '(No change)'. A three-edition watchlist item RESOLVED, against the claim — FLOW, not STOCK, now on allied paper rather than on this document's inference.",
   "The long end sold off in the shape the Treasury test was written for. A BEAR STEEPENER rising monotonically with tenor: 2-year −0.19 bp, 5-year +2.13 to a second consecutive war-high close, 10-year +3.20 to a war-high close and its first since 31 July, 30-year +3.67; BE10 +0.27. Real yield and term premium, not compensation. Threshold B HELD a second close with both legs widening — 4.23 bp from 0.56 and 10.00 from 6.80. Ordinals UNCHANGED at eleven states, ten changes.",
   "MOVE broke back above 75 and the Treasury downgrade lost its remaining leg. 75.32, +4.35, ending the run of NINE consecutive closes below 75; the yield leg widened from 20.56 to 24.23 bp. §9.15 does not fire for a THIRD consecutive session, and a leg was LOST rather than narrowed. The month-long anomaly closed from the wrong end: volatility 1.94 above its anchor and the 30-year 63.17 bp above its own — same side, first time since 17 August.",
   "5y5y closed below 2.30% for a SECOND CONSECUTIVE session — the first time the break has held two closes. 2.2964% then 2.2885%, the lowest since the upgrade fired; the two prior breaks, 13 and 25 August, were each retraced in one session. The most adverse fact here for the monitor's own scoring. The channel holds at 5 because the downgrade is 14.65 bp lower and §9.26 forbids moving the rule — a third close would make it the largest open methodological problem in the document.",
   "UKMTO became PARTLY obtainable by a varied method. The listing pages are client-hydrated and will never serve product to a fetcher, but the media PDFs fetch once the file revision token is known. Two Tier 1 warnings and JMIC 091 were recovered and 122-26's provenance CORRECTED — issued 30 August, source military authorities, vessel inbound; Advisory 123-26 and Warnings 125/126-26 stay NOT OBTAINED. New pitfall §9.50: a NOT OBTAINED on a JS-rendered site is a statement about the METHOD, which must be varied before the negative is published again.",
   "The Khamenei question is RESOLVED and the suspended clock retired. Trump named Mojtaba Khamenei as the incumbent on 26 August (Tier 1); Tasnim published his 28 August message (Iranian state); Al Jazeera, NBC, TIME and Iran International have carried the succession since March, with no rebuttal from any tier. The Friday/Sunday conflict resolves: there were two messages, and the 'imaginary dualism' line belongs to Friday 28 August. An inherited clock of this document's own is RETIRED rather than repeated. And a Tier 1 negative of its own: english.khamenei.ir carries a 1 January 2026 dateline and nothing later — the Leader's platform has published nothing since two months BEFORE the war began.",
   "Both the diplomatic and the economic tracks stopped, and a statutory clock runs out into an empty chamber. Nothing from Oman or Iran after 29 August, nothing from the White House on negotiations after 27 August, no OFAC action or Treasury release on Iran after 28 August, still no Chinese bank and no UAE embargo decree at fourteen days. The 60-day War Powers clock from the 10 July notification expires 8 SEPTEMBER and the Senate is in pro forma session only until 14 September — 8 September is itself a pro forma day. A statutory expiry arrives six days before the chamber that would act can act. Primary source, not inference.",
  ],
 },
 "scenarios": [
  {"name": "Deal collapse — talks stall on terms", "p": 40,
   "desc": "The corridor framework exists on paper and dies over geometry, fees and sovereignty; the blockade and the counter-blockade both continue.",
   "shift": "−2, and a thirteenth edition as the modal case. Still modal, but an exchange of fire reaching American bases in Jordan makes 'collapse over geometry and fees' a less complete description of the state."},
  {"name": "Return to full war", "p": 23,
   "desc": "Sustained US or Israeli strike campaign inside Iran with Iranian reprisals against US bases and Gulf infrastructure.",
   "shift": "+2, a second consecutive rise. Iranian ballistic missiles were fired at US bases in Jordan and the President said 'there will be a response'. It is +2 and not more BECAUSE the retaliation had not been delivered at the cut, no casualties were reported, and Trump himself called it 'a relatively little war'."},
  {"name": "Contained but violent", "p": 21,
   "desc": "The present state persists: blockade, counter-blockade, periodic strikes on shipping, no reopening and no general war.",
   "shift": "−3. The escalation lines gained six between them; three points came from here, two from deal collapse and one from mediated pause. It still describes the maritime record — two Khasab strikes in three days — but no longer the state-on-state record."},
  {"name": "Regional relapse", "p": 13,
   "desc": "The war widens to Gulf states directly — UAE, Saudi or Qatari territory or infrastructure struck.",
   "shift": "+4, and this is the line the window actually moved. The last edition held it deliberately because Jordan is not in its stated population. The UAE is: Iran claimed a drone attack on Al Minhad, the UAE confirmed engaging a UAV approaching from Iran, and Qatar condemned attacks on the UAE by name — all Tier 1."},
  {"name": "Mediated pause", "p": 3,
   "desc": "A verified stand-down, resumed talks and a reopening on published terms.",
   "shift": "−1, a third consecutive cut and a new low for the war. Qatar went from Tehran on 27 August to condemning Iran on 31 August; Bessent set maximalist conditions on television; Oman and Iran have both been silent since 29 August."},
 ],
 "scenarioShift": (
  "Sums to 100. Deal collapse and full war together carry 63%, UNCHANGED — but the composition beneath that number "
  "moved: the three lines involving continued or widening violence now carry 57%, UP from 54%, and mediated pause "
  "is at its lowest reading of the war. The weight behind each shift differs and is named rather than blurred. "
  "Full war and contained-but-violent move on TIER 1 facts — Petra on eight missiles destroyed in Jordanian "
  "airspace, and Iran's MFA and Qatar's MFA on missiles fired at US bases in Jordan. Regional relapse moves on a "
  "WEAKER basis and is stated as such: the UAE MoD confirmed engaging a UAV approaching from Iran and Qatar named "
  "the UAE, but the STRIKE claim is Iranian, Tier 3 and DENIED by the UAE, so the +4 records a demonstrated "
  "willingness to reach Gulf airspace, NOT a strike on Gulf territory. Mediated pause moves on Tier 2 and on two "
  "negatives. The 'heavy damage' assertion carries NO weight anywhere. If the promised American retaliation is "
  "delivered, the full-war line moves again; if it is not delivered inside a week, this reading is at the top of "
  "its range."
 ),
 "watchlist": [
  "Whether the promised American retaliation is delivered, and against what. Trump said 'we're going to hit them hard' on 31 August; nothing had been executed at the cut. The largest open fact on the board, and the reason the full-war line moved 2 points rather than 10. A strike inside Iran answering an attack on a third country's territory is a different war from the one fought since 29 July.",
  "Whether any US or Jordanian source publishes impact points, a BDA or a casualty figure for King Hussein and Al-Azraq — and whether Petra's account survives ABC's two Jordanian security sources saying some missiles were not intercepted. Petra states EIGHT INTERCEPTED and gives NO launch total, so no interception RATE follows from it. Whether missiles landed on a base hosting US forces is not a detail.",
  "Whether 5y5y closes below 2.30% a THIRD consecutive session. It closed below on 28 and 31 August, the first time the break has held two sessions. A third close would make the gap between the firing rule and the documented downgrade the largest open methodological problem in this document, ahead of §9.49.",
  "Whether MOVE holds above 75 and whether Threshold B holds a third close. MOVE broke a nine-close run at 75.32; B now clears by 4.23 and 10.00 bp. A second close above 75 would end the volatility leg as a live candidate rather than a lapse, and B at these margins is no longer decided by fractions of a basis point — itself a change of regime.",
  "The 1 September ISM, JOLTS and GDPNow; the 2 September Beige Book and WPSR; Waller at Reuters NEXT on 3 September; payrolls 4 September — all PROSPECTIVE at the cut. The ISM adjudicates between Chicago at 47.1 and Dallas at +11.6. The WPSR is the next chance at the SPR conflict — EIA 289.7 mn bbl against DOE 294.1 MMB, both standing. Waller is one of only two Board slots before the blackout.",
  "The 8 September War Powers expiry into a pro forma Senate; Treasury's still-unpublished buyback schedule eight days before the $4bn regime starts on 9 September; UKMTO VRA Overview No. 5 on 4 September; OPEC+ on 6 September. Four dated events inside a week, two turning on a promised document that does not exist.",
 ],
 "sourceLog": {
  "tier1Market": (
   "Tecity Bloomberg extract, US Iran BBG Data.xlsx, 1 September pull, 173 rows to 1 September 2026 — ALL scored "
   "prices, yields, spreads, volatility and both gasoline series. No market figure in this document comes from the "
   "web. Every row of the live tape carries the Bloomberg ticker it is drawn from, taken from the extract's own "
   "row-0 header scan and never hardcoded: CO2/COA Comdty (Brent listed and active), CL2/CLA Comdty (WTI), NGA "
   "Comdty (Henry Hub), TZTA Comdty (TTF), JGLA Comdty (Japan/Asia LNG), USGG2YR/5YR/10YR/30YR Index, USYC2Y10 "
   "Index (2s10s), USGGBE10 Index, USGG5Y5Y Index, MOVE Index, VIX Index, DXY Index, SOFRRATE Index, AUTMUSAG "
   "Index (scored gasoline) and USRFRUSA Index (DOE corroboration)."
  ),
  "tier1News": (
   "Primary documents read directly: JMIC Advisory Note UPDATE 091 (ICOD 301500Z August) and UKMTO Warnings 122-26 "
   "and 124-26, all obtained as primary PDFs on 1 September; Petra (Jordan News Agency), Jordan Armed Forces "
   "spokesman, 31 August 06:41; the Iranian Ministry of Foreign Affairs statement via Mehr, 31 August; the Qatar "
   "Ministry of Foreign Affairs statement, 31 August; the UAE Ministry of Defence and Ministry of Foreign Affairs; "
   "@CENTCOM's 31 August mine statement relayed on the record; centcom.mil's public-releases index, read direct, "
   "for the negative; the Federal Reserve Board speeches and press feeds and the Board calendar JSON; the Treasury "
   "press-release index and api.fiscaldata.treasury.gov's auctions query for the 7-year and bill internals on both "
   "denominators; the Senate floor schedule of 8 August for the pro forma calendar; ofac.treasury.gov recent "
   "actions; the Dallas Fed Texas Manufacturing Outlook release; the Atlanta Fed GDPNow page metadata; the EIA "
   "Weekly Petroleum Status Report highlights re-fetched 1 September; the DOE SPR Quick Facts page; gasprices.aaa.com "
   "read direct 1 September; fm.gov.om's Statements page and the 25 August Oman–Iran joint statement read in full; "
   "and the Baltic Exchange tanker report for week 35."
  ),
  "tier3": (
   "Tier 2 — reputable wire or press, used for characterisation and for the damage contradictions: Reuters, "
   "Bloomberg, CNBC, AP, ABC, CBS, Fox, Al Jazeera, Stars and Stripes, USNI News, The National, Gulf News, Forbes, "
   "Kalshi News, Washington Post, TankerMap and IMF PortWatch. Tier 3 — state media or a relayed claim, "
   "corroborated against Tier 1 before it is used for anything market-moving: IRNA (the Qeshm governor's Larak "
   "casualty figure, 31 August, and Makizadeh on the bulk-carrier seizure), IRIB and Fars via Western press, "
   "Tasnim (28 August), and Nour News via Reuters for the NIOC statement. NONE moves a probability on its own, and "
   "the 'heavy damage' assertion is contradicted by every non-Iranian source. NOT OBTAINED, with the query stated: "
   "any US, CENTCOM, Pentagon or Jordanian battle-damage assessment, casualty figure or interception count for King "
   "Hussein and Al-Azraq; any US BDA for Larak; any US acknowledgement of the IRGC's claimed drone shoot-down; any "
   "US strike inside Iran dated 31 August or 1 September; any mine count or allied comment on Bloomberg's 80–150 "
   "residual estimate; JMIC Update 092; UKMTO Warnings 125-26 or 126-26 and the primary PDF of Advisory 123-26; the "
   "vessel name, IMO and flag of the bulk carrier Iran claims to have seized; any AMARA update since 19 August; "
   "Windward's Hormuz brief and any LSEG transit figure; any named, dated broker war-risk quote; any Iranian "
   "corridor statement after 29 August, Omani publication after 29 August, readout of the Qatari PM's Tehran visit, "
   "or US negotiations statement after 27 August; any OFAC action or Iran-related Treasury release after 28 August; "
   "any UAE decree for the embargo announced 18 August, now fourteen days old; any CME FedWatch close for 31 "
   "August or dated Kalshi or Polymarket reading — the live Polymarket pages are JavaScript-rendered and returned "
   "nothing, a METHOD-BOUND negative that §9.50 requires be varied next edition; and any content whatsoever dated "
   "1 September 2026, since the US session had not begun at the cut."
  ),
 },
 "protocol": [
  {"step": "Refresh and integrity-check the extract",
   "detail": "Never build an edition off a stale extract: check the file timestamp AND parse the sheet. This edition the extract carries a 1 September row against the 31 August row the last edition ran on, and the 31 August row has settled into a genuine close."},
  {"step": "Run all THREE integrity checks, then the backfill check in both directions",
   "detail": "Row-level, field-level identical-value at each series' own published precision, and the continuation-versus-active BASIS check. ALL THREE CLEAR this edition — the first clean sweep in three — and the basis check clears as a POSITIVE result, a stable non-zero basis on both sides of the roll being the evidence that the 31 August step was a roll and not a second restatement. The two-way backfill test then fired on FOUR cells and two were consequential: MOVE backfilled at 75.32 and ENDED a nine-close run below 75, removing a downgrade leg, and AUTMUSAG backfilled a cent BELOW the value being carried."},
  {"step": "Compute deltas and test every trigger, then re-sort before asserting any rank",
   "detail": "d/d, w/w five rows back, and versus pre-war; explicit trigger tests for the four market channels plus Stage-4 A, B and C. Run min, max and last-prior-occurrence on the full column before writing ANY superlative — it is what established two war-high closes and a war-record TTF close this edition, and what corrected 'VIX sixth-lowest' to EIGHTH and 'the eleventh close above 5.24' to the TENTH."},
  {"step": "Verify the news, re-verify what was inherited, and VARY THE METHOD on a repeated negative",
   "detail": "Every claim needs a named source and an exact date, and negative claims decay fastest of all. State the exact query behind every negative, say NOT OBTAINED rather than estimating, and distinguish NOT OBTAINED from PROSPECTIVE. New this edition: a NOT OBTAINED on a JavaScript-rendered site is a statement about the METHOD, not the source, and the method must be varied before the same negative is published a second time — doing so recovered three Tier 1 maritime documents and retired a suspended clock."},
  {"step": "Build, then QA in three passes, and measure the typography",
   "detail": "A numeric harness against the dataframe — 254 independent checks this edition, all passing; an adversarial PROSE pass by a reviewer with no access to the source data, run TWICE because fixing introduces defects, returning about fifty then eleven; and a VISUAL render, which is not optional. Re-run the numeric harness AFTER the prose fixes, and balance the bold tags in every fragment after every edit. The harness now also asserts the rendered bold ratio and the headline length, both of which had drifted."},
  {"step": "Deliver both documents",
   "detail": "The edition and the annex go into the project root together; a file that is not committed never reaches the reader. The annex does not go into the dashboard's pdf/ folder, because the score-history script regexes a score sentence out of every PDF there and the annex has none — it goes in annex/, where the manifest pairs it to its date."},
 ],
 "methodology": {
  "scale": (
   "Shock-score scale. Six transmission channels — maritime denial, oil price shock, US inflation impulse, "
   "Treasury stress, political stress and escalation risk — each scored 0–5 and summed to 0–30. Bands: 0–7 watch, "
   "8–14 stress, 15–21 systemic-risk watch, 22–30 crisis. Maritime denial and escalation risk are event channels; "
   "the other four are market channels scored on CONFIRMED CLOSES only. No market channel moves on an intraday "
   "print, so the 1 September snapshot in this document moves nothing — including two more war-high yield prints, "
   "a TTF mark above the record close set the day before, and 5y5y ticking back up to 2.2947%."
  ),
  "scaleCap": (
   "The saturated scale, and it fails in BOTH directions. FIVE of the six channels are at 5; only oil, at 2, is "
   "not. Further geopolitical deterioration cannot raise the score, so this edition could register neither an "
   "Iranian ballistic-missile attack on American bases in a treaty partner nor two new war-high Treasury closes on "
   "the same day. It equally could not register the improvements. A flat 27 is an instrument at its stop, not a "
   "stable week, and the composition must be read with the same energy either way."
  ),
  "integrity": (
   "Data integrity this edition. Three checks run every time and all three CLEARED — the first clean sweep in "
   "three editions. The row-level check clears decisively: not one of the fourteen scored fields the last edition "
   "published as a 31 August intraday is identical to its settled value, and the row additionally carries MOVE, "
   "VIX and Asia LNG where the snapshot had blanks. The field-level identical-value check clears, run at the "
   "precision each series is published to. Its structural caveat is restated anyway, because it must be restated "
   "every time the check clears: it is a DAY-ON-DAY test and is therefore structurally incapable of seeing a "
   "restatement that moves a whole COLUMN across many sessions at once, so a CLEAR is never an all-clear on the "
   "data. The basis check clears as a POSITIVE result: the Brent continuation-to-active basis printed 2.12 on 31 "
   "August and 2.23 on 1 September, having stepped from twenty consecutive sessions of exactly zero, and a stable, "
   "non-zero, same-signed basis on both sides of the step is the affirmative evidence that the step was the "
   "contract roll this document identified rather than a second restatement. The consequence still binds: 28 "
   "August and 31 August active-contract prices are DIFFERENT DELIVERY MONTHS, so no day-on-day change may be "
   "constructed across that boundary, and the four active prices withdrawn last edition stay withdrawn. The "
   "reconciliation of the 31 August snapshot is a NEAR-ONE-DIRECTIONAL miss with NO EXCLUSIONS — the first clean "
   "table in three editions — and one reading is withdrawn by name: 'the 31 August intraday is short by 0.17 bp "
   "and would, on a close, be a SIXTH lapse' is withdrawn, because the 30-year settled CLEARING by 4.23 bp."
  ),
  "gasoline": (
   "Gasoline series, and a denominator warning that covers THREE series rather than two. AUTMUSAG (AAA all-grades "
   "retail pump, daily, one-day lag) is the SCORED reference and preserves the $3.52 pre-war anchor, the $4.75 "
   "level that fired the upgrade and the $4.60 downgrade condition; it last RESOLVED at $4.81 on 28 August and is "
   "dark on 31 August and 1 September. USRFRUSA (DOE regular-grade retail spot, weekly, surveyed Mondays) is "
   "CORROBORATION ONLY, last printing $4.085 for the week surveyed 24 August. AAA's own published headline is a "
   "THIRD series, read direct on 1 September from a page stamped 'price as of 8/31/26', at regular $4.0807 and "
   "diesel $5.6002. The three are never compared with one another. The month-on-month diesel figure was CORRECTED "
   "this edition from +26.4c to +24.74c because AAA's month-ago row now reads $5.3528 — a rolling comparison "
   "window moving, not a restatement — and diesel remains 21.57 cents below the all-time record of $5.8159 set on "
   "19 June 2022, four years before this war, which must never be described as a war high."
  ),
  "anchor": (
   "Pre-war anchor (27 February 2026 close), re-verified field by field this edition and unchanged on all "
   "seventeen fields: Brent $72.48, WTI $67.02, 2-year 3.3749%, 5-year 3.5017%, 10-year 3.9375%, 30-year 4.6106%, "
   "2s10s +55.64 bp, 5y5y 2.142%, 10-year breakeven 2.2569%, MOVE 73.38, VIX 19.86, DXY 97.608, gasoline (AAA) "
   "$3.52, gasoline (DOE) about $2.94, Henry Hub $3.063, TTF €31.23 and Asia LNG ¥1,669. Hysteresis governs every "
   "channel: upgrades fire on a sustained break, downgrades require a sustained reversal past a WIDER threshold. "
   "It faces its sharpest test of the war here, because the 5y5y forward has now closed BELOW its own firing level "
   "on two consecutive sessions where the two earlier breaks were each retraced inside one session — and the "
   "channel still holds at 5, because the documented downgrade is 14.65 bp lower and the rule is NOT moved to meet "
   "the trigger."
  ),
  "intraday": (
   "Intraday caveat, and the three open methodological items. The 1 September row is a Singapore-morning mark "
   "taken before a US cash session that had not begun at the cut; it scores nothing, and every US publication "
   "dated 1 September is PROSPECTIVE rather than unobtained. Three items are DISCLOSED RATHER THAN DECIDED. First, "
   "the oil channel's downgrade is written as a mediated pause AND 'a close' at or below $72.48 while its upgrade "
   "requires a SUSTAINED break, so as written the downgrade is easier to trip than the upgrade; it is $15.89 away "
   "and not live, so the asymmetry is disclosed rather than settled under time pressure. Second, Threshold B's "
   "long-end LEVEL versus long-end CONTRIBUTION question: B armed on 28 August on a bear flattener in which the "
   "30-year contributed 1.25 bp of an 11.14 bp move, and held on 31 August on a bear steepener led entirely by the "
   "long end — the written test was met identically in both cases, and a test that returns the same answer for two "
   "opposite curve signatures is not discriminating between them. Third, and rising: the US-inflation channel is "
   "scored at its maximum on a trigger that has now failed on two consecutive closes. A third consecutive close "
   "below 2.30% would make the distance between the firing rule and the downgrade rule the largest open "
   "methodological problem in this document, ahead of Threshold B. It is flagged now so that it is not discovered "
   "late."
  ),
 },
}
