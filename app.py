import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Ubah warna latar belakang menjadi hitam
st.markdown(
"""
<style>
body {
    background-color: #000000;
}
h1, h2, h3, h4, h5, h6 {
    color: #FFFFFF;
}
</style>
""",
unsafe_allow_html=True)

model = pickle.load(open('prediksi_co2.sav','rb'))

df = pd.read_excel("CO2 dataset.xlsx")
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index(['Year'], inplace=True)

st.title('Forecasting Kualitas Udara Project Mastering Digital Transformation')
year = st.slider("Tentukan Tahun", 1, 30, step=1)

pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=['CO2'])

if st.button("Predict"):

    col1, col2 = st.columns([2, 3])
    with col1:
        st.subheader("Hasil Prediksi:")
        st.dataframe(pred.style.format("{:.2f}").highlight_min(axis=0, color='lightgreen').highlight_max(axis=0, color='#FF6347'))

    with col2:
        fig, ax = plt.subplots()
        df['CO2'].plot(style='--', color='gray', legend=True, label='known')
        pred['CO2'].plot(color='b', legend=True, label='Prediction')
        st.pyplot(fig)
