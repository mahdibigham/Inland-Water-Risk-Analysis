# -*- coding: utf-8 -*-
"""
IWRAS Multi-Station Visualizer
Author: Mahdi Bigham
Task: Plot forensic correlation between wind gusts and pressure drops for research papers.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_stations(station_map):
    n = len(station_map)
    fig, axes = plt.subplots(n, 1, figsize=(15, n * 6))
    if n == 1: axes = [axes]
    
    for i, (name, path) in enumerate(station_map.items()):
        if not os.path.exists(path): continue
        
        df = pd.read_csv(path)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Identify the peak storm moment for visualization
        peak_idx = df['windgusts (m/s)'].idxmax()
        peak_time = df.loc[peak_idx, 'timestamp']
        
        # Filter a 12-hour window around the event
        mask = (df['timestamp'] > peak_time - pd.Timedelta(hours=9)) & \
               (df['timestamp'] < peak_time + pd.Timedelta(hours=3))
        pdf = df[mask]
        
        ax = axes[i]
        # Primary Axis: Wind Gust
        ax.plot(pdf['timestamp'], pdf['windgusts (m/s)'], color='blue', label='Wind Gust (m/s)')
        ax.set_ylabel('Wind Gust (m/s)', color='blue', fontweight='bold')
        
        # Secondary Axis: Barometric Pressure
        if 'atmosphericpressure (kPa)' in pdf.columns:
            ax2 = ax.twinx()
            ax2.plot(pdf['timestamp'], pdf['atmosphericpressure (kPa)'], color='green', linestyle='--', label='Pressure')
            ax2.set_ylabel('Pressure (kPa)', color='green', fontweight='bold')
            
        ax.set_title(f"Forensic View - Station: {name} | Event Date: {peak_time.date()}")
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    # Save the output for the Research Proposal
    plt.savefig('IWRAS_Forensic_Chart.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    BASE = os.path.dirname(os.path.abspath(__file__))
    stations = {
        'Entebbe Airport': os.path.join(BASE, 'TA00215.csv'),
        'Jinja Airfield': os.path.join(BASE, 'TA00227.csv')
    }
    plot_stations(stations)
