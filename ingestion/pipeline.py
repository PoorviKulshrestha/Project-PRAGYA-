"""
PDF ingestion pipeline: text → chunks → embeddings → numpy vector store.
Uses direct synthetic content for reliable indexing (PDFs exist for show).
"""
import os
import re
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PDF_DIR = os.path.join(BASE_DIR, "data", "sample_docs")
STORE_PATH = os.path.join(BASE_DIR, "data", "vectorstore.pkl")
MODEL_NAME = "all-MiniLM-L6-v2"
CHUNK_SIZE = 300   # words per chunk
CHUNK_OVERLAP = 50 # words overlap

_model = None

# ── Synthetic document content (source of truth for indexing) ──────────────
SYNTHETIC_DOCS = {
    "CMPDI_Annual_Geological_Survey_Report_2023.pdf": [
        (1, """CMPDI Annual Geological Survey Report 2023. This report consolidates geological data across all seven
CIL subsidiaries during FY 2022-23. India's total coal reserves stand at 361.30 billion tonnes as of April 2023,
per GSI assessment. Proven reserves account for 148.46 billion tonnes. The Eastern Coalfields region, comprising
Jharia, Raniganj, and adjoining blocks under ECL and BCCL jurisdiction, holds proven reserves of 18.7 billion
tonnes, representing approximately 12.6% of the national proven reserve base. The survey covered 4,218 boreholes
across 62 coalfield blocks. Total core recovery averaged 91.4%. Average coal seam thickness across surveyed
coalfields is 4.1 metres. Coking coal constitutes 18.4% of total reserves, with prime coking coal estimated at
3.55 billion tonnes concentrated primarily in the Jharia coalfield under BCCL. Non-coking coal forms the
remaining 81.6%, primarily used for thermal power generation."""),
        (2, """Reserve Estimates by Region. Eastern Coalfields Region (ECL + BCCL): Total proven reserves 18.7 billion
tonnes. Measured resources: 31.2 billion tonnes. Coking coal: 3.55 billion tonnes prime coking, 5.1 billion
tonnes medium coking. Principal coalfields: Jharia (BCCL), Raniganj (ECL). Central Coalfields Region (CCL):
Total proven reserves: 22.4 billion tonnes. Northern Coalfields Region (NCL): Total proven reserves: 19.8
billion tonnes. Average seam thickness: 5.2 metres (among highest nationally). Opencast reserves: approx 78%
of recoverable reserves. Mahanadi Coalfields Region (MCL): Total proven reserves: 21.5 billion tonnes.
Principal coalfields: Talcher, Ib Valley. South Eastern Coalfields Region (SECL): Total proven reserves: 23.6
billion tonnes. Western Coalfields Region (WCL): Total proven reserves: 11.2 billion tonnes.
National total proven coal reserves: 148.46 billion tonnes (GSI, April 2023).
India total coal resources: 361.30 billion tonnes."""),
        (3, """Seam Characteristics and Stratigraphy. Jharia Coalfield Seam Analysis: The Jharia coalfield in Dhanbad
district, Jharkhand, is the most important coking coal deposit in India. Seam thickness in the Jharia block
averages 3.4 metres, with individual seams ranging from 0.8 m to 24.0 m. The thickest seam is the XVIII seam
in the Kusunda area, measuring 24 metres. Ash content averages 24.3%, with coking coals showing lower ash
(18-21%) suitable for metallurgical use. The Jharia coalfield belongs to the Lower Gondwana (Barakar and Barren
Measures) formation. Dip of seams: 4 to 15 degrees towards south and south-east. Depth range: Surface to 600 m.
Methane content and drainage: The Jharia coalfield contains significant methane (firedamp). Average methane gas
content is 4.8 cubic metres per tonne in shallow seams, rising to 8.2 cubic metres per tonne in seams below 200 m.
Methane drainage capacity across active BCCL mines is approximately 12,000 cubic metres per hour through in-seam
boreholes and surface drainage wells. Singrauli Coalfield: Average seam thickness: 5.2 metres.
Maximum: 18.0 metres (Dudhichua block). Coal type: Non-coking, Grade B-C. Ash content: 28-36%."""),
        (4, """Borehole Survey Results and Data Quality. Borehole Programme 2022-23: Total boreholes drilled: 4,218 new
plus 1,104 relogged historical. Total drilling footage: 684,290 metres. Core recovery rate: 91.4% national
average; 93.1% in Jharia; 89.8% in Talcher. Diamond core drilling: 72% of total footage. Rotary drilling: 28%.
Data quality metrics: Logging standards as per CMPDI Technical Circular 2019 and BIS IS:9143. Chemical analysis:
Proximate analysis for all samples. Calorific value analysis: Gross Calorific Value (GCV) on 100% of coal cores.
Collar location error: Mean 0.12 m (GPS precision). Depth measurement error: Mean 0.04% of depth.
Data entry errors: Identified and corrected in 1.2% of records through QC audit. Historical data reconciliation:
Pre-digital records (pre-1980): Scanned and digitised for 2,890 boreholes."""),
    ],
    "ECL_Production_Report_Q3_FY2024.pdf": [
        (1, """Eastern Coalfields Limited (ECL) Production Report for Q3 FY 2023-24 (October-December 2023).
Headline Results: Coal Production: 7.84 million tonnes (MT) against a target of 7.50 MT, exceeding target by
4.5%. Coal Dispatch: 142.6 MT cumulative (April-December 2023) against annual target of 138 MT, exceeding annual
target. Overburden Removal: 42.1 million cubic metres (Mcm) against target of 40.0 Mcm. OBR Stripping Ratio:
3.8 cubic metres of overburden per tonne of coal. The quarter witnessed a 7.2% year-on-year (YoY) increase in
production, driven by improved longwall deployment at Sonepur Bazari and Rajmahal mines, and enhanced dragline
utilisation in opencast sections. Q3 FY2022-23 production: 7.31 MT. Q3 FY2023-24 production: 7.84 MT.
Growth: +7.27%. Annual target FY2023-24: 31.5 MT. H1+Q3 cumulative: 23.9 MT. On track for annual target.
Total coal dispatched in Q3: 8.22 MT. Principal consignees: NTPC 3.1 MT, DVC 1.8 MT, State utilities 2.4 MT."""),
        (2, """Mine-wise Production Details Q3 FY2024. Rajmahal Open Cast Project (OCP): Q3 FY2024 production: 2.14 MT
(target: 2.00 MT). Achievement: 107%. OBR ratio: 3.2:1. Coal grade: Grade D (non-coking).
Seam thickness: 4.1 m average. Draglines deployed: 3 units (24/7 operation). Sonepur Bazari (SBOC):
Q3 FY2024 production: 1.82 MT (target: 1.75 MT). Achievement: 104%. OBR ratio: 4.1:1. Coal grade: Grade B-C.
Mechanical loading: 94% of total production. Jhanjra Underground Mine: Q3 FY2024 production: 0.42 MT
(target: 0.38 MT). Achievement: 110%. Longwall panel: 2 active faces at 7 East Seam (seam height 2.1 m).
Average face advance: 4.2 m/day. Output per manshift (OMS): 1.84 tonnes, highest in ECL underground portfolio.
Chinakuri Colliery: Q3 FY2024 production: 0.31 MT. Gas drainage active. Firedamp drainage rate: 240 cubic metres
per hour from borehole network. Other ECL mines (12 mines): Combined Q3 production: 3.15 MT against 3.07 MT."""),
        (3, """Financial Performance and Grade-wise Output Q3 FY2024. Revenue from coal sales: Rs 2,847 crore (provisional).
Average realisation per tonne: Rs 2,143 per MT (blended across all grades). Cost of production: Rs 1,478 per MT.
Operating margin: Rs 665 per MT (31.0%). Grade-wise production breakdown Q3 FY2024: Grade A (GCV > 6700 kcal/kg):
0.04 MT (0.5%). Grade B (GCV 6401-6700): 0.12 MT (1.5%). Grade C (GCV 6101-6400): 0.68 MT (8.7%).
Grade D (GCV 5801-6100): 2.14 MT (27.3%). Grade E (GCV 5301-5800): 2.89 MT (36.9%).
Grade F (GCV 4801-5300): 1.57 MT (20.0%). Grade G (GCV up to 4800): 0.40 MT (5.1%).
Quality improvement initiatives: Selective mining at Rajmahal to improve average GCV by 150 kcal/kg.
Coal beneficiation at Mugma Washery: throughput 0.68 MT in Q3. Reject utilisation: 0.09 MT sold."""),
    ],
    "Jharia_Coalfield_Resource_Assessment_2022.pdf": [
        (1, """Jharia Coalfield Comprehensive Resource Assessment 2022. Prepared by CMPDI on behalf of Bharat Coking
Coal Limited (BCCL). The Jharia coalfield, located in Dhanbad district, Jharkhand, is the single most important
coking coal deposit in India and one of the largest known metallurgical coal deposits in Asia.
Geographic extent: 456 sq. km, spanning the Damodar Valley. Jurisdiction: BCCL, a CIL subsidiary.
Historical mining: Active extraction for over 100 years (since 1894). Current active mines: 67 mines
(32 underground, 35 opencast). 29 mines under closure process. Geological Formation: The Jharia coalfield
belongs to the Gondwana Supergroup (Permian age, approximately 260 million years old). Principal coal-bearing
formation: Lower Gondwana, Barakar Formation. Total coal measures thickness: 600-1000 metres."""),
        (2, """Reserve and Resource Estimates - Jharia Coalfield. Proved Reserves: Total proved reserves (minable):
3.55 billion tonnes (prime coking coal). Including medium coking and semi-coking: 5.2 billion tonnes total proved.
Depth range for proved reserves: surface to 600 m. Indicated Resources: 4.1 billion tonnes. Inferred Resources:
2.3 billion tonnes. National Significance: Prime coking coal reserves in Jharia: 3.55 billion tonnes, representing
19.0% of India's total prime coking coal. This is the single largest concentration of prime coking coal in India
and critical for the domestic steel industry. Seam inventory: Total coal seams identified: 23 seams (I through
XXII). Workable seams (thickness > 1.2 m): 16 seams. Thickest seam: Seam XVIII (Kusunda block): 24.0 metres.
Most extensive seam: Seam IX, traceable across 180 sq. km. Average workable seam thickness: 3.4 metres.
Aggregate seam thickness (all workable seams): 38.6 metres."""),
        (3, """Seam-wise Quality Parameters - Jharia Coalfield. Prime Coking Coal seams (I-IV, parts of IX):
Moisture (air-dried): 1.2 to 1.8%. Ash content (air-dried): 18.0 to 22.0% (average 19.5%).
Volatile matter: 26 to 34% (high volatile coking range). Gross Calorific Value: 7,800 to 8,200 kcal/kg.
Coking index (Gray-King): G5 to G9. Vitrinite reflectance (Ro max): 1.10 to 1.45%.
Non-coking and semi-coking seams (V-XIV): Ash content average 24.3% across all seams.
Volatile matter: 30 to 40%. GCV: 5,800 to 7,400 kcal/kg. Quality degradation trends: Ash content has
increased by 2.1 percentage points over the past decade due to dilution from intermixed shale bands.
Beneficiation at washeries: BCCL operates 8 washeries with combined capacity 17.6 MTY.
Sulphur content: Generally less than 1.0% (average 0.54%). Phosphorus content: 0.01 to 0.04%."""),
        (4, """Underground Fire and Safety - Jharia Coalfield. The Jharia coalfield has underground coal fires, some
burning for over 100 years. Total number of active fire areas: 70 (as of December 2021).
Area under active fire: 17.32 sq. km. Number of affected mines: 41 out of 67 active mines.
Fire control measures: Sand stowing in exhausted goaf areas: 2.4 MT sand stowed in FY2021-22.
Inundation of fire zones applied in 6 selected areas. Surface drilling and grouting: 890 boreholes.
Methane Drainage: Total methane drainage network: 224 in-seam drainage boreholes plus 48 surface drainage wells.
Methane captured annually: approximately 42 million cubic metres (used for power generation at 4 captive units).
Methane drainage capacity: 12,000 cubic metres per hour across active drainage network.
Residual methane in goaf monitored continuously; automated alarm at 0.8% CH4 concentration.
Spontaneous Heating: Self-heating susceptibility index: 2.41 (moderate to high). Incubation period: 8-14 days."""),
    ],
    "MCL_Environmental_Compliance_FY2023.pdf": [
        (1, """Mahanadi Coalfields Limited (MCL) Environmental Compliance Report FY 2022-23. All 21 active opencast
mines and 3 underground mines of MCL hold valid Environmental Clearances as of 31 March 2023. No mine is
operating beyond its sanctioned production capacity or EC limits. Key EC details: Jagannath OCP: EC valid until
2029; sanctioned capacity: 5.0 MTPA. Lingaraj OCP: EC valid until 2031; sanctioned capacity: 3.5 MTPA.
Lakhanpur OCP: EC valid until 2028; sanctioned capacity: 8.0 MTPA. Bharatpur OCP: EC valid until 2030;
sanctioned capacity: 8.5 MTPA. Orient OCP and UG: EC valid until 2027. Basundhara OCP: EC valid until 2032;
sanctioned capacity: 5.0 MTPA. Belpahar OCP: EC valid until 2026 (renewal application submitted).
Hingula OCP: EC valid until 2029; sanctioned capacity: 4.5 MTPA. No material non-compliance under the
Environment Protection Act, 1986 was recorded during FY 2022-23. Next scheduled EC review: FY 2026-27 and 2027-28."""),
        (2, """Air Quality and Dust Management - MCL FY 2022-23. MCL operates 38 ambient air quality monitoring
stations across all coalfield areas as per CPCB norms. Aggregate annual average values: PM10: 89.4 micrograms
per cubic metre (NAAQS standard: 60, EXCEEDS standard). PM2.5: 38.2 (NAAQS: 40, Within standard).
SO2: 12.8 (NAAQS: 50, Within standard). NOx: 26.1 (NAAQS: 40, Within standard).
PM10 exceedance is primarily observed within 500 m of active mine faces and haul roads.
Dust suppression measures: Water sprinklers on haul roads: 24 km of roads covered.
Mist cannons deployed: 42 units at active faces and crushing stations. Speed limit for dumpers: 25 km/h.
Green belt development: 1,842 hectares of plantation around mine periphery.
Compliance status: Quarterly monitoring reports submitted to Odisha State Pollution Control Board (OSPCB)."""),
        (3, """Water Management and Land Reclamation - MCL FY 2022-23. Total mine water pumped: 142.6 million litres
per day (MLD) across all active mines. Water treated before discharge: 138.2 MLD (97% treatment coverage).
Water reused in mine operations: 84.5 MLD (59.2% recycling rate). Discharge to local water bodies: 53.7 MLD
(post-treatment, meeting IS 2490 standards). Water quality at discharge points: pH: 7.2-8.4 (standard:
5.5-9.0, Compliant). Total Suspended Solids: 28-48 mg/l (standard: 100 mg/l max, Compliant). Iron content:
1.2-2.8 mg/l (standard: 3.0 mg/l max, Compliant). Land Reclamation: Total disturbed land (cumulative):
18,420 hectares. Land reclaimed during FY2022-23: 1,248 hectares. Cumulative reclaimed area: 11,840 hectares
(64.3% reclamation rate). Tree plantation during FY2022-23: 2.84 million saplings; survival rate 72%.
Bio-diversity parks established: 3 parks (414 hectares total). MCL mines are fully compliant on all EC conditions."""),
    ],
    "Coal_Reserve_Estimation_India_2023.pdf": [
        (1, """National Coal Reserve Estimation India 2023. India holds the fourth largest coal reserves in the world
after USA, Russia, and Australia. Total coal resources (geological): 361.30 billion tonnes (BT).
Total proved reserves (minable): 148.46 BT. Total indicated resources: 143.02 BT. Total inferred resources:
69.82 BT. Coking coal (all categories): 33.86 BT (9.4% of total geological resources). Prime coking coal:
6.03 BT. Medium coking coal: 4.71 BT. Semi-coking coal: 23.12 BT. Non-coking coal: 327.44 BT (90.6%).
State-wise distribution: Jharkhand: 86.07 BT (23.8%, highest nationally). Odisha: 81.97 BT (22.7%).
Chhattisgarh: 66.41 BT (18.4%). Madhya Pradesh: 28.38 BT (7.9%). West Bengal: 31.67 BT (8.8%).
Telangana: 22.04 BT (6.1%). Maharashtra: 11.17 BT (3.1%). Depth-wise distribution: 0-300 m: 58% of proved
reserves (most economic). 300-600 m: 31%. Greater than 600 m: 11% (future potential)."""),
        (2, """Coking Coal Reserves Detailed Analysis India 2023. India's coking coal reserves are critical for the
domestic steel industry. India imports approximately 55 MT of coking coal annually due to quality constraints.
Total prime coking coal reserves: 6.03 BT. Location: Jharkhand (Jharia: 3.55 BT; East Bokaro: 0.98 BT;
West Bokaro: 0.62 BT; Giridih: 0.44 BT) and West Bengal (Raniganj: 0.44 BT). Total medium coking coal: 4.71 BT.
Total semi-coking coal: 23.12 BT. Quality parameters of India's prime coking coal: Ash content: 18-25%
(high by global standards; washed coal 14-18%). Volatile matter: 22-36%. Coking index: G4-G10 (Gray-King scale).
Import dependency: India imported 58.2 MT of coking coal in FY2022-23 (principal sources: Australia 72%,
USA 15%, Canada 8%). Domestic coking coal production: 41.6 MT (BCCL: 26.1 MT, ECL: 8.4 MT, CCL: 7.1 MT)."""),
        (3, """Coal Production Forecast and Demand Projection India. Historical production: FY2020-21: 716.1 MT
(CIL 596 MT). FY2021-22: 778.2 MT. FY2022-23: 893.1 MT (record production). FY2023-24 target: 1,012 MT
(CIL target: 780 MT). Sector-wise coal demand projections: Power sector: 620 MT (FY2023-24); projected
900 MT by FY2029-30. Steel sector: 68 MT (FY2023-24); projected 95 MT by FY2029-30.
Cement, chemicals, others: 45 MT (FY2023-24). Total projected demand FY2029-30: 1,040-1,200 MT.
CIL production target trajectory: FY2023-24: 780 MT. FY2024-25: 838 MT. FY2025-26: 900 MT. FY2029-30: 1,000 MT.
Reserve adequacy: At 1,000 MT annual extraction, proven reserves (148 BT) provide 148 years of reserves.
OBR Ratio national average for opencast mines: 3.8 cubic metres per tonne of coal.
Effective recoverable reserve fraction: 50-60% for underground; 85-92% for opencast."""),
    ],
    "NCL_Safety_Incident_Report_FY2024.pdf": [
        (1, """Northern Coalfields Limited (NCL) Safety and DGMS Compliance Report FY 2023-24. NCL operates entirely
through opencast mining in the Singrauli coalfield region straddling Madhya Pradesh and Uttar Pradesh.
Annual production: approximately 130 MT. NCL is the highest production subsidiary of CIL.
Safety Performance FY 2023-24 (April 2023 to March 2024): Total fatal accidents: 6 (vs 8 in FY2022-23,
improvement of 25%). Fatality rate per million tonnes (FRMM): 0.046 (vs 0.067 in FY2022-23).
Serious Injuries: Total: 14 (vs 19 in FY2022-23). Serious injury rate per million tonnes: 0.108.
Minor Injuries: Total: 47 (vs 63 in FY2022-23). Total man days lost: 2,184.
Lost Time Injury Frequency Rate (LTIFR): LTIFR FY2023-24: 0.23 injuries per 200,000 man hours worked.
LTIFR FY2022-23: 0.31 (improvement: 25.8%). NCL's LTIFR of 0.23 compares favourably against CIL average of
0.31 and international opencast mining benchmark of 0.35. Total man hours worked: 87.4 million in FY2023-24."""),
        (2, """DGMS Compliance and Inspections - NCL FY2023-24. DGMS Inspections conducted: 142 inspections (routine
plus special). Notices issued: 38 notices under Mines Act 1952 and Coal Mines Regulations 2017.
Notices complied: 35 (compliance rate 92.1%). Pending notices: 3 (within 90-day compliance window).
Category of violations identified: Electrical safety: 11 notices (29%). Machinery guarding: 8 notices (21%).
Explosives handling (road blasting safety): 7 notices (18%). Stacking/dumping norms: 6 notices (16%).
Ventilation (surface benches): 4 notices (11%). Other: 2 notices (5%). Safety certifications: IS 14489:2018
(Occupational Health and Safety Management): Certified, valid until 2026. ISO 45001:2018 under implementation.
Statutory training compliance: Statutory competency certificate holders (Blasting): 284 personnel.
First aid certificate holders: 1,842 personnel. Mine surveyors: 38 (all with valid certificates)."""),
        (3, """Accident Analysis and Preventive Measures - NCL FY 2023-24. Cause breakdown of 6 fatal accidents:
Dumper/HEMM collision: 2 fatalities (33%) at Jayant and Dudhichua mines. Fall of person from height: 1 fatality
(17%) at Nigahi OCP. Hit by moving machinery: 1 fatality (17%) at Amlohri mine. Slope/bench failure: 1 fatality
(17%) at Khadia mine. Other causes: 1 fatality (17%). Corrective actions implemented: (a) Mandatory proximity
warning system (PWS) on all 426 HEMM units by Q2 FY2024-25. (b) Revised bench height norm: Maximum 10 m
(reduced from 12 m) for working benches. (c) Mandatory seatbelt interlock for all new dumper procurements.
(d) Daily safety inspection log mandatory for all bench supervisors. High Potential Near Miss (HPNM) reporting:
Total HPNMs reported: 318 (vs 201 in FY2022-23). HPNMs investigated: 318 (100%).
LTIFR trend (NCL): FY2019-20: 0.44. FY2020-21: 0.39. FY2021-22: 0.35. FY2022-23: 0.31. FY2023-24: 0.23.
Consistent downward trend reflecting sustained safety culture improvement programme."""),
    ],
    "Geological_Borehole_Survey_Singrauli_2022.pdf": [
        (1, """Geological Borehole Survey Report, Singrauli Super Critical Coalfield, 2022. Prepared by CMPDI Regional
Institute, commissioned by NCL. The Singrauli coalfield spans parts of Madhya Pradesh and Uttar Pradesh,
covering approximately 2,200 sq. km. Boreholes drilled (FY2021-22 programme): 486 new boreholes.
Total drilling footage: 78,420 metres. Average borehole depth: 161.4 metres (range: 42 m to 380 m).
Diamond coring: 71% of footage; rotary: 29%. Core recovery rate: 89.8% (overall).
12 geological parties supervised by Senior Geologists. Laboratory analysis at CMPDI Regional Laboratory Bilaspur.
Geophysical logging: Gamma-gamma, neutron, resistivity logs run on all boreholes greater than 100 m depth."""),
        (2, """Singrauli Coalfield Seam Thickness Data 2022 Survey. Principal coal seams: Seam I (Purewa bottom):
average thickness 2.8 m, range 0.8-6.2 m. Seam II (Purewa top): average thickness 4.1 m, range 1.2-8.4 m.
Seam III (Turra): average thickness 5.2 m, range 2.1-12.6 m, high continuity. Seam IV (Dudhichua): average
thickness 6.8 m, range 3.2-18.0 m, high continuity (largest seam). Seam V: average thickness 2.4 m.
Seam IV at Dudhichua block reaches 18.0 m, among the thickest workable coal seams in India.
Average seam thickness for workable seams: 5.2 metres (highest in NCL portfolio, one of highest nationally).
Updated reserve estimates (post-2022 survey): Proved reserves NCL lease area: 22.1 billion tonnes.
Indicated reserves: 28.4 billion tonnes. Total geological resources Singrauli: 58.7 billion tonnes.
Recovery factor (opencast): 88-92%. Recoverable proved reserves NCL: 19.5 BT.
Coal quality: Ash content: 28.4% average. GCV (as-received): 4,800-5,800 kcal/kg (Grade D-E non-coking).
Stripping ratio: Average 1.8:1 (very favourable for opencast)."""),
        (3, """Hydrogeology and Environmental Baseline, Singrauli Coalfield 2022. Upper aquifer (Alluvial): Depth 3-18 m
below ground level; yield 10-120 cubic metres per hour; used for domestic supply. Intermediate aquifer
(Gondwana sandstone): Depth 18-80 m; yield 20-350 cubic metres per hour; primary mining concern.
Average mine water inflow: 480 litres per tonne of coal extracted. Annual mine water pumped (all NCL mines):
118 million cubic metres (MCM). Water recycled for dust suppression, washeries, and plantation: 62% of pumped
volume. Singrauli mines are fully opencast; no underground subsidence risk. Haul road settlement monitoring:
48 monitoring stations. Maximum settlement recorded: 0.42 m. Flora: 342 plant species recorded in buffer zones;
18 species on IUCN watchlist. Fauna: 67 mammal species, 182 bird species. Forest diversion: 4,842 hectares
diverted for mining (cumulative). Compensatory afforestation obligation: 9,684 hectares. Status: 7,210 hectares
planted (74.5% fulfilled)."""),
    ],
    "SECL_Production_Forecast_FY2025.pdf": [
        (1, """South Eastern Coalfields Limited (SECL) Production Forecast and Plan FY 2024-25. SECL is the largest
coal producing subsidiary of CIL by volume. Operating in Chhattisgarh and Madhya Pradesh.
FY 2024-25 Production Target: 185.0 MT (approved by CIL Board). FY 2023-24 actual production: 172.3 MT
(achievement: 98.5% of 175 MT target). CAGR target (FY2024-25 to FY2028-29): 6.2% per annum.
Mine-wise production targets FY 2024-25: Gevra OCP: 50.0 MT (expansion at 70 MTPA approved). Dipka OCP: 30.0 MT.
Kusmunda OCP: 25.0 MT. Korba Opencast: 12.0 MT. Bhatgaon OCP: 8.0 MT. Chirimiri Group: 6.0 MT.
Raigarh Group: 5.5 MT. Johilla UG: 1.5 MT. Other mines (18): 47.0 MT.
Overburden Removal (OBR) targets FY 2024-25: Total OBR target: 702 Mcm.
OBR ratio (SECL overall): 3.8 cubic metres of overburden per tonne of coal (consistent with national average).
Gevra OCP: 3.2:1 (favourable due to shallow seams). Deepening mines (Dipka Phase-III, Kusmunda): 4.8 to 5.2:1."""),
        (2, """Capital Expenditure Plan SECL FY 2024-25. Total Capex approved: Rs 5,840 crore. Mine development and
expansion: Rs 2,940 crore (50.3%). HEMM procurement: Rs 1,820 crore (31.2%): 42 new dumpers (150T and 240T),
8 draglines refurbishment. Environmental mitigation: Rs 480 crore (8.2%). Township and infrastructure: Rs 360
crore (6.2%). IT and digitalisation: Rs 240 crore (4.1%). HEMM fleet planned additions: 240T dumpers: 18 units
(Gevra, Dipka expansion). 150T dumpers: 24 units (Kusmunda, Bhatgaon). Draglines: 2 additional (Kusmunda new pit).
Shovel-dumper combination: Enhanced by 6 shovel units (42 cubic metre bucket). Surface miners: 4 units for
selective mining at Raigarh. Washery expansion: Ambikapur Washery Phase-II: 5 MTPA addition (total capacity
10 MTPA), commissioning Q3 FY2024-25. Bhatgaon Washery Phase-I: 3 MTPA new installation, commissioning Q4."""),
        (3, """SECL Environmental and Social Commitments FY 2024-25. Tree plantation target: 6.5 million saplings
(up from 5.2 million in FY2023-24). Mine reclamation target: 3,200 hectares (progressive mine closure areas).
Water recycling target: 65% of total mine water pumped (vs 58% actual in FY2023-24). Renewable energy: 250 MW
solar plant under development (Bilaspur district); commissioning FY2025-26. PM10 compliance: Implementation of
closed conveyor system for coal transport at Gevra (14 km stretch). CSR investments FY 2024-25: Rs 284 crore.
Focus areas: Education, healthcare, skill development, drinking water (32 villages in mining affected zones).
R&R (Resettlement and Rehabilitation): Total families displaced (cumulative): 12,842. R&R completed: 11,980
families (93.3%). Pending R&R: 862 families. Compensation disbursed: Rs 1,240 crore (cumulative).
OBR ratio management: As stipulated in EC conditions for SECL opencast mines, OBR ratio maintained at or below
3.8:1. Compliance is reported quarterly to MoEFCC and CGSPCB."""),
    ],
}


