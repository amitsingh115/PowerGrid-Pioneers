import streamlit as st
import pandas as pd

st.title('Smart Grid Management System')

st.info('This app builds smart grid management systems')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/amitsingh115/PowerGrid-Pioneers/refs/heads/master/Power%20Stations.csv')
  df
