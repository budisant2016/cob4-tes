import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Dashboard Analisis Data Baru")

# Mengunggah file
uploaded_file = st.file_uploader("Unggah file CSV", type="csv")

if uploaded_file:
    # Membaca file CSV
    data = pd.read_csv(uploaded_file)
    st.write("Data yang diunggah:")
    st.write(data)

    # Statistik deskriptif
    st.write("Statistik Deskriptif:")
    st.write(data.describe())

    # Visualisasi
    if st.checkbox("Tampilkan histogram"):
        column = st.selectbox("Pilih kolom untuk histogram:", data.columns)
        st.bar_chart(data[column].value_counts())
