import streamlit as st
import pandas as pd

# Load data
data = pd.read_csv("data_siswa.csv")

# Display data
st.write("Data Siswa")
st.write(data)