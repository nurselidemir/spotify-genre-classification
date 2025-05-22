# Spotify Genre Classification with Machine Learning

## Akbank Machine Learning Bootcamp

Bu proje, Spotify şarkı verileri üzerinde çok sınıflı bir sınıflandırma problemi çözerek şarkının türünü (genre) tahmin etmeyi amaçlamaktadır. Python, Scikit-learn ve XGBoost gibi kütüphaneler kullanılarak veri analizi, model eğitimi ve değerlendirme aşamaları detaylıca gerçekleştirilmiştir.

## Proje Amacı

Bu projede, Spotify'ın sağladığı çeşitli şarkı özellikleri kullanılarak şarkının ait olduğu müzik türünü tahmin etmek amaçlanmaktadır. Gözetimli öğrenme (supervised learning) yöntemleriyle çoklu sınıf (multiclass) sınıflandırma problemi çözülmektedir.

## Veri Seti

- **Kaynak:** [Kaggle - Spotify Tracks DB](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)
- **Dosya:** SpotifyFeatures.csv

## 🛠️ Veri Ön İşleme

- Gereksiz sütunlar silindi (track_id, artist_name, track_name)
- Nadir sınıflar çıkarıldı
- Kategorik veriler sayısallaştırıldı
- Korelasyon analizine göre filtreleme yapıldı
- Label Encoding, One-hot encoding ve Normalizasyon uygulandı

## Modelleme ve Eğitim

- **Logistic Regression** - Basit ve yorumlanabilir model
- **Random Forest** - Topluluk modeli (ensemble)
- **XGBoost** - En iyi sonucu veren gelişmiş boosting modeli  
*Not:* XGBoost için RandomizedSearchCV ile hiperparametre optimizasyonu yapıldı

## 📈 Model Performansı ve Görselleştirme

Tüm modeller `cross_val_score` ile değerlendirildi ve **accuracy, F1-score** gibi metriklerle karşılaştırıldı.

## Proje Sonuçları ve Yorumlar

Bu projede Spotify şarkı türü sınıflandırması üzerine çalıştım ve üç farklı makine öğrenmesi modeli (Lojistik Regresyon, Random Forest, XGBoost) kullandım. Modellerin performanslarını karşılaştırarak en iyi sonucu veren modeli belirledim.

- **Lojistik Regresyon modeli**, temel bir lineer sınıflandırıcı olarak başlangıç performansı sağladı. Model, doğruluk oranı açısından makul seviyelerde olsa da, karmaşık veri yapısında sınıf farklılıklarını yakalamakta zorlandı.
- **Random Forest**, bir ansamble yöntemi olarak, karar ağaçlarının topluluğu sayesinde daha yüksek doğruluk ve genelleme kabiliyeti gösterdi. Verideki karmaşık ilişkileri daha iyi yakalayarak modelin doğruluğunu artırdı.
- **XGBoost**, gelişmiş gradyan artırma algoritması olarak, hem doğruluk hem de genel model performansı açısından en iyi sonucu verdi. RandomizedSearchCV ile yapılan hiperparametre optimizasyonu, modelin overfitting riskini azaltırken test setinde en yüksek doğruluğa ulaşmasını sağladı.


## Gereksinimler

- Python 3.8+
- pandas, numpy, scikit-learn
- xgboost, seaborn, matplotlib

## Kaggle linkleri

- https://www.kaggle.com/code/nurselidemir/datapreprocessing
- https://www.kaggle.com/code/nurselidemir/supervised
