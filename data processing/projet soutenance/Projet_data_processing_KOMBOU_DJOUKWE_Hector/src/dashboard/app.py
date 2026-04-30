# dashboard/app.py
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dashboard Météo", layout="wide")

# 📍 Chemin du fichier CSV
CSV_PATH = "meteo.csv"

# ❌ Vérification du fichier
if not os.path.exists(CSV_PATH):
    st.error("❌ Fichier meteo.csv introuvable")
    st.stop()

# 📥 Chargement des données
df = pd.read_csv(CSV_PATH)

# 🧼 Vérification des colonnes
required_cols = ["time", "temperature"]

if not all(col in df.columns for col in required_cols):
    st.error("❌ Colonnes requises : time, temperature")
    st.write("Colonnes disponibles :", df.columns)
    st.stop()

# 📊 Traitement des données
df["time"] = pd.to_datetime(df["time"])
df = df.sort_values("time")

# 📈 Dashboard
st.title("🌤 Dashboard Météo")

st.line_chart(df.set_index("time")["temperature"])