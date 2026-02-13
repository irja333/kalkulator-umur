import streamlit as st
from datetime import date
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="Modern Age Calculator", page_icon="📅", layout="centered")

# Custom CSS untuk tampilan lebih modern
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
    }
    .age-card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📅 Kalkulator Umur Modern")
st.write("Masukkan tanggal lahirmu untuk melihat detail usia secara presisi.")

# Input Tanggal Lahir
today = date.today()
birth_date = st.date_input("Pilih Tanggal Lahir", 
                          value=date(2000, 1, 1),
                          max_value=today)

if st.button("Hitung Usia Sekarang"):
    # Logika Perhitungan
    age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    # Menghitung total hari
    delta = today - birth_date
    total_days = delta.days
    
    # Layout Kolom untuk Statistik
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Tahun", f"{age_years}")
    with col2:
        st.metric("Bulan", f"{age_years * 12}")
    with col3:
        st.metric("Total Hari", f"{total_days:,}")

    st.markdown("---")
    
    # Detail tambahan
    st.subheader("Detail Perjalanan Hidupmu 🚀")
    
    data = {
        "Satuan Waktu": ["Minggu", "Jam", "Menit"],
        "Jumlah": [f"{total_days // 7:,}", f"{total_days * 24:,}", f"{total_days * 24 * 60:,}"]
    }
    df = pd.DataFrame(data)
    st.table(df)

    # Progress Bar menuju ulang tahun berikutnya
    next_birthday = date(today.year, birth_date.month, birth_date.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    
    days_to_go = (next_birthday - today).days
    progress = (365 - days_to_go) / 365
    
    st.write(f"**{days_to_go} hari lagi** menuju ulang tahunmu berikutnya! 🎉")
    st.progress(progress)
    
    st.balloons()
