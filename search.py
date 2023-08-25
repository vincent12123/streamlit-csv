import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv("data_siswa.csv")

# Add title
st.title("Dashboard Data Siswa")

# Add sidebar
st.sidebar.title("Filter Data Siswa")

# Add search input
search_input = st.sidebar.text_input("Cari siswa")

# Filter data based on search query
if search_input:
    data = data[data["nama"].str.contains(search_input, case=False)]

# Add dropdown widget for gender filter
gender_filter = st.sidebar.selectbox("Filter berdasarkan jenis kelamin", ["Semua", "Laki-laki", "Perempuan"])

# Filter data based on gender selection
if gender_filter != "Semua":
    data = data[data["KELAMIN"] == gender_filter]

# Add slider widget for age filter
age_filter = st.sidebar.slider("Filter berdasarkan umur", 14, 18, (14, 18))

# Filter data based on age range selection
data = data[(data["umur"] >= age_filter[0]) & (data["umur"] <= age_filter[1])]

# Display filtered data
st.write("Data Siswa")
st.write(data)

# Add bar chart for father's occupation
father_occupation_count = data["Pekerjaan Ayah"].value_counts()
fig = px.bar(father_occupation_count, x=father_occupation_count.index, y=father_occupation_count.values)
fig.update_layout(title="Jumlah Siswa Berdasarkan Pekerjaan Ayah")
st.plotly_chart(fig)