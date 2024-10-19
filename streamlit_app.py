import streamlit as st
import pandas as pd

st.title('Smart Grid Management System')

st.info('This app builds smart grid management systems')

with st.expander('Data'):
  st.write('**Power Generation Plants**')
  df = pd.read_csv('https://raw.githubusercontent.com/amitsingh115/PowerGrid-Pioneers/refs/heads/master/Power%20Stations.csv')
  df

  

with st.expander('power generation'):
  #S.no,Power station,Type of energy source,Energy Output
  st.bar_chart(data=df, x='Power station' , y='Energy Output')
