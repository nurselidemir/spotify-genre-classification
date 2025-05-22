import streamlit as st
import joblib
import numpy as np

model = joblib.load("classification_model.pkl")

genre_dict = {
    1: "Alternative",
    2: "Anime",
    3: "Blues",
    4: "Children's Music",
    5: "Children's Music",
    6: "Classical",
    7: "Comedy",
    8: "Country",
    9: "Dance",
    10: "Electronic",
    11: "Folk",
    12: "Hip-Hop",
    13: "Indie",
    14: "Jazz",
    15: "Movie",
    16: "Opera",
    17: "Pop",
    18: "R&B",
    19: "Rap",
    20: "Reggae",
    21: "Reggaeton",
    22: "Rock",
    23: "Ska",
    24: "Soul",
    25: "Soundtrack",
    26: "World"
}

st.title("🎵 Spotify Şarkı Türü Tahmini")

st.markdown("## Özellik Açıklamaları")

st.markdown("### Mode Nedir?")
st.write("""
- **Mode**, şarkının majör (1) ya da minör (0) modda olduğunu gösterir.  
- 1 → Major (Majör) — Neşeli, enerjik şarkılar  
- 0 → Minor (Minör) — Daha hüzünlü, duygusal şarkılar  
""")

st.markdown("### Key Nedir?")
key_mapping = {
    0: 'C', 1: 'C#/Db', 2: 'D', 3: 'D#/Eb', 4: 'E', 5: 'F',
    6: 'F#/Gb', 7: 'G', 8: 'G#/Ab', 9: 'A', 10: 'A#/Bb', 11: 'B'
}
st.write("Key, şarkının hangi müzik notasına göre yazıldığını gösterir:")
for code, note in key_mapping.items():
    st.write(f"- {code}: {note}")

st.markdown("### Time Signature Nedir?")
time_sig_mapping = {
    0: " Bu veri geçersiz sayıldı ve temizlendi.",
    1: " Tek vuruşluk ölçü, nadir kullanılır",
    3: " Valslerde ve bazı halk müziklerinde sık görülür",
    4: " En yaygın ölçü, pop ve rock şarkılarında standart",
    5: " Karmaşık ritim, genellikle caz ve progresif türlerde"
}
st.write("Ritim kalıplarının kodları ve anlamları:")
for code, desc in time_sig_mapping.items():
    st.write(f"- {code}: {desc}")

st.markdown("---")
st.markdown("## Şarkı Özellikleri Giriniz")


popularity = st.slider("Popularity (0-1)", 0.0, 1.0, 0.5)
acousticness = st.slider("Acousticness (0-1)", 0.0, 1.0, 0.5)
danceability = st.slider("Danceability (0-1)", 0.0, 1.0, 0.5)
duration_ms = st.slider("Duration (normalized, 0-1)", 0.0, 1.0, 0.5)
energy = st.slider("Energy (0-1)", 0.0, 1.0, 0.5)
instrumentalness = st.slider("Instrumentalness (0-1)", 0.0, 1.0, 0.0)
key = st.slider("Key (0-11)", 0, 11, 5)
liveness = st.slider("Liveness (0-1)", 0.0, 1.0, 0.1)
loudness = st.slider("Loudness (-60 to 0 dB)", -60.0, 0.0, -20.0)
mode = st.selectbox("Mode", [0, 1], format_func=lambda x: "Minor (0)" if x==0 else "Major (1)")
speechiness = st.slider("Speechiness (0-1)", 0.0, 1.0, 0.05)
tempo = st.slider("Tempo (BPM)", 0.0, 250.0, 120.0)
time_signature_0 = st.checkbox("Time Signature 0 (Geçersiz)")
time_signature_1 = st.checkbox("Time Signature 1")
time_signature_3 = st.checkbox("Time Signature 3")
time_signature_4 = st.checkbox("Time Signature 4")
time_signature_5 = st.checkbox("Time Signature 5")
valence = st.slider("Valence (0-1)", 0.0, 1.0, 0.5)

input_data = np.array([[
    popularity, acousticness, danceability, duration_ms, energy,
    instrumentalness, key, liveness, loudness, mode,
    speechiness, tempo, valence,
    time_signature_0, time_signature_1, time_signature_3,
    time_signature_4, time_signature_5
]])

if st.button("Tahmin Et"):
    prediction_number = model.predict(input_data)[0]
    prediction_genre = genre_dict.get(prediction_number, "Bilinmeyen Tür")
    st.success(f"Model Tahmini: {prediction_genre}")
