# -*- coding: utf-8 -*-
"""
Inland Water Risk Assessment System (IWRAS) - Simulation Version
Author: Mahdi Bigham
Goal: Validate mathematical logic and simulate critical scenarios without real-time data.
"""

class IWRASSimulator:
    def __init__(self, vessel_type="Artisanal_Wooden_Boat"):
        self.vessel_type = vessel_type
        # Critical thresholds based on Lake Victoria safety standards
        self.config = {
            "wind_gust_threshold": 12.0,  # Critical wind gust limit (m/s)
            "temp_drop_critical": 2.5,    # Temp drop threshold for convective storms
            "sampling_window": 5          # Analysis window in minutes
        }
        self.temp_history = []

    def calculate_integrated_risk(self, wind_gust, current_temp):
        """
        Calculate integrated risk index using weighted parameters.
        """
        
        # 1. Wind Gust Score (Primary Weight: 70%)
        # Score is 1.0 if wind reaches or exceeds 12 m/s
        gust_score = min(1.0, wind_gust / self.config["wind_gust_threshold"])
        
        # 2. Temperature Drop Score (Verification Weight: 30%)
        temp_score = 0
        if self.temp_history:
            # Calculate drop relative to the previous record
            drop = self.temp_history[-1] - current_temp
            temp_score = max(0.0, min(1.0, drop / self.config["temp_drop_critical"]))

        # Final IWRAS Risk Index Formula
        total_risk_index = (gust_score * 0.7) + (temp_score * 0.3)
        
        # Define Alert Levels
        if total_risk_index > 0.75:
            return "RED (Critical)", total_risk_index
        elif total_risk_index > 0.4:
            return "YELLOW (Warning)", total_risk_index
        else:
            return "GREEN (Safe)", total_risk_index

    def update_sensors(self, temp):
        """Update sensor history buffer"""
        self.temp_history.append(temp)
        if len(self.temp_history) > self.config["sampling_window"]:
            self.temp_history.pop(0)

if __name__ == "__main__":
    engine = IWRASSimulator()
    
    # Mock scenarios for logic testing
    # Format: (Time, Temperature, Wind Gust)
    scenarios = [
        ("10:00 AM", 28.0, 3.5),  # Normal conditions
        ("10:05 AM", 27.5, 5.0),  # Mild changes
        ("10:10 AM", 24.0, 14.5), # Convective storm (Sudden temp drop + High wind)
    ]
    
    print(f"--- IWRAS Simulation for {engine.vessel_type} ---")
    print(f"{'Time':<10} | {'Temp':<6} | {'Wind':<8} | {'Risk Index':<10} | {'Status'}")
    print("-" * 65)
    
    for time_label, temp, gust in scenarios:
        status, score = engine.calculate_integrated_risk(gust, temp)
        engine.update_sensors(temp)
        print(f"{time_label:<10} | {temp:<6} | {gust:<8} | {score:<10.2f} | {status}")
