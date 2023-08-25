import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    data = pd.read_csv("data_siswa.csv")
    return data

def filter_data(data, search_input, gender_filter, age_filter):
    if search_input:
        data = data[data["nama"].str.contains(search_input, case=False)]
    
    if gender_filter != "Semua":
        data = data[data["KELAMIN"] == gender_filter]
    
    data = data[(data["umur"] >= age_filter[0]) & (data["umur"] <= age_filter[1])]
    
    return data

def display_data(data):
    st.write("Data Siswa")
    st.write(data)

def display_father_occupation_chart(data):
    father_occupation_count = data["Pekerjaan Ayah"].value_counts()
    fig = px.bar(father_occupation_count, x=father_occupation_count.index, y=father_occupation_count.values)
    fig.update_layout(title="Jumlah Siswa Berdasarkan Pekerjaan Ayah")
    st.plotly_chart(fig)

def main():
    st.title("Dashboard Data Siswa")
    data = load_data()
    
    st.sidebar.title("Filter Data Siswa")
    search_input = st.sidebar.text_input("Cari siswa")
    gender_filter = st.sidebar.selectbox("Filter berdasarkan jenis kelamin", ["Semua", "Laki-laki", "Perempuan"])
    age_filter = st.sidebar.slider("Filter berdasarkan umur", 0, 18, (10, 18))
    
    filtered_data = filter_data(data, search_input, gender_filter, age_filter)
    display_data(filtered_data)
    display_father_occupation_chart(filtered_data)

if __name__ == "__main__":
    main()