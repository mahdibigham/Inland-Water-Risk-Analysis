Project Concept Note: IWRAS

Project Name: Inland Water Risk Assessment System (IWRAS)
Author: Mahdi Bigham
Affiliation: Research Expert, National University of Skills (NUS)

1. Problem Statement

Artisanal fishing communities in Lake Victoria face a mortality rate that is among the highest globally, with 3,000 to 5,000 estimated deaths annually. The primary cause is sudden, nocturnal convective storms. While global weather models exist, they fail to provide high-resolution, local-scale "Safety Decisions" for small wooden vessels.

2. The IWRAS Solution

IWRAS is a deterministic risk-estimation framework that bridges the "Data-to-Decision Gap." It operates as a software-defined safety layer that translates raw meteorological variables into a 3-level Safety Integrity Level (SIL).

3. Methodology

The system utilizes a weighted multi-parametric index:

Wind Gusts (50%): The direct physical cause of vessel instability.

Barometric Pressure (30%): A critical early-warning precursor (30-60 min lead time).

Temperature Lapse (20%): Identifying the thermodynamic onset of convective cells.

4. Technical Implementation

Logic Engine: Developed in Python (for research/validation) and C++ (for hardware deployment).

Edge Readiness: Designed to run locally on ESP32-based IoT nodes at landing sites, ensuring functionality during GSM network outages.

5. Collaboration

This project utilizes the TAHMO (Trans-African Hydro-Meteorological Observatory) sensor network and is conducted under the academic guidance of Professor Nick van de Giesen (TU Delft).
