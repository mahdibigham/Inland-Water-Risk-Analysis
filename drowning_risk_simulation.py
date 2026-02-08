import time
import math

class IWRAS_Research_Engine:
    """
    IWRAS (Inland Water Risk Assessment System) - Initial Prototype for Victoria Pilot
    Developer: Mahdi Bigham
    Goal: Early detection of capsizing risks for small-scale artisanal fishing boats.
    """

    def __init__(self, vessel_type="artisanal_wooden_boat"):
        self.vessel_type = vessel_type
        
        # I've set these thresholds based on the low stability of local wooden boats.
        # These will likely need fine-tuning once we get the actual TAHMO high-res data.
        self.config = {
            "wind_gust_threshold": 12.0,  # Gusts above 12m/s are usually critical for these vessels.
            "temp_drop_critical": 2.5,    # A 2.5C drop per hour often signals a convective storm onset.
            "visibility_critical": 500,   # Anything below 500m is a high disorientation risk at night.
            "sampling_window": 5          # Using 5 samples to smooth out momentary sensor noise.
        }
        self.sensor_history = {"temp": [], "wind": []}

    def _apply_fuzzy_weight(self, value, threshold, inverse=False):
        """
        Using fuzzy-like weights to avoid hard 'binary' alerts.
        I don't want the system to toggle between Green/Red at exactly 11.9 vs 12.0 m/s.
        This approach makes transitions much smoother for real-world sensing.
        """
        if not inverse:
            return min(1.0, value / threshold) if threshold > 0 else 0
        else:
            return max(0.0, 1.0 - (value / threshold)) if threshold > 0 else 0

    def validate_sensor_data(self, data_point):
        """
        Basic integrity check. If a sensor sends null or negative values due to interference, 
        the system shouldn't crash or trigger a false alarm.
        """
        if data_point is None or data_point < 0:
            return False
        return True

    def calculate_integrated_risk(self, gust_speed, temp, visibility):
        """
        Calculating the Integrated Risk Index.
        Note: For small boats, Wind Gusts are far more dangerous than average wind speed,
        so I've given them a 60% weight in the final calculation.
        """
        if not self.validate_sensor_data(gust_speed):
            return -1, 0.0 # Sensor failure or data drop-out

        # Calculating weights (0.0 to 1.0 scale)
        w_gust = self._apply_fuzzy_weight(gust_speed, self.config["wind_gust_threshold"])
        
        # Detecting nocturnal storms (Entebbe style) via sudden temperature drops
        w_temp = 0
        if len(self.sensor_history["temp"]) >= 2:
            drop = self.sensor_history["temp"][-1] - temp
            w_temp = self._apply_fuzzy_weight(drop, self.config["temp_drop_critical"])

        # Navigational risk (heavy rain or tropical fog)
        w_vis = self._apply_fuzzy_weight(visibility, self.config["visibility_critical"], inverse=True)

        # Weighted Index Calculation
        total_risk_index = (w_gust * 0.6) + (w_temp * 0.2) + (w_vis * 0.2)
        
        # Mapping the index to operational SIL (Safety Integrity Level)
        if total_risk_index > 0.75:
            return 3, total_risk_index # RED - Evacuation required
        elif total_risk_index > 0.4:
            return 2, total_risk_index # YELLOW - Warning for small crafts
        else:
            return 1, total_risk_index # GREEN - Normal operations

    def update_history(self, temp, wind):
        """ Storing sensor data for trend analysis in future steps """
        self.sensor_history["temp"].append(temp)
        self.sensor_history["wind"].append(wind)
        if len(self.sensor_history["temp"]) > self.config["sampling_window"]:
            self.sensor_history["temp"].pop(0)

def run_victoria_pilot_simulation():
    """ 
    Simulating a real-world scenario: 
    A sudden nocturnal storm hit near Entebbe at 3:00 AM. 
    """
    engine = IWRAS_Research_Engine()
    
    # Mock data: [Time, Temperature, Wind Gust, Visibility]
    scenarios = [
        ("02:00 AM", 25.0, 4.0, 2000), # Clear weather
        ("02:30 AM", 24.2, 7.5, 1500), # Wind picking up
        ("03:00 AM", 21.5, 13.0, 400), # Sudden temp drop + Critical gust (Danger starts)
        ("03:30 AM", 20.0, 18.5, 200)  # Peak storm - Very low visibility
    ]

    print(f"{'Time':<10} | {'Risk Index':<12} | {'Status':<12} | {'Action'}")
    print("-" * 80)

    for time_label, temp, gust, vis in scenarios:
        level, raw_index = engine.calculate_integrated_risk(gust, temp, vis)
        engine.update_history(temp, gust)
        
        status = "🔴 DANGER" if level == 3 else "🟡 CAUTION" if level == 2 else "🟢 SAFE"
        action = "Immediate return!" if level == 3 else "Stay near shore" if level == 2 else "Conditions Clear"
        
        print(f"{time_label:<10} | {raw_index:<12.2f} | {status:<12} | {action}")

if __name__ == "__main__":
    run_victoria_pilot_simulation()
