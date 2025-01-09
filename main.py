import os
import pandas as pd
import requests
import streamlit as st
import zipfile
from autogluon.multimodal import MultiModalPredictor

zip_url = 'https://huggingface.co/pncqq/emotion_predictor/resolve/main/ag-20241112_165247.zip'
zip_local  = "ag-20241112_165247.zip"
target_dir = "AutogluonModels/ag-20241112_165247"

if not os.path.exists(target_dir):
    # os.makedirs(os.path.dirname(local_path), exist_ok=True)
    print("Downloading model...")
    r = requests.get(zip_url, stream=True)
    with open(zip_local, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

    with zipfile.ZipFile(zip_local, 'r') as zip_ref:
        zip_ref.extractall("AutogluonModels")
    print("Download complete.")

model = MultiModalPredictor.load(target_dir)

st.title("Emotion detection app")
user_input = st.text_input('Enter a text to recognize emotion')

if user_input:
    st.session_state['input_received'] = True
else:
    st.session_state['input_received'] = False

if st.session_state.get('input_received'):
    dt_frame = pd.DataFrame({'text': [user_input]})
    st.write("Input received.")
    with st.spinner("Detecting emotion..."):
        prediction = model.predict(dt_frame[['text']])
        st.write("Prediction: ", prediction.iloc[0].upper())
    

