# -*- coding: utf-8 -*-
"""
IWRAS Multi-Station Visualizer (v2.3)
Author: Mahdi Bigham
Generates high-resolution forensic charts for TAHMO stations.
Ensures output filename is: IWRAS_Forensic_Chart.png
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class IWRASVisualizer:
    def __init__(self, station_map, base_dir):
        self.station_map = station_map
        self.base_dir = base_dir

    def analyze_station(self, file_path):
        """
        Executes IWRAS risk logic and prepares data for forensic plotting.
        """
        if not os.path.exists(file_path):
            print(f"Warning: File not found at {file_path}")
            return None

        try:
            df = pd.read_csv(file_path)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df = df.sort_values('timestamp')

            # Smart interpolation for sensor dropouts (up to 1 hour)
            cols = ['temperature (degrees Celsius)', 'windgusts (m/s)', 'atmosphericpressure (kPa)']
            present_cols = [c for c in cols if c in df.columns]
            df[present_cols] = df[present_cols].interpolate(method='linear', limit=12)

            # Drop rows missing vital sensor data
            df = df.dropna(subset=['windgusts (m/s)', 'temperature (degrees Celsius)'])
            
            if df.empty: return None

            # Calculate IWRAS component scores
            df['g_score'] = np.minimum(df['windgusts (m/s)'] / 12.0, 1.5)
            
            df['p_score'] = 0
            if 'atmosphericpressure (kPa)' in df.columns:
                p_drop = df['atmosphericpressure (kPa)'].diff(periods=12) * -1
                df['p_score'] = np.maximum(p_drop / 0.15, 0)

            t_drop = df['temperature (degrees Celsius)'].diff(periods=12) * -1
            df['t_score'] = np.maximum(t_drop / 2.5, 0)

            # Calculate Final Integrated Risk Index
            df['total_risk'] = (df['g_score'] * 0.5) + (df['p_score'] * 0.3) + (df['t_score'] * 0.2)
            
            return df
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            return None

    def plot_all_summaries(self):
        """
        Plots combined charts for all stations centered on the peak risk event.
        """
        active_stations = {name: path for name, path in self.station_map.items() if os.path.exists(path)}
        num_stations = len(active_stations)
        
        if num_stations == 0:
            print("No valid data files found to plot.")
            return

        fig_height = num_stations * 8
        fig, axes = plt.subplots(nrows=num_stations, ncols=1, figsize=(16, fig_height))
        
        if num_stations == 1: axes = [axes]

        fig.subplots_adjust(hspace=0.6, top=0.94, bottom=0.06)

        for i, (name, path) in enumerate(active_stations.items()):
            df = self.analyze_station(path)
            ax = axes[i]
            
            if df is None:
                ax.text(0.5, 0.5, f"Data Error: {name}", ha='center', va='center')
                ax.set_axis_off()
                continue

            # Identify the peak risk moment (Composite Risk, not just wind)
            peak_idx = df['total_risk'].idxmax()
            peak_time = df.loc[peak_idx, 'timestamp']

            # Visualization Window: 12 hours before and 4 hours after peak
            mask = (df['timestamp'] > peak_time - pd.Timedelta(hours=12)) & \
                   (df['timestamp'] < peak_time + pd.Timedelta(hours=4))
            plot_df = df.loc[mask]

            if plot_df.empty:
                ax.text(0.5, 0.5, f"No significant events in {name}", ha='center', va='center')
                continue

            # Plot Axis 1: Wind Gust
            ax.plot(plot_df['timestamp'], plot_df['windgusts (m/s)'], color='#1f77b4', lw=2.5, label='Wind Gust (m/s)')
            ax.set_ylabel('Wind Gust (m/s)', color='#1f77b4', fontsize=12, fontweight='bold')
            ax.tick_params(axis='y', labelcolor='#1f77b4')
            
            # Danger Threshold Line
            ax.axhline(y=12, color='red', linestyle='--', alpha=0.6, label='Danger Threshold (12m/s)')

            # Plot Axis 2: Atmospheric Pressure
            if 'atmosphericpressure (kPa)' in plot_df.columns:
                ax2 = ax.twinx()
                ax2.plot(plot_df['timestamp'], plot_df['atmosphericpressure (kPa)'], color='#2ca02c', ls=':', lw=2, label='Pressure')
                ax2.set_ylabel('Pressure (kPa)', color='#2ca02c', fontsize=12, fontweight='bold')
                ax2.tick_params(axis='y', labelcolor='#2ca02c')

            ax.set_title(f"Station: {name} | Peak Risk Index: {df['total_risk'].max():.2f} at {peak_time}", 
                         fontsize=16, fontweight='bold', pad=15)
            ax.grid(True, alpha=0.3)
            ax.legend(loc='upper left')

        fig.suptitle("IWRAS Forensic Analysis: Correlation between Pressure Dips and Wind Gusts", 
                     fontsize=22, fontweight='bold', y=0.99)
        
        # CORRECTED OUTPUT FILENAME
        save_path = os.path.join(self.base_dir, 'IWRAS_Forensic_Chart.png')
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n[SUCCESS] Forensic analysis complete. Chart saved at: {save_path}")
        plt.show()

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    stations = {
        'Entebbe WME': os.path.join(BASE_DIR, 'TA00033.csv'),
        'Entebbe Airport': os.path.join(BASE_DIR, 'TA00215.csv'),
        'Jinja Airfield': os.path.join(BASE_DIR, 'TA00227.csv'),
        'Kenya Greenergia': os.path.join(BASE_DIR, 'TA00146.csv'),
        'Tanzania LVBWB': os.path.join(BASE_DIR, 'TA00590.csv')
    }

    viz = IWRASVisualizer(stations, BASE_DIR)
    viz.plot_all_summaries()
