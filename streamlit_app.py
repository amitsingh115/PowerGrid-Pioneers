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

    

  


  
  
  
