# ⚡ Enerji Tüketimi Tahmin Sistemi

Bu proje, üretim miktarı, hava sıcaklığı ve hammadde sıcaklığı gibi değişkenleri kullanarak bir üretim tesisindeki **enerji tüketimini tahmin etmek** amacıyla geliştirilmiştir. Proje, makine öğrenmesi modeli ve kullanıcı dostu arayüzüyle enerji yönetimini kolaylaştırmayı hedefler.

## 🎯 Amaç
Sanayi tesislerinde üretim sırasında tüketilen enerjiyi tahmin ederek:
- Enerji verimliliğini artırmak
- Maliyetleri azaltmak
- Sürdürülebilirliğe katkı sağlamak

## 🛠️ Kullanılan Teknolojiler
- Python 🐍
- Streamlit 🎈
- scikit-learn ⚙️
- Pandas & NumPy 📊
- Matplotlib 📉
- Jupyter Notebook 📓

## 📂 Proje Yapısı

```
AI_Energy_Optimization_Project/
│
├── data/                           # Enerji tüketimi veri seti
├── results/                        # Eğitim sonrası kaydedilen modeller
├── notebooks/                     # Jupyter eğitim ve analiz notları
├── src/                            # Yardımcı Python script dosyaları
├── app.py                          # Streamlit uygulama arayüzü
├── model_train.ipynb              # Model eğitimi notebook'u
└── README.md                       # Bu dosya
```

## 🧠 Makine Öğrenmesi Modeli

- Model: En başarılı sonuç veren algoritma seçildi (`RandomForestRegressor` vs `XGBoost` vs `LinearRegression` test edildi)
- Performans: MSE ve R² skorlarına göre optimize edildi
- Veri: Gerçek üretim verilerinden oluşturulmuş örnek set

## 🚀 Uygulama Arayüzü

Kullanıcılar aşağıdaki değişkenleri girerek enerji tüketimi tahmini alabilir:
- Üretim Miktarı (adet)
- Hava Sıcaklığı (°C)
- Hammadde Sıcaklığı (°C)


## 🧪 Nasıl Çalıştırılır?

```bash
# Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# Uygulamayı başlatın
streamlit run app.py
```

## 📈 Örnek Grafik

Enerji tahmini ile birlikte tahmin girdileri aşağıdaki gibi grafikle gösterilir:



## ✨ Katkı ve Geliştirme

Projeyi kendi verilerinizle test etmek isterseniz `data/` klasörüne veri setinizi ekleyin ve `model_train.ipynb` dosyasını çalıştırarak yeni bir model eğitin.
