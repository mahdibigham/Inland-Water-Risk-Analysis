import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration & Thresholds
# These values mimic typical conditions for inland lakes in the Netherlands
SIMULATION_HOURS = 1000
BASE_WIND_SPEED = 15  # km/h
BASE_WATER_TEMP = 10  # Celsius

# Risk Thresholds
CRITICAL_WIND_SPEED = 25
CRITICAL_VISIBILITY = 200
CRITICAL_WATER_TEMP = 5

def generate_synthetic_data(hours):
    """
    Generates synthetic environmental data for testing the risk model.
    In the production phase, this will be replaced by API calls (e.g., KNMI).
    """
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', periods=hours, freq='H')
    
    return pd.DataFrame({
        'timestamp': dates,
        'wind_speed': np.random.normal(BASE_WIND_SPEED, 5, hours),
        'water_temp': np.random.normal(BASE_WATER_TEMP, 3, hours),
        'visibility': np.random.uniform(50, 2000, hours),
        'current_factor': np.random.uniform(0, 10, hours) 
    })

def calculate_risk_score(row):
    """
    Calculates a composite risk score based on environmental instability.
    Logic: Higher wind/current + Lower temp/visibility = Higher Risk.
    """
    risk_score = 0
    
    # Wind factor
    if row['wind_speed'] > CRITICAL_WIND_SPEED:
        risk_score += 3
    elif row['wind_speed'] > 15:
        risk_score += 1
        
    # Temperature factor (Hypothermia risk)
    if row['water_temp'] < CRITICAL_WATER_TEMP:
        risk_score += 3
    elif row['water_temp'] < 10:
        risk_score += 1
        
    # Visibility factor
    if row['visibility'] < CRITICAL_VISIBILITY:
        risk_score += 2
        
    return risk_score

def analyze_risk():
    # 1. Load Data
    lake_data = generate_synthetic_data(SIMULATION_HOURS)
    
    # 2. Apply Risk Model
    lake_data['risk_score'] = lake_data.apply(calculate_risk_score, axis=1)
    
    # 3. Categorize for easier reporting
    bins = [-1, 2, 4, 10]
    labels = ['Low', 'Medium', 'High']
    lake_data['risk_level'] = pd.cut(lake_data['risk_score'], bins=bins, labels=labels)
    
    return lake_data

def visualize_results(data):
    plt.figure(figsize=(10, 6))
    
    sns.scatterplot(
        data=data, 
        x='wind_speed', 
        y='risk_score', 
        hue='risk_level', 
        palette='viridis',
        alpha=0.7
    )
    
    plt.axvline(CRITICAL_WIND_SPEED, color='red', linestyle='--', label='Critical Wind Threshold')
    plt.title('Impact of Wind Speed on Calculated Risk Score')
    plt.xlabel('Wind Speed (km/h)')
    plt.ylabel('Risk Score')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    output_file = 'risk_distribution_plot.png'
    plt.savefig(output_file)
    print(f"Plot saved to {output_file}")

if __name__ == "__main__":
    print("Running Risk Assessment Simulation...")
    df_result = analyze_risk()
    
    print("\nRisk Level Distribution:")
    print(df_result['risk_level'].value_counts())
    
    visualize_results(df_result)
