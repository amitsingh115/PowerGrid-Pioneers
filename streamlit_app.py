import streamlit as st
import pandas as pd
import numpy as np

st.title('Smart Grid Management System')

st.info('This app builds smart grid management systems')

with st.expander('Data'):
  st.write('**Power Generation Plants**')
  df = pd.read_csv('https://raw.githubusercontent.com/amitsingh115/PowerGrid-Pioneers/refs/heads/master/Power%20Stations.csv')
  df

  
st.info('power generation')
with st.expander('power generation'):
  #S.no,Power station,Type of energy source,Energy Output
  st.bar_chart(data=df, x='Power station' , y='Energy Output',)

#data preparation
with st.sidebar:
  st.header('input features')
  #S.no,Power station,Source,Energy Output
  Source = st.selectbox('Source',('Renewable','Non-renewable'))



with st.expander('Total Renewable energy production'):
 st.write('**Total renewable energy production**')
 df = pd.read_csv('https://raw.githubusercontent.com/amitsingh115/PowerGrid-Pioneers/refs/heads/master/total%20renewable%20energy%20power%20generation%20new.csv')
 df

with st.expander('Total Renewable energy production line chart'):
 st.line_chart(
    data=df,
    x="time",
    y=["power generation",])


def generate_energy_demand():
    hours = np.arange(24)
    demand = np.random.randint(100, 500, size=24)  # Random demand values
    return pd.DataFrame({"Hour": hours, "Demand (MW)": demand})

def main():
    st.title("Advanced Smart Grid Management")
    st.markdown("Optimizing energy distribution for a sustainable future")

    # Load energy demand data
    energy_demand_df = generate_energy_demand()

    # User input for real-time optimization
    user_input = st.slider("Adjust Demand (MW)", min_value=0, max_value=1000, value=500)

    # Predicted demand (simple linear model)
    predicted_demand = user_input * 0.9  # Placeholder prediction (adjust as needed)

    st.subheader("Real-Time Energy Distribution")
    st.markdown(f"Predicted Demand: {predicted_demand:.2f} MW")

    # Display energy demand chart
    st.subheader("Hourly Energy Demand")
    st.line_chart(energy_demand_df.set_index("Hour"))

    # Placeholder renewable energy integration
    st.subheader("Renewable Energy Sources")
    st.markdown("Integrating solar and wind power seamlessly...")

    # Placeholder for Sign Up form

    # Placeholder for Grid Management content
    st.subheader("Grid Management")
    st.markdown("All the content related to grid management goes here...")

    st.markdown("---")
    st.markdown("This is an advanced example. In practice, you'd use real data, more sophisticated models, and optimization algorithms for smart grid management.")

if __name__ == "__main__":
    main()

#New coding of failure mechanism

import streamlit as st
import time

# Define Substation class
class Substation:
    def __init__(self, name, load_threshold):
        self.name = name
        self.load = 0  # Initial load is 0 MW
        self.load_threshold = load_threshold  # Load threshold in MW
        self.power_status = True  # Power is ON initially

    def set_load(self, load):
        self.load = load
        self.check_overload()

    def check_overload(self):
        """Checks if the load exceeds the threshold and cuts power if necessary."""
        if self.load > self.load_threshold:
            self.power_status = False
        else:
            self.power_status = True

    def get_status(self):
        """Returns the power status as 'ONLINE' or 'OFFLINE'."""
        return "ONLINE" if self.power_status else "OFFLINE"


# Initialize grid system with multiple substations
substations = [
    Substation("North Substation", 100),  # Substation name, Load threshold (MW)
    Substation("South Substation", 120),
    Substation("East Substation", 90),
    Substation("West Substation", 110)
]

# Title of the app
st.title("Smart Grid Power Failure Mechanism")

st.write("### Monitor and manage power distribution in the grid")

# Sidebar inputs for load values
st.sidebar.header("Set Substation Loads (MW)")

# Allow the user to input load for each substation
for substation in substations:
    load = st.sidebar.slider(f"Set Load for {substation.name} (MW)", 0, 150, 50)
    substation.set_load(load)

# Display substation status
st.write("### Substation Status")
for substation in substations:
    # Display each substation's status
    st.write(f"**{substation.name}**: Load = {substation.load} MW | Status = {substation.get_status()}")

# Simulate the system in real-time (optional)
st.write("### Monitoring System")
if st.button("Start Monitoring"):
    st.write("Monitoring grid...")
    for i in range(10):  # Simulate monitoring for 10 cycles
        for substation in substations:
            # Update status and display in real-time
            substation.check_overload()
            status = substation.get_status()
            st.write(f"{substation.name} Status: {status}")
            time.sleep(1)  # Simulate delay between cycles

