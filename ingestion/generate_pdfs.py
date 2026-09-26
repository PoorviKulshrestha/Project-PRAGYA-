"""Generate synthetic mining/coal industry PDFs for demo."""
from fpdf import FPDF
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_docs')

DOCS = {
    "CMPDI_Annual_Geological_Survey_Report_2023.pdf": {
        "title": "CMPDI Annual Geological Survey Report 2023",
        "pages": [
            ("Executive Summary", """
This Annual Geological Survey Report has been prepared by the Central Mine Planning and Design Institute (CMPDI),
the apex technical consultancy body of Coal India Limited (CIL). The report consolidates geological data collected
across all seven CIL subsidiaries during the financial year 2022-23.

India's total coal reserves stand at 361.30 billion tonnes as of April 2023, as per the Geological Survey of
India (GSI) assessment. Of this, proven reserves account for 148.46 billion tonnes. The Eastern Coalfields
region, comprising Jharia, Raniganj, and adjoining blocks under ECL and BCCL jurisdiction, holds proven reserves
of 18.7 billion tonnes, representing approximately 12.6% of the national proven reserve base.

The survey covered 4,218 boreholes across 62 coalfield blocks. Total core recovery averaged 91.4%, indicating
high data reliability. The average coal seam thickness across the surveyed coalfields is 4.1 metres, with maximum
seam thickness reaching 24 metres in select Barakar formation blocks in Jharia.

Coal rank distribution shows that coking coal constitutes 18.4% of total reserves, with prime coking coal
estimated at 3.55 billion tonnes concentrated primarily in the Jharia coalfield under BCCL. Non-coking coal
forms the remaining 81.6%, primarily used for thermal power generation.
"""),
            ("Reserve Estimates by Region", """
Eastern Coalfields Region (ECL + BCCL):
Total proven reserves: 18.7 billion tonnes
Measured resources: 31.2 billion tonnes
Coking coal component: 3.55 billion tonnes (prime coking), 5.1 billion tonnes (medium coking)
Principal coalfields: Jharia (BCCL), Raniganj (ECL), East Bokaro (CCL)

Central Coalfields Region (CCL):
Total proven reserves: 22.4 billion tonnes
Principal coalfields: North Karanpura, South Karanpura, Ramgarh, Bokaro

Northern Coalfields Region (NCL):
Total proven reserves: 19.8 billion tonnes
Principal coalfield: Singrauli Super Thermal Power region
Average seam thickness: 5.2 metres (among highest nationally)
Opencast reserves: approximately 78% of total recoverable reserves

Mahanadi Coalfields Region (MCL):
Total proven reserves: 21.5 billion tonnes
Principal coalfields: Talcher, Ib Valley
Coal grade: predominantly Grade C-D non-coking coal

South Eastern Coalfields Region (SECL):
Total proven reserves: 23.6 billion tonnes
Principal coalfields: Korba, Chirimiri, Bisrampur

Western Coalfields Region (WCL):
Total proven reserves: 11.2 billion tonnes
Principal coalfield: Wardha Valley, Kamptee, Yeotmal

National total proven coal reserves: 148.46 billion tonnes (GSI, April 2023)
India's total coal resources: 361.30 billion tonnes
"""),
            ("Seam Characteristics and Stratigraphy", """
Jharia Coalfield - Seam Analysis:
The Jharia coalfield in Dhanbad district, Jharkhand, is the most important coking coal deposit in India.
Seam thickness in the Jharia block averages 3.4 metres, with individual seams ranging from 0.8 m to 24.0 m.
The thickest seam is the XVIII seam in the Kusunda area, measuring 24 metres. Ash content averages 24.3%,
with coking coals showing lower ash (18-21%) suitable for metallurgical use.

Stratigraphy: The Jharia coalfield belongs to the Lower Gondwana (Barakar and Barren Measures) formation.
Dip of seams: 4° to 15° towards south and south-east in the northern part.
Strike: Generally E-W to NW-SE orientation.
Depth range: Surface to 600 m, with most active mining between 80 m and 350 m.

Methane content and drainage:
The Jharia coalfield contains significant methane (firedamp) deposits. Average methane gas content is
4.8 m³/tonne in shallow seams, rising to 8.2 m³/tonne in seams below 200 m. Methane drainage capacity
across active BCCL mines is approximately 12,000 m³/hour through in-seam boreholes and surface drainage wells.
Methane drainage reduces outburst risk and, when captured, provides a supplementary energy source.

Singrauli Coalfield - Seam Analysis:
Average seam thickness: 5.2 metres. Maximum: 18.0 metres (Dudhichua block).
Coal type: Non-coking, Grade B-C. Ash content: 28-36%.
Hydrogeology: Moderate aquifer interaction above 150 m depth. Water table at 12-18 m below ground.
"""),
            ("Borehole Survey Results and Data Quality", """
Borehole Programme 2022-23:
Total boreholes drilled: 4,218 (new) + 1,104 (relogged historical)
Total drilling footage: 684,290 metres
Core recovery rate: 91.4% (national average); 93.1% in Jharia; 89.8% in Talcher
Diamond core drilling: 72% of total footage
Rotary drilling: 28% of total footage

Data quality metrics:
Logging standards: As per CMPDI Technical Circular 2019 and BIS IS:9143
Chemical analysis: Proximate analysis (moisture, ash, volatile matter, fixed carbon) for all samples
Calorific value analysis: Gross Calorific Value (GCV) on 100% of coal cores
Petrographic analysis: Vitrinite reflectance measurements for rank determination in selected boreholes

Errors and discrepancies:
Collar location error: Mean 0.12 m (GPS precision); maximum 0.8 m in hilly terrain
Depth measurement error: Mean 0.04% of depth; corrected using magnetic deviation logs
Data entry errors: Identified and corrected in 1.2% of records through QC audit

Historical data reconciliation:
Pre-digital records (pre-1980): Scanned and digitised for 2,890 boreholes. Handwritten logs converted
to structured database entries. Depth discrepancies of 2-8% identified and flagged for expert review.
"""),
        ]
    },
    "ECL_Production_Report_Q3_FY2024.pdf": {
        "title": "Eastern Coalfields Limited - Production Report Q3 FY 2023-24",
        "pages": [
            ("Executive Summary - Q3 Performance", """
Eastern Coalfields Limited (ECL) Production Report for Q3 FY 2023-24 (October-December 2023).

Headline Results:
Coal Production: 7.84 million tonnes (MT) against a target of 7.50 MT - exceeding target by 4.5%.
Coal Dispatch: 142.6 MT cumulative (April-December 2023) against annual target of 138 MT.
Overburden Removal: 42.1 million cubic metres (Mcm) against target of 40.0 Mcm.
Stripping Ratio: 3.8 cubic metres of overburden per tonne of coal (OBR ratio).

The quarter witnessed a 7.2% year-on-year (YoY) increase in production, driven by improved longwall
deployment at Sonepur Bazari and Rajmahal mines, and enhanced dragline utilisation in opencast sections.

Comparison with Q3 FY2022-23:
Q3 FY2022-23 production: 7.31 MT. Q3 FY2023-24 production: 7.84 MT. Growth: +7.27%.
Annual target FY2023-24: 31.5 MT. H1+Q3 cumulative: 23.9 MT. On track for annual target.

Dispatch and off-take:
Total coal dispatched in Q3: 8.22 MT. Principal consignees: NTPC (3.1 MT), DVC (1.8 MT), State utilities (2.4 MT).
Pit-head stock as on 31 December 2023: 2.14 MT (within norms).
"""),
            ("Mine-wise Production Details", """
Rajmahal Open Cast Project (OCP):
Q3 FY2024 production: 2.14 MT (target: 2.00 MT). Achievement: 107%.
OBR ratio: 3.2:1. Coal grade: Grade D (non-coking). Seam thickness: 4.1 m average.
Longwall panels operational: 0 (fully opencast). Draglines deployed: 3 units (24/7 operation).

Sonepur Bazari (SBOC):
Q3 FY2024 production: 1.82 MT (target: 1.75 MT). Achievement: 104%.
OBR ratio: 4.1:1. Coal grade: Grade B-C. Methane detection: within safe limits (<1% CH4).
Mechanical loading: 94% of total production.

Jhanjra Underground Mine:
Q3 FY2024 production: 0.42 MT (target: 0.38 MT). Achievement: 110%.
Longwall panel: 2 active faces at 7 East Seam (seam height 2.1 m).
Average face advance: 4.2 m/day. Immediate roof: argillaceous shale.
Output per manshift (OMS): 1.84 tonnes - highest in ECL underground portfolio.

Chinakuri Colliery (Combined):
Q3 FY2024 production: 0.31 MT (target: 0.30 MT).
Gas drainage active: Yes. Firedamp drainage rate: 240 m³/hour from borehole network.

Other ECL mines (aggregated, 12 mines):
Combined Q3 production: 3.15 MT against 3.07 MT target.
"""),
            ("Financial Performance and Grade-wise Output", """
Revenue from coal sales in Q3 FY2024: ₹2,847 crore (provisional).
Average realisation per tonne: ₹2,143/MT (blended across all grades).
Cost of production: ₹1,478/MT. Operating margin: ₹665/MT (31.0%).

Grade-wise production breakdown Q3 FY2024:
Grade A (GCV > 6700 kcal/kg): 0.04 MT - 0.5%
Grade B (GCV 6401-6700): 0.12 MT - 1.5%
Grade C (GCV 6101-6400): 0.68 MT - 8.7%
Grade D (GCV 5801-6100): 2.14 MT - 27.3%
Grade E (GCV 5301-5800): 2.89 MT - 36.9%
Grade F (GCV 4801-5300): 1.57 MT - 20.0%
Grade G (GCV ≤ 4800): 0.40 MT - 5.1%

Quality improvement initiatives:
Selective mining at Rajmahal to improve average GCV by 150 kcal/kg.
Coal beneficiation at Mugma Washery: throughput 0.68 MT in Q3.
Reject utilisation: 0.09 MT sold to local consumers under CIL policy.
"""),
        ]
    },
    "Jharia_Coalfield_Resource_Assessment_2022.pdf": {
        "title": "Jharia Coalfield - Comprehensive Resource Assessment 2022",
        "pages": [
            ("Introduction and Scope", """
This Comprehensive Resource Assessment of the Jharia Coalfield has been prepared by CMPDI on behalf of
Bharat Coking Coal Limited (BCCL), covering data up to March 2022. The Jharia coalfield, located in Dhanbad
district, Jharkhand, is the single most important coking coal deposit in India and one of the largest known
metallurgical coal deposits in Asia.

Geographic extent: 456 sq. km, spanning the Damodar Valley.
Administrative jurisdiction: Bharat Coking Coal Limited (BCCL), a CIL subsidiary.
Historical mining: Active extraction for over 100 years (since 1894).
Current active mines: 67 mines (32 underground, 35 opencast); 29 mines under closure process.

Geological Formation:
The Jharia coalfield belongs to the Gondwana Supergroup (Permian age, ~260 million years old).
Principal coal-bearing formation: Lower Gondwana - Barakar Formation.
Secondary coal-bearing horizon: Barren Measures Formation.
Total coal measures thickness: 600-1000 metres.
"""),
            ("Reserve and Resource Estimates", """
Coal Reserve Classification (as per UNFC 2009 and GSI classification):

Proved Reserves:
Total proved reserves (minable): 3.55 billion tonnes (prime coking coal)
Including medium coking and semi-coking: 5.2 billion tonnes total proved
Depth range for proved reserves: surface to 600 m
Area covered by proved reserves: 312 sq. km

Indicated Resources:
Total indicated resources: 4.1 billion tonnes (all categories)
Depth range: 300 m to 1,200 m
Data density: borehole spacing 200-400 m

Inferred Resources:
Total inferred resources: 2.3 billion tonnes (extrapolated)

National Significance:
Prime coking coal reserves in Jharia: 3.55 billion tonnes = 19.0% of India's total prime coking coal
This is the single largest concentration of prime coking coal in India and critical for the domestic steel industry.

Seam inventory:
Total number of coal seams identified: 23 seams (I through XXII plus localised seams)
Workable seams (thickness > 1.2 m): 16 seams
Thickest seam: Seam XVIII (Kusunda block) - 24.0 metres
Most extensive seam: Seam IX - traceable across 180 sq. km
Average workable seam thickness: 3.4 metres
Aggregate seam thickness (all workable seams): 38.6 metres
"""),
            ("Seam-wise Quality Parameters", """
Coal Quality - Jharia Coalfield Average Parameters:

Prime Coking Coal seams (I-IV, parts of IX):
Moisture (air-dried): 1.2-1.8%
Ash content (air-dried): 18.0-22.0% (average 19.5%)
Volatile matter: 26-34% (high volatile coking range)
Gross Calorific Value: 7,800-8,200 kcal/kg (air-dried)
Coking index (Gray-King): G5 to G9
Vitrinite reflectance (Ro max): 1.10-1.45% (medium volatile bituminous)

Non-coking and semi-coking seams (V-XIV, parts):
Ash content (air-dried): 22.0-32.0% (average 24.3% across all seams)
Volatile matter: 30-40%
GCV: 5,800-7,400 kcal/kg

Quality degradation trends:
Ash content has increased by 2.1 percentage points over the past decade due to dilution from
intermixed shale bands and reduced selectivity in mechanised mining. Beneficiation at washeries
(BCCL operates 8 washeries with combined capacity 17.6 MTY) is essential for export-grade product.

Sulphur content: Generally < 1.0% (average 0.54%) - favourable for coking use.
Phosphorus content: 0.01-0.04% - within steel industry specifications.
"""),
            ("Underground Fire and Safety", """
Underground Fire Management - Jharia Coalfield:
The Jharia coalfield has been plagued by underground coal fires, some burning for over 100 years.
Total number of active fire areas: 70 (as of December 2021)
Area under active fire: 17.32 sq. km
Number of affected mines: 41 out of 67 active mines

Fire control measures implemented:
1. Sand stowing in exhausted goaf areas: 2.4 MT sand stowed in FY2021-22
2. Inundation of fire zones: Applied in 6 selected areas
3. Surface drilling and grouting: 890 boreholes for fire delineation and sealing
4. Relocation of surface communities: BCCL-CMPDIL Master Plan for relocation of affected persons

Methane Drainage:
Total methane drainage network: 224 in-seam drainage boreholes + 48 surface drainage wells
Methane captured annually: ~42 million m³ (used for power generation at 4 captive units)
Methane drainage capacity: 12,000 m³/hour across active drainage network
Residual methane in goaf: Monitored continuously; automated alarm at 0.8% CH4 concentration

Spontaneous Heating:
Self-heating susceptibility index (SHI): 2.41 cm³/g/min (moderate to high)
Incubation period estimated: 8-14 days for fresh goaf in deep seams
Preventive measures: nitrogen injection, quick stowing, monitoring with CO sensors
"""),
        ]
    },
    "MCL_Environmental_Compliance_FY2023.pdf": {
        "title": "Mahanadi Coalfields Limited - Environmental Compliance Report FY 2022-23",
        "pages": [
            ("Environmental Clearances Status", """
Mahanadi Coalfields Limited (MCL) Environmental Compliance Report for FY 2022-23.

Environmental Clearance (EC) Status - All Active MCL Mines:
All 21 active opencast mines and 3 underground mines of MCL hold valid Environmental Clearances
as of 31 March 2023. No mine is operating beyond its sanctioned production capacity or EC limits.

Key EC details:
Talcher Coalfields (Odisha):
  - Jagannath OCP: EC valid until 2029 (Grant date: 2017). Sanctioned capacity: 5.0 MTPA.
  - Lingaraj OCP: EC valid until 2031 (Grant date: 2019). Sanctioned capacity: 3.5 MTPA.
  - Lakhanpur OCP: EC valid until 2028. Sanctioned capacity: 8.0 MTPA.
  - Bharatpur OCP: EC valid until 2030. Sanctioned capacity: 8.5 MTPA.
  - Orient OCP and UG: EC valid until 2027. Sanctioned capacity: 1.2 MTPA (OC) + 0.5 MTPA (UG).

Ib Valley Coalfields (Odisha):
  - Basundhara OCP: EC valid until 2032. Sanctioned capacity: 5.0 MTPA.
  - Belpahar OCP: EC valid until 2026 (renewal application submitted). Sanctioned: 2.5 MTPA.
  - Hingula OCP: EC valid until 2029. Sanctioned capacity: 4.5 MTPA.

No material non-compliance under the Environment Protection Act, 1986 was recorded during FY 2022-23.
The next scheduled EC review for the majority of mines is FY 2026-27 and FY 2027-28.
"""),
            ("Air Quality and Dust Management", """
Ambient Air Quality Monitoring - FY 2022-23:

MCL operates 38 ambient air quality monitoring stations across all coalfield areas as per CPCB norms.
Parameters monitored: PM10, PM2.5, SO2, NOx, CO.

Aggregate annual average values (MCL coalfields):
PM10: 89.4 µg/m³ (National Ambient Air Quality Standard: 60 µg/m³ - EXCEEDS standard)
PM2.5: 38.2 µg/m³ (NAAQS: 40 µg/m³ - Within standard)
SO2: 12.8 µg/m³ (NAAQS: 50 µg/m³ - Within standard)
NOx: 26.1 µg/m³ (NAAQS: 40 µg/m³ - Within standard)

PM10 exceedance analysis:
The PM10 exceedance is primarily observed within 500 m of active mine faces and haul roads.
Dust suppression measures active:
- Water sprinklers on haul roads: 24 km of roads covered
- Mist cannons deployed: 42 units at active faces and crushing stations
- Speed limit for dumpers on haul roads: 25 km/h (enforced with speed breakers)
- Green belt development: 1,842 hectares of plantation around mine periphery

Compliance status: Under MoEFCC Consent to Operate conditions, quarterly monitoring reports
submitted to Odisha State Pollution Control Board (OSPCB). All submissions current.
"""),
            ("Water Management and Land Reclamation", """
Water Management - MCL FY 2022-23:

Mine water discharge:
Total mine water pumped: 142.6 million litres/day (MLD) across all active mines
Water treated before discharge: 138.2 MLD (97% treatment coverage)
Water reused in mine operations: 84.5 MLD (59.2% recycling rate)
Discharge to local water bodies: 53.7 MLD (post-treatment, meeting IS 2490 standards)

Water quality parameters at discharge points:
pH: 7.2-8.4 (standard: 5.5-9.0 - Compliant)
Total Suspended Solids (TSS): 28-48 mg/l (standard: ≤ 100 mg/l - Compliant)
Iron content: 1.2-2.8 mg/l (standard: ≤ 3.0 mg/l - Compliant)

Land Reclamation:
Total disturbed land (cumulative): 18,420 hectares
Land reclaimed during FY2022-23: 1,248 hectares
Cumulative reclaimed area: 11,840 hectares (64.3% reclamation rate)
Tree plantation during FY2022-23: 2.84 million saplings; survival rate 72%.
Bio-diversity parks established: 3 parks (414 hectares total)

Progressive mine closure:
Mines under approved progressive closure: 4 mines
Expenditure on closure activities: ₹94 crore in FY2022-23
"""),
        ]
    },
    "Coal_Reserve_Estimation_India_2023.pdf": {
        "title": "National Coal Reserve Estimation Report - India 2023",
        "pages": [
            ("National Reserve Summary", """
National Coal Reserve and Resource Estimation - India (as of April 2023)
Prepared by: Geological Survey of India (GSI) in coordination with CMPDI/CIL

India holds the fourth largest coal reserves in the world after USA, Russia, and Australia.
Total coal resources (geological): 361.30 billion tonnes (BT)
Total proved reserves (minable): 148.46 BT
Total indicated resources: 143.02 BT
Total inferred resources: 69.82 BT

Category-wise breakdown:
Coking coal (all categories): 33.86 BT (9.4% of total geological resources)
  - Prime coking coal: 6.03 BT
  - Medium coking coal: 4.71 BT
  - Semi-coking coal: 23.12 BT
Non-coking coal: 327.44 BT (90.6% of total geological resources)
  - Grade A to G (thermal and industrial use): 327.44 BT

State-wise distribution of total coal resources:
Jharkhand: 86.07 BT (23.8%) - highest nationally
Odisha: 81.97 BT (22.7%)
Chhattisgarh: 66.41 BT (18.4%)
Madhya Pradesh: 28.38 BT (7.9%)
West Bengal: 31.67 BT (8.8%)
Telangana: 22.04 BT (6.1%)
Maharashtra: 11.17 BT (3.1%)
Uttar Pradesh: 1.06 BT (0.3%)
Other states: 32.53 BT (9.0%)

Depth-wise distribution of reserves:
0-300 m depth: 58% of proved reserves (most economic for extraction)
300-600 m depth: 31% of proved reserves
>600 m depth: 11% of proved reserves (future potential, technology-dependent)
"""),
            ("Coking Coal Reserves - Detailed Analysis", """
Coking Coal Reserves - India 2023

India's coking coal reserves are critical for the domestic steel industry. The country imports
approximately 55 MT of coking coal annually due to quality constraints of domestic supply.

Total prime coking coal reserves: 6.03 BT
Location: Jharkhand (Jharia: 3.55 BT; East Bokaro: 0.98 BT; West Bokaro: 0.62 BT; Giridih: 0.44 BT)
         West Bengal (Raniganj: 0.44 BT)

Total medium coking coal reserves: 4.71 BT
Location: Jharkhand (South Karanpura, North Karanpura, Bokaro), Odisha (Talcher)

Total semi-coking coal reserves: 23.12 BT
Location: Multiple states; Chhattisgarh and Madhya Pradesh dominant

Quality parameters of India's prime coking coal:
Ash content: 18-25% (high by global standards; washed coal 14-18%)
Volatile matter: 22-36% (suited for blending)
Coking index: G4-G10 (Gray-King scale)
Vitrinite reflectance: 0.9-1.6% Ro (medium to high volatile bituminous)

Import dependency analysis:
India imported 58.2 MT of coking coal in FY2022-23 (principal sources: Australia 72%, USA 15%, Canada 8%)
Domestic coking coal production: 41.6 MT (BCCL: 26.1 MT, ECL: 8.4 MT, CCL: 7.1 MT)
Import substitute potential: Limited due to quality gap; blending with domestic is viable up to 30-35%

Future reserve development:
Jharia Deep Mining: Reserves below 600 m estimated at 1.8 BT; technology evaluation underway
Bokaro North Block: 0.28 BT indicated resource; awaiting clearance
New exploration areas: Talcher deep blocks, Wardha deep, Pranhita-Godavari valley
"""),
            ("Production Forecast and Demand", """
Coal Production Forecast and Demand Projection - India

Historical production:
FY2020-21: 716.1 MT (CIL: 596 MT, SCCL: 64 MT, Captive/others: 56 MT)
FY2021-22: 778.2 MT
FY2022-23: 893.1 MT (record production)
FY2023-24 target: 1,012 MT (CIL target: 780 MT)

Sector-wise coal demand projections (Planning Commission/NITI Aayog):
Power sector: 620 MT (FY2023-24); projected 900 MT by FY2029-30
Steel sector: 68 MT (FY2023-24); projected 95 MT by FY2029-30
Cement, chemicals, others: 45 MT (FY2023-24)
Total projected demand FY2029-30: 1,040-1,200 MT

CIL production target trajectory:
FY2023-24: 780 MT; FY2024-25: 838 MT; FY2025-26: 900 MT; FY2029-30: 1,000 MT

Reserve adequacy at projected production rates:
At 1,000 MT annual extraction, proven reserves (148 BT) provide 148 years of reserves.
Measured + indicated resources (291 BT): ~291 years at 1,000 MTPA.
Note: Reserve to production (R/P) ratios do not account for recoverability factors.
Effective recoverable reserve fraction: 50-60% for underground; 85-92% for opencast.

OBR Ratio national average for opencast mines: 3.8 cubic metres per tonne of coal.
This ratio has been increasing due to deeper workings and increasing overburden thickness.
"""),
        ]
    },
    "NCL_Safety_Incident_Report_FY2024.pdf": {
        "title": "Northern Coalfields Limited - Safety & DGMS Compliance Report FY 2023-24",
        "pages": [
            ("Safety Performance Overview", """
Northern Coalfields Limited (NCL) Safety & DGMS Compliance Report - FY 2023-24

NCL operates entirely through opencast mining in the Singrauli coalfield region straddling
Madhya Pradesh and Uttar Pradesh. With an annual production of approximately 130 MT, NCL is
the highest production subsidiary of CIL.

Safety Performance Summary - FY 2023-24 (April 2023 to March 2024):

Fatalities:
Total fatal accidents: 6 (vs 8 in FY2022-23 - improvement of 25%)
Fatality rate per million tonnes (FRMM): 0.046 (vs 0.067 in FY2022-23)

Serious Injuries:
Total serious injuries: 14 (vs 19 in FY2022-23)
Serious injury rate per million tonnes: 0.108

Minor Injuries:
Total minor injuries: 47 (vs 63 in FY2022-23)
Total man days lost due to accidents: 2,184

Lost Time Injury Frequency Rate (LTIFR):
LTIFR FY2023-24: 0.23 injuries per 200,000 man hours worked
LTIFR FY2022-23: 0.31 (improvement: 25.8%)
NCL's LTIFR of 0.23 compares favourably against the CIL average of 0.31 and international
opencast mining benchmark of 0.35 (ICMM Global Sentinel 2023).

Total man hours worked: 87.4 million man hours in FY2023-24.
"""),
            ("DGMS Compliance and Inspections", """
Directorate General of Mines Safety (DGMS) Compliance - NCL FY2023-24:

DGMS Inspections conducted: 142 inspections (routine + special)
Notices issued: 38 notices under Mines Act 1952 / Coal Mines Regulations 2017
Notices complied: 35 (compliance rate 92.1%)
Pending notices (under rectification): 3 (within 90-day compliance window)
Notices contested / under review: 0

Category of violations identified:
Electrical safety: 11 notices (29%)
Machinery guarding: 8 notices (21%)
Explosives handling (road blasting safety): 7 notices (18%)
Stacking/dumping norms: 6 notices (16%)
Ventilation (surface benches): 4 notices (11%)
Other: 2 notices (5%)

Safety certifications:
IS 14489:2018 (Occupational Health and Safety Management): Certified, valid until 2026
ISO 45001:2018: Under implementation; target certification FY2024-25

Statutory training compliance:
Statutory competency certificate holders (Blasting): 284 personnel (all active blasters certified)
First aid certificate holders: 1,842 personnel
Mine surveyors: 38 (all with valid certificates of competency)
Gas testing personnel: Not applicable (fully opencast operations)
"""),
            ("Accident Analysis and Preventive Measures", """
Accident Root Cause Analysis - FY 2023-24:

Cause category breakdown of 6 fatal accidents:
1. Dumper/HEMM collision: 2 fatalities (33%) - Jayant and Dudhichua mines
2. Fall of person from height: 1 fatality (17%) - Nigahi OCP
3. Hit by moving machinery: 1 fatality (17%) - Amlohri mine
4. Slope/bench failure: 1 fatality (17%) - Khadia mine
5. Other causes: 1 fatality (17%)

Corrective actions implemented post major accidents:
(a) Mandatory proximity warning system (PWS) on all 426 HEMM units by Q2 FY2024-25
(b) Revised bench height norm: Maximum 10 m (reduced from 12 m) for working benches
(c) Mandatory seatbelt interlock for all new dumper procurements
(d) Daily safety inspection log mandatory for all bench supervisors (E&M grade)
(e) Night-shift lighting audit: 6,800 lux minimum at all active faces (upgraded)

High Potential Near Miss (HPNM) reporting:
Total HPNMs reported: 318 (vs 201 in FY2022-23 - increase due to improved reporting culture)
HPNMs investigated: 318 (100%)
Systemic actions from HPNM learning: 12 mine-wide directives issued

LTIFR trend (NCL):
FY2019-20: 0.44 | FY2020-21: 0.39 | FY2021-22: 0.35 | FY2022-23: 0.31 | FY2023-24: 0.23
Consistent downward trend reflecting sustained safety culture improvement programme.
"""),
        ]
    },
    "Geological_Borehole_Survey_Singrauli_2022.pdf": {
        "title": "Geological Borehole Survey - Singrauli Coalfield 2022",
        "pages": [
            ("Survey Scope and Methodology", """
Geological Borehole Survey Report - Singrauli Super Critical Coalfield, 2022
Prepared by: CMPDI, Regional Institute - Nagpur
Commissioned by: NCL, Northern Coalfields Limited

Survey scope:
The Singrauli coalfield (also called Singrauli Super Critical Coalfield) spans parts of
Madhya Pradesh and Uttar Pradesh, covering an area of approximately 2,200 sq. km.
This 2022 borehole survey covered 18 blocks within NCL's Singrauli lease area.

Boreholes drilled (FY2021-22 programme): 486 new boreholes
Total drilling footage: 78,420 metres
Average borehole depth: 161.4 metres (range: 42 m to 380 m)
Diamond coring: 71% of footage; rotary: 29%
Core recovery rate: 89.8% (overall), ranging from 83.4% (alluvial overburden) to 97.2% (coal seams)

Field teams: 12 geological parties; each supervised by a Senior Geologist (Grade E3 or above)
Laboratory analysis: CMPDI Regional Laboratory, Bilaspur; cross-checked at Central Laboratory, Ranchi
Geophysical logging: Gamma-gamma, neutron, resistivity logs run on all boreholes > 100 m depth
"""),
            ("Seam Thickness and Reserve Estimates", """
Singrauli Coalfield - Seam Thickness Data (2022 Survey):

Principal coal seams in Singrauli coalfield:
Seam I (Purewa bottom): average thickness 2.8 m; range 0.8-6.2 m; continuity: moderate
Seam II (Purewa top): average thickness 4.1 m; range 1.2-8.4 m; continuity: high
Seam III (Turra): average thickness 5.2 m; range 2.1-12.6 m; continuity: high
Seam IV (Dudhichua): average thickness 6.8 m; range 3.2-18.0 m; continuity: high (largest seam)
Seam V: average thickness 2.4 m; continuity: moderate; partly worked out in northern blocks

National significance of Seam III (Turra) and Seam IV (Dudhichua):
These two seams account for 68% of total NCL reserve base. Seam IV at Dudhichua block reaches 18.0 m
- among the thickest workable coal seams in India. Average seam thickness for workable seams: 5.2 metres.

Updated reserve estimates (post-2022 survey):
Proved reserves (NCL lease area): 22.1 billion tonnes
Indicated reserves: 28.4 billion tonnes
Total geological resources (Singrauli super critical coalfield): 58.7 billion tonnes
Recovery factor (opencast): 88-92%
Recoverable proved reserves (NCL): 19.5 BT - approximately 150 years at current extraction rates

Coal quality:
Ash content: 28.4% (average across all seams)
GCV (as-received): 4,800-5,800 kcal/kg (Grade D-E non-coking coal)
Stripping ratio: Average 1.8:1 (cubic metres overburden per tonne coal) - very favourable for opencast
"""),
            ("Hydrogeology and Environmental Baseline", """
Hydrogeology - Singrauli Coalfield 2022:

Aquifer characterisation:
Upper aquifer (Alluvial): Depth 3-18 m below ground level; yield 10-120 m³/hour; used for domestic supply
Intermediate aquifer (Gondwana sandstone): Depth 18-80 m; yield 20-350 m³/hour; primary mining concern
Deep aquifer (Basal Gondwana): Depth > 120 m; low permeability; limited connectivity to upper systems

Mine water inflow rates:
Average mine water inflow: 480 litres/tonne of coal extracted
Annual mine water pumped (all NCL mines): 118 million cubic metres (MCM)
Water recycled for dust suppression, washeries, and plantation: 62% of pumped volume

Subsidence monitoring:
Singrauli mines are fully opencast; no underground subsidence risk.
Haul road settlement monitoring: 48 monitoring stations. Maximum settlement recorded: 0.42 m
(Jayant mine southern haul road - attributed to high OBR areas and monsoon infiltration)

Baseline ecological survey:
Flora: 342 plant species recorded in buffer zones; 18 species on IUCN watchlist
Fauna: 67 mammal species, 182 bird species in the landscape corridor
Forest diversion: 4,842 hectares diverted for mining (cumulative); compensatory afforestation
obligation: 9,684 hectares (1:2 ratio). Status: 7,210 hectares planted (74.5% fulfilled)
"""),
        ]
    },
    "SECL_Production_Forecast_FY2025.pdf": {
        "title": "South Eastern Coalfields Ltd - Production Forecast FY 2024-25",
        "pages": [
            ("Production Targets FY 2024-25", """
South Eastern Coalfields Limited (SECL) Production Forecast and Plan - FY 2024-25

SECL is the largest coal producing subsidiary of CIL by volume. Operating in Chhattisgarh and
Madhya Pradesh, SECL targets continued growth through opencast expansion and underground modernisation.

FY 2024-25 Production Target: 185.0 MT (approved by CIL Board)
FY 2023-24 actual production: 172.3 MT (achievement: 98.5% of 175 MT target)
CAGR target (FY2024-25 to FY2028-29): 6.2% per annum

Mine-wise production targets FY 2024-25 (major mines):
Gevra OCP: 50.0 MT (current capacity: 45 MTPA; expansion under Phase-III at 70 MTPA approved)
Dipka OCP: 30.0 MT
Kusmunda OCP: 25.0 MT
Korba Opencast: 12.0 MT
Bhatgaon OCP: 8.0 MT
Chirimiri Group: 6.0 MT
Raigarh Group: 5.5 MT
Johilla UG: 1.5 MT
Other mines (18): 47.0 MT

Overburden Removal (OBR) targets FY 2024-25:
Total OBR target: 702 Mcm (against FY2023-24 actual of 654 Mcm)
OBR ratio (SECL overall): 3.8 cubic metres of overburden per tonne of coal (consistent with national average)
Gevra OCP: 3.2:1 (favourable due to shallow seams)
Deepening mines (Dipka Phase-III, Kusmunda): 4.8-5.2:1 (increasing with depth)
"""),
            ("Capital Expenditure and Infrastructure", """
Capital Expenditure Plan - SECL FY 2024-25:

Total Capex approved: ₹5,840 crore
Breakdown:
Mine development and expansion: ₹2,940 crore (50.3%)
HEMM procurement: ₹1,820 crore (31.2%) - 42 new dumpers (150T and 240T), 8 draglines refurbishment
Environmental mitigation: ₹480 crore (8.2%)
Township and infrastructure: ₹360 crore (6.2%)
IT and digitalisation: ₹240 crore (4.1%)

HEMM fleet planned additions:
240T dumpers: 18 units (Gevra, Dipka expansion)
150T dumpers: 24 units (Kusmunda, Bhatgaon)
Draglines: 2 additional (Kusmunda new pit)
Shovel-dumper combination: Enhanced by 6 shovel units (42 m³ bucket)
Surface miners: 4 units for selective mining at Raigarh

Washery expansion:
Ambikapur Washery Phase-II: 5 MTPA addition (total capacity 10 MTPA), commissioning Q3 FY2024-25
Bhatgaon Washery Phase-I: 3 MTPA new installation, commissioning Q4 FY2024-25
"""),
            ("Environmental and Social Commitments", """
SECL Environmental and Social Commitments FY 2024-25:

Environmental commitments:
Tree plantation target: 6.5 million saplings (up from 5.2 million in FY2023-24)
Mine reclamation target: 3,200 hectares (progressive mine closure areas)
Water recycling target: 65% of total mine water pumped (vs 58% actual in FY2023-24)
Renewable energy: 250 MW solar plant under development (Bilaspur district); commissioning FY2025-26
PM10 compliance: Implementation of closed conveyor system for coal transport at Gevra (14 km stretch)

CSR investments FY 2024-25: ₹284 crore
Focus areas: Education (Korba district schools), healthcare (mobile medical units), skill development
(mining trades ITI expansion), drinking water (32 villages in mining affected zones)

R&R (Resettlement and Rehabilitation):
Total families displaced (cumulative to FY2023-24): 12,842
R&R completed: 11,980 families (93.3%)
Pending R&R: 862 families (under process; all within policy timelines)
Compensation disbursed: ₹1,240 crore (cumulative)

OBR ratio management and compliance:
As stipulated in EC conditions for SECL opencast mines, the OBR ratio is maintained at or below
3.8:1. Compliance is reported quarterly to MoEFCC and OSPCB/CGSPCB.
"""),
        ]
    },
}


