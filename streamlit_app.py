import streamlit as st
import panda as pd

st.title('Smart Grid Management System')

st.info('This app builds smart grid management systems')

df = pd.read_csv('https://raw.githubusercontent.com/amitsingh115/PowerGrid-Pioneers/refs/heads/master/Power%20Stations.csv')
df