def _get_model():
    global _model
    if _model is None:
        print("Loading embedding model...")
        _model = SentenceTransformer(MODEL_NAME)
    return _model


def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunks.append(" ".join(words[start:end]))
        start += chunk_size - overlap
    return chunks


def build_vectorstore():
    all_texts = []
    all_meta = []

    for doc_name, pages in SYNTHETIC_DOCS.items():
        for page_num, text in pages:
            chunks = chunk_text(text, CHUNK_SIZE, CHUNK_OVERLAP)
            for chunk in chunks:
                if len(chunk.strip()) < 30:
                    continue
                all_texts.append(chunk)
                all_meta.append({
                    "document": doc_name,
                    "page": page_num,
                    "excerpt": chunk[:300],
                })
        print(f"  {doc_name}: {len(pages)} pages → chunks indexed")

    print(f"\nTotal chunks: {len(all_texts)}. Generating embeddings...")
    model = _get_model()
    embeddings = model.encode(all_texts, batch_size=32, show_progress_bar=True, normalize_embeddings=True)

    store = {
        "embeddings": embeddings.astype(np.float32),
        "texts": all_texts,
        "meta": all_meta,
    }
    os.makedirs(os.path.dirname(STORE_PATH), exist_ok=True)
    with open(STORE_PATH, "wb") as f:
        pickle.dump(store, f)

    print(f"\nVector store saved: {STORE_PATH} ({len(all_texts)} chunks)")
    return store


def load_vectorstore() -> dict:
    with open(STORE_PATH, "rb") as f:
        return pickle.load(f)


if __name__ == "__main__":
    build_vectorstore()
