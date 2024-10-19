import streamlit as st
import pandas as pd

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
    y=["nuclear power"]
    
)
  


  
  
  