st.write("Note: Power will be cut if the load exceeds the substation's threshold.")


#   Weather Forecast

import streamlit as st
import requests
import json

# Constants
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key from a weather service

# Function to fetch weather data
def get_weather_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        
        forecast = {
            "Temperature": f"{main['temp']} °C",
            "Humidity": f"{main['humidity']} %",
            "Pressure": f"{main['pressure']} hPa",
            "Wind Speed": f"{wind['speed']} m/s",
            "Description": weather_desc
        }
        return forecast
    else:
        return None

# Substation class for managing substations
class Substation:
    def __init__(self, id, load, has_fault):
        self.id = id
        self.load = load
        self.has_fault = has_fault
        self.power_cut = False

    def cut_power(self):
        self.power_cut = True

    def restore_power(self):
        self.power_cut = False

    def status(self):
        status = "Power Cut" if self.power_cut else "Active"
        return {
            "ID": self.id,
            "Load": self.load,
            "Has Fault": self.has_fault,
            "Status": status
        }

# Function to simulate grid monitoring and auto-cut power
def monitor_grid(substations):
    for substation in substations:
        if substation.load > 80 or substation.has_fault:
            substation.cut_power()
        elif substation.power_cut and substation.load <= 80 and not substation.has_fault:
            substation.restore_power()

# Streamlit Sidebar for navigation
option = st.sidebar.selectbox(
    "Choose an option",
    ["Grid Management", "Weather Forecast"]
)

# Grid Management Option
if option == "Grid Management":
    st.title("Smart Grid Management System")

    # Initialize substations (could be dynamic, but hardcoded for now)
    substations = [
        Substation(1, 60, False),
        Substation(2, 85, False),  # Overload
        Substation(3, 50, True),   # Fault detected
        Substation(4, 75, False),
        Substation(5, 90, False)   # Overload
    ]

    # Monitor the grid
    monitor_grid(substations)

    # Display Substation statuses
    st.subheader("Substation Statuses")
    for substation in substations:
        status = substation.status()
        st.write(f"Substation ID: {status['ID']}")
        st.write(f"Load: {status['Load']}%")
        st.write(f"Fault: {status['Has Fault']}")
        st.write(f"Status: {status['Status']}")
        st.write("---")

# Weather Forecast Option
elif option == "Weather Forecast":
    st.title("Weather Forecast")

    # Input for city name
    city = st.text_input("Enter city name for weather forecast:", "New York")

    if st.button("Get Forecast"):
        forecast = get_weather_forecast(city)
        
        if forecast:
            st.subheader(f"Weather forecast for {city.capitalize()}:")
            st.write(f"Temperature: {forecast['Temperature']}")
            st.write(f"Humidity: {forecast['Humidity']}")
            st.write(f"Pressure: {forecast['Pressure']}")
            st.write(f"Wind Speed: {forecast['Wind Speed']}")
            st.write(f"Weather Description: {forecast['Description']}")
        else:
            st.error("Could not fetch weather data. Please check the city name or try again later.")


#F2 Smartload balancing 

import streamlit as st
import requests

# Constants
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key from a weather service

# Function to fetch weather data
def get_weather_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        
        forecast = {
            "Temperature": f"{main['temp']} °C",
            "Humidity": f"{main['humidity']} %",
            "Pressure": f"{main['pressure']} hPa",
            "Wind Speed": f"{wind['speed']} m/s",
            "Description": weather_desc
        }
        return forecast
    else:
        return None

# Substation class for managing substations
class Substation:
    def __init__(self, id, load, has_fault):
        self.id = id
        self.load = load
        self.has_fault = has_fault
        self.power_cut = False

    def cut_power(self):
        self.power_cut = True

    def restore_power(self):
        self.power_cut = False

    def status(self):
        status = "Power Cut" if self.power_cut else "Active"
        return {
            "ID": self.id,
            "Load": self.load,
            "Has Fault": self.has_fault,
            "Status": status
        }

# Energy Source class
class EnergySource:
    def __init__(self, name, capacity, efficiency):
        self.name = name
        self.capacity = capacity  # Max capacity in MW
        self.efficiency = efficiency  # Efficiency (0-100%)
        self.current_output = 0  # Current output in MW

    def provide_energy(self, demand):
        available = min(self.capacity, demand)
        self.current_output = available
        return available

    def reset_output(self):
        self.current_output = 0

    def status(self):
        return f"{self.name}: Output {self.current_output} MW / Capacity {self.capacity} MW"

