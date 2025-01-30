import streamlit as st
import pandas as pd
import pygal
from pygal.style import LightColorizedStyle
from streamlit.components.v1 import html
import plotly.express as px

# ---- Konfigurasi Streamlit ----
st.set_page_config(page_title="Visualisasi Data", layout="wide")

# ---- Header ----
st.title("📊 Visualisasi Data dengan Pygal dan Plotly")
st.markdown("Gunakan aplikasi ini untuk mengeksplorasi dataset yang telah dibersihkan.")

# ---- Upload Data ----
uploaded_file = st.file_uploader("Unggah dataset CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset berhasil dimuat!")
else:
    st.warning("Silakan unggah file CSV untuk melanjutkan.")
    st.stop()

# ---- Tampilkan Data ----
st.subheader("🔍 Preview Data")
st.write(df.head())

# ---- Pilih Kolom untuk Visualisasi ----
num_columns = df.select_dtypes(include=['number']).columns
if len(num_columns) == 0:
    st.error("Tidak ada kolom numerik dalam dataset.")
    st.stop()

selected_column = st.selectbox("Pilih kolom numerik untuk visualisasi", num_columns)

# ---- VISUALISASI PYGAL ----
st.subheader("📈 Visualisasi dengan Pygal")

# Buat grafik batang
bar_chart = pygal.Bar(style=LightColorizedStyle, show_legend=False)
bar_chart.title = f"Distribusi Data: {selected_column}"

for index, value in enumerate(df[selected_column][:10]):  # Ambil 10 data pertama
    bar_chart.add(f"Data {index+1}", value)

# Render Pygal ke HTML
chart_html = bar_chart.render_data_uri()
html(f'<embed type="image/svg+xml" src="{chart_html}" width="700" height="500" />', height=600)

# ---- VISUALISASI PLOTLY ----
st.subheader("⚡ Visualisasi dengan Plotly")

fig = px.scatter(df, x=selected_column, y=selected_column, title="Scatter Plot dengan Plotly")
st.plotly_chart(fig)

# ---- Penutup ----
st.markdown("🚀 **Aplikasi ini menggunakan Pygal & Plotly untuk analisis data interaktif!**")
