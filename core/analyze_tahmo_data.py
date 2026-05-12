# -*- coding: utf-8 -*-
"""
IWRAS Batch Analysis Engine
Author: Mahdi Bigham
Task: Analyze TAHMO station data and export "Red Alert" events to CSV.
"""

import pandas as pd
import numpy as np
import os

class IWRAS_Analyzer:
    def __init__(self, station_files):
        self.station_files = station_files
        self.all_alerts = []

    def run_analysis(self):
        print(f"{'Station':<20} | {'Max Risk':<12} | {'Red Alert Count'}")
        print("-" * 55)
        
        for name, path in self.station_files.items():
            if not os.path.exists(path):
                continue
            
            df = pd.read_csv(path)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            # Data Cleaning: Interpolate missing sensor values (max 1 hour gap)
            cols = ['windgusts (m/s)', 'atmosphericpressure (kPa)', 'temperature (degrees Celsius)']
            df[cols] = df[cols].interpolate(method='linear', limit=12)
            
            # IWRAS Risk Logic Calculations
            df['g_idx'] = np.minimum(df['windgusts (m/s)'] / 12.0, 1.5)
            # Pressure drop over 1 hour (12 periods of 5 mins)
            df['p_idx'] = (df['atmosphericpressure (kPa)'].diff(periods=12) * -1).clip(lower=0) / 0.15
            df['t_idx'] = (df['temperature (degrees Celsius)'].diff(periods=12) * -1).clip(lower=0) / 2.5
            
            # Weighted Risk Score
            df['total_risk'] = (df['g_idx'] * 0.5) + (df['p_idx'] * 0.3) + (df['t_idx'] * 0.2)
            
            # Filter for Critical (RED) events
            reds = df[df['total_risk'] > 0.75].copy()
            reds['station'] = name
            if not reds.empty:
                self.all_alerts.append(reds[['timestamp', 'station', 'windgusts (m/s)', 'total_risk']])
            
            print(f"{name:<20} | {df['total_risk'].max():<12.3f} | {len(reds)}")

        if self.all_alerts:
            pd.concat(self.all_alerts).to_csv('red_alerts_summary.csv', index=False)
            print("\n[Success] Critical alerts exported to red_alerts_summary.csv")

if __name__ == "__main__":
    BASE = os.path.dirname(os.path.abspath(__file__))
    my_stations = {
        'Entebbe Airport': os.path.join(BASE, 'TA00215.csv'),
        'Jinja Airfield': os.path.join(BASE, 'TA00227.csv'),
        'Tanzania LVBWB': os.path.join(BASE, 'TA00590.csv')
    }
    IWRAS_Analyzer(my_stations).run_analysis()
