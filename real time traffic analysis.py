import time
import random
from collections import defaultdict

class TrafficSensor:
    def __init__(self, name):
        self.name = name

    def get_traffic_intensity(self):
        # Simulate traffic intensity data
        return random.randint(0, 100)

class TrafficManagementSystem:
    def __init__(self):
        self.sensors = {}  # Dictionary to store traffic sensors
        self.sensor_data = defaultdict(list)  # Dictionary to store historical sensor data

    def add_sensor(self, sensor):
        self.sensors[sensor.name] = sensor

    def collect_data(self):
        while True:
            for name, sensor in self.sensors.items():
                intensity = sensor.get_traffic_intensity()
                self.sensor_data[name].append((time.time(), intensity))  # Record timestamped intensity data
            time.sleep(1)  # Collect data every second

    def analyze_data(self):
        while True:
            print("Traffic Analysis:")
            for name, data in self.sensor_data.items():
                if data:
                    latest_time, latest_intensity = data[-1]
                    print(f"{name}: Intensity {latest_intensity}% at {time.ctime(latest_time)}")
            print("-------------------")
            time.sleep(5)  # Analyze data every 5 seconds

# Example usage:
sensor1 = TrafficSensor("Sensor1")
sensor2 = TrafficSensor("Sensor2")

traffic_system = TrafficManagementSystem()
traffic_system.add_sensor(sensor1)
traffic_system.add_sensor(sensor2)

# Start data collection and analysis threads
import threading
collection_thread = threading.Thread(target=traffic_system.collect_data)
analysis_thread = threading.Thread(target=traffic_system.analyze_data)

collection_thread.start()
analysis_thread.start()

# Keep the main thread alive
collection_thread.join()
analysis_thread.join()