# Function to simulate load balancing
def smart_load_balancing(substations, energy_sources):
    total_demand = sum([substation.load for substation in substations if not substation.power_cut])
    remaining_demand = total_demand

    # Prioritize energy sources based on efficiency
    energy_sources.sort(key=lambda x: x.efficiency, reverse=True)

    # Allocate energy from most efficient sources
    for source in energy_sources:
        if remaining_demand > 0:
            provided = source.provide_energy(remaining_demand)
            remaining_demand -= provided
        else:
            source.reset_output()

    if remaining_demand > 0:
        st.warning(f"Warning: Unmet demand of {remaining_demand} MW. Consider adding more capacity.")

    # Display energy source statuses
    for source in energy_sources:
        st.write(source.status())

# Function to simulate grid monitoring
def monitor_grid(substations):
    for substation in substations:
        if substation.load > 80 or substation.has_fault:
            substation.cut_power()
        elif substation.power_cut and substation.load <= 80 and not substation.has_fault:
            substation.restore_power()

# Streamlit Sidebar for navigation
option = st.sidebar.selectbox(
    "Choose an option",
    ["Grid Management", "Weather Forecast", "Smart Load Balancing"]
)

# Initialize substations and energy sources
substations = [
    Substation(1, 60, False),
    Substation(2, 85, False),  # Overloaded
    Substation(3, 50, True),   # Fault detected
    Substation(4, 75, False),
    Substation(5, 90, False)   # Overloaded
]

# Energy sources with different capacities and efficiencies
energy_sources = [
    EnergySource("Fossil Fuel Plant", 150, 50),  # Capacity 150 MW, 50% efficiency
    EnergySource("Wind Farm", 80, 90),           # Capacity 80 MW, 90% efficiency
    EnergySource("Solar Plant", 50, 85),         # Capacity 50 MW, 85% efficiency
]

# Grid Management Option
if option == "Grid Management":
    st.title("Smart Grid Management System")

    # Monitor the grid for overloads or faults
    monitor_grid(substations)

    # Display Substation statuses
    st.subheader("Substation Statuses")
    for substation in substations:
        status = substation.status()
        st.write(f"Substation ID: {status['ID']}")
        st.write(f"Load: {status['Load']}%")
        st.write(f"Fault: {status['Has Fault']}")
        st.write(f"Status: {status['Status']}")
        st.write("---")

# Weather Forecast Option
elif option == "Weather Forecast":
    st.title("Weather Forecast")

    # Input for city name
    city = st.text_input("Enter city name for weather forecast:", "New York")

    if st.button("Get Forecast"):
        forecast = get_weather_forecast(city)
        
        if forecast:
            st.subheader(f"Weather forecast for {city.capitalize()}:")
            st.write(f"Temperature: {forecast['Temperature']}")
            st.write(f"Humidity: {forecast['Humidity']}")
            st.write(f"Pressure: {forecast['Pressure']}")
            st.write(f"Wind Speed: {forecast['Wind Speed']}")
            st.write(f"Weather Description: {forecast['Description']}")
        else:
            st.error("Could not fetch weather data. Please check the city name or try again later.")

# Smart Load Balancing Option
elif option == "Smart Load Balancing":
    st.title("Smart Load Balancing System")

    st.subheader("Substation Demand")
    total_demand = sum([substation.load for substation in substations if not substation.power_cut])
    st.write(f"Total Energy Demand: {total_demand} MW")

    st.subheader("Energy Source Allocation")
    smart_load_balancing(substations, energy_sources)

#line chart of different sources
import pandas as pd
import numpy as np

# Function to simulate energy production over time
def simulate_energy_production(hours=12):
    # Randomly simulate production data for 24 hours
    time_range = pd.date_range(start="00:00", periods=hours, freq="H")
    
    # Simulated data for each energy source
    solar_production = np.clip(np.sin(np.linspace(0, np.pi, hours)) * 50, 0, 50)  # Solar peaks during the day
    wind_production = np.random.normal(loc=60, scale=15, size=hours)  # Wind varies but stays active
    thermal_production = np.full(hours, 100)  # Thermal power is steady
    
    # Creating DataFrame for the energy production
    energy_data = pd.DataFrame({
        "Time": time_range,
        "Solar Farm": solar_production,
        "Wind Farm": wind_production,
        "Thermal Power Plant": thermal_production
    }).set_index("Time")
    
    return energy_data

# Use the function to simulate energy production for 24 hours
energy_data = simulate_energy_production(hours=12)

# Display the line chart in your Streamlit app
st.subheader("Energy Production Over 12 Hours")
st.line_chart(energy_data)

st.write("This chart shows the simulated energy production for the Solar Farm, Wind Farm, and Thermal Power Plant over the last 24 hours.")




    

  


  
  
  
