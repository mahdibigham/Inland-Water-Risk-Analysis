RESEARCH PROPOSAL CONCEPT NOTE

Project Title: Inland Water Risk Assessment System (IWRAS): A Data-Driven Approach to Preventive Safety
Applicant: Mahdi Bigham
Affiliation: National University of Skills (NUS) - Research Expert
Date: January 2026

1. The Scientific Problem

Safety protocols in inland water bodies (canals, urban lakes, recreational reservoirs) are predominately reactive. Measures such as warning signs or patrols are typically static and fail to adapt to rapidly changing environmental parameters.

As a Research Expert at National University of Skills, I have analyzed operational safety workflows and identified a critical gap: the lack of real-time, data-driven risk estimation leads to avoidable accidents and inefficient allocation of rescue resources.

2. The Proposed Solution

IWRAS is proposed as a predictive safety architecture. Instead of relying on human intuition or static schedules, it utilizes environmental data to calculate a dynamic "Safety Integrity Level" (SIL) or Risk Index. The objective is to transition the operational paradigm from "Incident Response" to "Incident Prevention."

3. Methodology & Logic

The system logic prioritizes interpretability—ensuring that automated decisions can be verified by human safety officers. The prototype assesses risk based on weighted vectors:

Surface Dynamics: Monitoring wind speed (Critical threshold: >25 km/h).

Physiological Risk: Monitoring water temperature for cold shock/hypothermia probability (Critical threshold: <5°C).

Rescue Viability: Assessing fog/haze levels (Critical threshold: <200m).

4. Technical Feasibility & Roadmap

A functional simulation model has been developed in Python to validate the algorithmic logic.

Future Development (C++ / Embedded):
To ensure the system can operate in remote locations with limited power and connectivity, the next phase of research involves re-engineering the core logic using C++. This will facilitate deployment on Edge IoT devices, leveraging hardware-oriented programming techniques to ensure real-time responsiveness and system stability.

5. Relevance to Applied Research

This project aligns with the goals of Smart City Safety and Resilient Environmental Management. It serves as a practical application of "Safety-Critical System Design," bridging the gap between academic risk theory and operational deployment.
