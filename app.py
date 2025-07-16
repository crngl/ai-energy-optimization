import streamlit as st
import pandas as pd
import joblib

# Modeli yükle
model = joblib.load("results/best_model.pkl")

# Başlık
st.title("🔋 Enerji Tüketimi Tahmini")

# Girdi alanları
uretim = st.number_input("Üretim Miktarı (adet)", min_value=0, step=1)
hava = st.number_input("Hava Sıcaklığı (°C)", format="%.2f")
hammadde = st.number_input("Hammadde Sıcaklığı (°C)", format="%.2f")

# Tahmin butonu
if st.button("Tahmin Et"):
    # Tahmin yap
    tahmin = model.predict([[uretim, hava, hammadde]])
    
    # Tahmin sonucunu göster
    st.success(f"Tahmin Edilen Enerji Tüketimi: {tahmin[0]:.2f} kWh")

    # Görselleştirme verisi oluştur
    veri = {
        "Üretim (adet)": uretim,
        "Hava Sıcaklığı (°C)": hava,
        "Hammadde Sıcaklığı (°C)": hammadde,
        "Tahmini Enerji Tüketimi (kWh)": tahmin[0]
    }

    df_gorsel = pd.DataFrame.from_dict(veri, orient="index", columns=["Değer"])

    # Bar chart çizdir
    st.subheader("📊 Tahmin ve Girdiler")
    st.bar_chart(df_gorsel)
