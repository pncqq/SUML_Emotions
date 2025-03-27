# 😍 SUML_Emotions

Aplikacja do analizy emocji w tekstach z wykorzystaniem uczenia maszynowego i AutoML. Projekt zrealizowany zespołowo w ramach kursu SUML.

## 📂 Zawartość repozytorium

- `main.py` – główny plik uruchamiający aplikację (Streamlit)
- `data_model.ipynb` – eksploracja danych i trenowanie modelu
- `requirements.txt` – zależności do uruchomienia projektu
- `README.md` – dokumentacja

## 🚀 Link do aplikacji (demo)

👉 [https://detectheremotion.streamlit.app](https://detectheremotion.streamlit.app)

## 📈 Zbiory danych

1. Empathetic Dialogues v2 (Hugging Face):  
   https://huggingface.co/datasets/Adapting/empathetic_dialogues_v2

2. SetFit Emotion Dataset:  
   https://huggingface.co/datasets/SetFit/emotion

## ⚙️ Technologie

- Python 3.x
- Streamlit
- scikit-learn
- AutoML (AutoGluon / TPOT – zależnie od wersji)
- Jupyter Notebook

## 🧠 Funkcjonalności aplikacji

- Wprowadzanie tekstu przez użytkownika
- Predykcja emocji (np. joy, sadness, anger, etc.)
- Możliwość rozszerzenia na chatboty, wsparcie emocjonalne lub psychologiczne

## 📅 Cel projektu

Celem projektu było stworzenie narzędzia wykorzystującego modele ML do rozpoznawania emocji w komunikatach tekstowych. Potencjalne zastosowania to:
- pomoc dla osób neuroatypowych w interpretacji emocji
- wsparcie chatbotów w lepszym dopasowaniu odpowiedzi
- aplikacje psychologiczne lub terapeutyczne

## ▶️ Jak uruchomić lokalnie

1. Sklonuj repo:
```bash
git clone https://github.com/pncqq/SUML_Emotions.git
cd SUML_Emotions
```

2. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

3. Uruchom aplikację Streamlit:
```bash
streamlit run main.py
```

## 👨‍💼 Zespół i autorstwo

- Filip Michalski – kod aplikacji, trenowanie modelu
- Filip Chrzanowski – deploy aplikacji, streamlit
- Szymon Kaliński – dokumentacja, prezentacja, oprawa graficzna

Projekt wykonany w ramach kursu **SUML – Systemy Uczące się Maszynowo**.