def _safe(text: str) -> str:
    """Encode to latin-1 safe ASCII, replacing unmappable chars. Also break long words."""
    text = text.encode("latin-1", errors="replace").decode("latin-1")
    # Break any word longer than 60 chars (prevents fpdf layout crash)
    words = text.split(" ")
    out = []
    for w in words:
        if len(w) > 60:
            out.extend([w[i:i+60] for i in range(0, len(w), 60)])
        else:
            out.append(w)
    return " ".join(out)


def generate_all_pdfs():
    os.makedirs(OUT_DIR, exist_ok=True)
    for filename, doc in DOCS.items():
        path = os.path.join(OUT_DIR, filename)
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_margins(20, 20, 20)

        for page_num, (heading, content) in enumerate(doc["pages"], start=1):
            pdf.add_page()
            if page_num == 1:
                pdf.set_font("Helvetica", "B", 14)
                pdf.multi_cell(0, 8, _safe(doc["title"]))
                pdf.ln(4)
                pdf.set_font("Helvetica", "", 9)
                pdf.set_text_color(120, 120, 120)
                pdf.cell(0, 6, "CMPDI / Coal India Limited - Confidential Internal Document",
                         new_x="LMARGIN", new_y="NEXT")
                pdf.set_text_color(0, 0, 0)
                pdf.ln(6)

            pdf.set_font("Helvetica", "B", 11)
            pdf.multi_cell(0, 7, _safe(f"Section {page_num}: {heading}"))
            pdf.ln(3)

            pdf.set_font("Helvetica", "", 10)
            for line in content.strip().split("\n"):
                line = _safe(line.strip())
                if not line:
                    pdf.ln(3)
                else:
                    try:
                        pdf.multi_cell(0, 5.5, line)
                    except Exception:
                        # skip any line that causes a layout error
                        pass

        pdf.output(path)
        print(f"  Generated: {filename} ({len(doc['pages'])} pages)")

    print(f"\nAll PDFs written to: {OUT_DIR}")


if __name__ == "__main__":
    generate_all_pdfs()

