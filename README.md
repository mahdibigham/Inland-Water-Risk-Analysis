Inland Water Risk Assessment System (IWRAS)

A Proactive Safety Initiative for Non-Standard Water Bodies

🔬 Project Context & Research Goal

This repository hosts the Proof of Concept (PoC) for IWRAS, a research initiative aimed at shifting drowning prevention from reactive measures (rescue) to predictive safety (risk estimation).

Unlike swimming pools, inland water bodies (dams, reservoirs, urban lakes) lack standardized supervision. This project investigates how Environmental AI can quantify safety risks in real-time.

🛠 System Architecture (Prototype)

The current implementation (drowning_risk_simulation.py) is a deterministic simulation model written in Python. It calculates a dynamic "Risk Index" based on three weighted environmental variables:

Surface Stability: Wind speed interaction with water surface.

Physiological Stress: Hypothermia risk calculated from water temperature.

Operational Visibility: Atmospheric visibility impacting rescue viability.

🚀 Roadmap & Future Development

This project is currently in the Pre-Alpha / Research Phase. The development roadmap includes:

Phase 1 (Current): Python-based simulation of risk logic (Completed).

Phase 2: Integration with real-world meteorological APIs (e.g., OpenWeatherMap).

Phase 3 (Performance): Porting the core risk-calculation engine to C++.

Objective: To deploy the system on low-power Embedded Edge Devices (IoT sensors) located at remote water sites, requiring efficient memory management and real-time processing.

👤 About the Author

Mahdi Bigham
Research Expert & Head of Open Education | National University of Skills (NUS)

With a background in University Operations and experience teaching C++ and Hardware-Oriented Programming, I focus on designing Interpretable Decision-Support Systems for safety-critical environments. My research aims to bridge the gap between theoretical safety protocols and practical, algorithmic enforcement.

For academic inquiries or collaboration, please open an issue in this repository.
