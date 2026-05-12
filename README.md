IWRAS: Inland Water Risk Assessment System

Predictive Safety Architecture for Artisanal Fisheries in Lake Victoria

🔬 Project Overview

IWRAS is a deterministic risk-modeling framework designed to mitigate drowning fatalities in Lake Victoria. By analyzing high-resolution (5-minute interval) hydro-meteorological data from the TAHMO sensor network, the system translates raw environmental variables into an actionable Safety Integrity Level (SIL).

This project focuses on the "Data-to-Decision Gap", specifically targeting the safety of artisanal fishers operating small wooden vessels who are highly vulnerable to sudden nocturnal convective storms.

🚀 Key Features & Methodology

Multi-Parametric Risk Scoring: A weighted tri-factor algorithm:

Wind Gusts (50%): Primary vector for vessel capsizing.

Barometric Pressure Drops (30%): A critical precursor providing 30-60 minutes of lead time.

Temperature Lapse (20%): Identifying the onset of convective storm cells.

Smart Data Imputation: Robust handling of sensor dropouts using linear interpolation.

Forensic Validation: Cross-referenced algorithmic "Red Alerts" with documented historical maritime incidents (2023-2024).

📊 Forensic Validation Highlights

The system has been retrospectively validated against real-world catastrophes:

January 11, 2023: IWRAS flagged a critical peak at the Tanzania (LVBWB) station, synchronized with severe flash floods and heavy rainfall reported in the region.

March-May 2024: Sustained high-risk indicators aligned with the El Niño-induced anomalies that caused over 150 fatalities in the basin.

📂 Repository Structure

/core: analyze_tahmo_data.py - The batch processing engine for risk estimation.

/simulation: drowning_risk_simulation.py - Proof-of-concept prototype for logic testing.

/visualization: visualize_all_stations.py - Tools for generating dual-axis forensic charts (Wind/Pressure).

/docs: Technical documentation and forensic analysis reports.

🛠 Installation & Usage

Clone the repository:

git clone [https://github.com/mahdibigham/IWRAS.git](https://github.com/mahdibigham/IWRAS.git)


Install dependencies:

pip install pandas numpy matplotlib


Run the visualizer:

python visualization/visualize_all_stations.py


👤 Author

Mahdi Bigham
Research Expert at National University of Skills (NUS)

LinkedIn Profile

ResearchGate

🤝 Collaboration & Acknowledgments

This research is conducted under the scientific guidance of Professor Nick van de Giesen (TU Delft) and utilizes data provided by the TAHMO Network.

Disclaimer: This is a research prototype intended for academic validation and pilot studies.
