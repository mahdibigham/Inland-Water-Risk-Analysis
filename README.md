# Inland Water Risk Assessment (PoC)

## Context
This is a **Proof of Concept (PoC)** developed as part of my research proposal on proactive drowning prevention. The goal is to demonstrate how environmental variables can be quantified into a real-time "Risk Score" for lifeguards.

## How it Works
The script simulates environmental conditions (Wind, Water Temp, Visibility) typical for inland lakes. It then runs a weighted logic model to classify safety conditions into Low, Medium, or High risk levels.

I focused on **predictive logic** rather than detection. For example, high wind speed combined with low water temperature triggers a high-risk alert even if no swimmer is currently in distress.

## Project Structure
- `drowning_risk_simulation.py`: Main script containing the data generation and risk logic.
- `risk_distribution_plot.png`: Visualization output showing the correlation between wind speed and risk levels.

## Future Improvements
Currently, the model uses synthetic data generated via NumPy. The next step is to connect this logic to real-time API feeds from Dutch meteorological services (e.g., KNMI) to test validity in real-world scenarios.

---
**Author:** Mahdi Bigham
