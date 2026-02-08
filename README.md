Inland-Water-Risk-Analysis

A Predictive Safety Architecture for Estimating Drowning Risk in Inland Water Bodies

🔬 Project Overview

This repository contains the Research-Grade Prototype for IWRAS (Inland Water Risk Assessment System). The project focuses on transitioning drowning prevention from reactive rescue to proactive risk modeling in non-standard environments like lakes and reservoirs.

🌍 Current Focus: Lake Victoria Pilot

The current iteration is specifically calibrated for the Lake Victoria (Entebbe Region) case study, addressing the high fatality rates among artisanal fishers caused by sudden nocturnal convective storms.

Key Features of the Algorithm:

Deterministic & Fuzzy Logic: Moving beyond simple binary thresholds to continuous risk estimation.

Weighted Risk Vectors: Prioritizing Wind Gusts (the primary capsize factor) alongside visibility and temperature gradients.

Sensor Reliability Handling: Built-in logic to manage sensor noise and data outliers, essential for safety-critical deployments.

🛠 Technical Stack

Language: Python 3.x (Core Logic)

Architecture: Designed for Edge Computing (optimized for future deployment on ESP32/C++).

Logic: Interpretable Weighted Decision Support.

🚀 Roadmap

[x] Phase 1: Research Prototype & Logic Validation (Current).

[ ] Phase 2: Retrospective Stress-Testing with TAHMO Historical Data.

[ ] Phase 3: Integration with Live API and real-time Dashboard.

[ ] Phase 4: Porting to C++ for low-power embedded hardware.

👤 Author

Mahdi Bigham
Research Expert | National University of Skills (NUS)
Focusing on AI for Public Safety and Smart Water Management.

This is a Proof of Concept (PoC) for academic and collaborative research purposes.
