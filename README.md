 <h1> Spotify Genre Classification with Machine Learning</h1>
 <h2> Akbank Machine Learning Bootcamp</h2>

    <p>Bu proje, Spotify şarkı verileri üzerinde çok sınıflı bir sınıflandırma problemi çözerek şarkının türünü (genre) tahmin etmeyi amaçlamaktadır. Python, Scikit-learn ve XGBoost gibi kütüphaneler kullanılarak veri analizi, model eğitimi ve değerlendirme aşamaları detaylıca gerçekleştirilmiştir.</p>

    <h2> Proje Amacı</h2>
    <p>Bu projede, Spotify'ın sağladığı çeşitli şarkı özellikleri kullanılarak şarkının ait olduğu müzik türünü tahmin etmek amaçlanmaktadır. Gözetimli öğrenme (supervised learning) yöntemleriyle çoklu sınıf (multiclass) sınıflandırma problemi çözülmektedir.</p>

    <h2> Veri Seti</h2>
    <ul>
      <li><strong>Kaynak:</strong> <a href="(https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)">Kaggle - Spotify Tracks DB</a></li>
      <li><strong>Dosya:</strong> SpotifyFeatures.csv</li>
    </ul>

    <h2>🛠️ Veri Ön İşleme</h2>
    <ul>
      <li>Gereksiz sütunlar silindi (track_id, artist_name, track_name)</li>
      <li>Nadir sınıflar çıkarıldı</li>
      <li>Kategorik veriler sayısallaştırıldı</li>
      <li>Korelasyon analizine göre filtreleme yapıldı</li>
      <li>Label Encoding, One-hot encoding ve Normalizasyon uygulandı</li>
    </ul>

    <h2> Modelleme ve Eğitim</h2>
    <ul>
      <li><strong>Logistic Regression</strong> - Basit ve yorumlanabilir model</li>
      <li><strong>Random Forest</strong> - Topluluk modeli (ensemble)</li>
      <li><strong>XGBoost</strong> - En iyi sonucu veren gelişmiş boosting modeli</li>
      <li><em>Not:</em> XGBoost için RandomizedSearchCV ile hiperparametre optimizasyonu yapıldı</li>
    </ul>

    <h2>📈 Model Performansı ve Görselleştirme</h2>
    <p>Tüm modeller <code>cross_val_score</code> ile değerlendirildi ve <strong>accuracy, F1-score</strong> gibi metriklerle karşılaştırıldı.</p>
    <pre><code>

    <h2> Proje Sonuçları ve Yorumlar</h2>
       <ul>
      <p>Bu projede Spotify şarkı türü sınıflandırması üzerine çalıştım ve üç farklı makine öğrenmesi modeli (Lojistik Regresyon, Random Forest, XGBoost) kullandım. Modellerin performanslarını karşılaştırarak en iyi sonucu veren modeli belirledim.</p>
      <li>Lojistik Regresyon modeli, temel bir lineer sınıflandırıcı olarak başlangıç performansı sağladı. Model, doğruluk oranı açısından makul seviyelerde olsa da, karmaşık veri yapısında sınıf farklılıklarını yakalamakta zorlandı.</li>
      <li>
Random Forest, bir ansamble yöntemi olarak, karar ağaçlarının topluluğu sayesinde daha yüksek doğruluk ve genelleme kabiliyeti gösterdi. Verideki karmaşık ilişkileri daha iyi yakalayarak modelin doğruluğunu artırdı.</li>
      <li>XGBoost, gelişmiş gradyan artırma algoritması olarak, hem doğruluk hem de genel model performansı açısından en iyi sonucu verdi. RandomizedSearchCV ile yapılan hiperparametre optimizasyonu, modelin overfitting riskini azaltırken test setinde en yüksek doğruluğa ulaşmasını sağladı.</li>
    </ul>

    

    

    <h2> Nasıl Çalıştırılır</h2>
    <ol>
      <li>Repoyu klonlayın:
        <pre><code>git clone https://github.com/kullaniciadi/spotify-genre-classification.git</code></pre>
      </li>
      <li>Bağımlılıkları yükleyin:
        <pre><code>pip install -r requirements.txt</code></pre>
      </li>
      <li>Notebook'u çalıştırın:
        <pre><code>jupyter notebook genre_classification.ipynb</code></pre>
      </li>
    </ol>

    <h2> Gereksinimler</h2>
    <ul>
      <li>Python 3.8+</li>
      <li>pandas, numpy, scikit-learn</li>
      <li>xgboost, seaborn, matplotlib</li>
      <li>pickle</li>
    </ul>

  
