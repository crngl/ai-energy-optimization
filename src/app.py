import streamlit as st
import pandas as pd
import joblib

# Başlık ve açıklama
st.title("🔋 AI Tabanlı Enerji Tüketimi Tahmin Aracı")
st.markdown("""
Bu uygulama, üretim verilerinize göre tahmini enerji tüketimini hesaplamak için Random Forest modelini kullanır.
Lütfen aşağıdaki bilgileri girin ve tahmini görün.
""")

# Modeli yükle
model = joblib.load("results/best_model.pkl")

# Kullanıcıdan giriş verisi al
st.subheader("📥 Girdi Verileri")

uretim = st.number_input("Üretim Miktarı (adet)", min_value=0)
hava = st.slider("Hava Sıcaklığı (°C)", min_value=-20.0, max_value=50.0, step=0.5)
hammadde = st.slider("Hammadde Sıcaklığı (°C)", min_value=0.0, max_value=200.0, step=0.5)

# Tahmin butonu
if st.button("⚡ Enerji Tüketimini Tahmin Et"):
    veri = pd.DataFrame([[uretim, hava, hammadde]],
                        columns=["Üretim_Miktarı_adet", "Hava_Sıcaklığı_C", "Hammadde_Sıcaklığı_C"])
    tahmin = model.predict(veri)
    st.success(f"🔮 Tahmin Edilen Enerji Tüketimi: {tahmin[0]:.2f} kWh")
