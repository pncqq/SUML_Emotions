import os
import pandas as pd
import requests
import streamlit as st
from autogluon.multimodal import MultiModalPredictor

url = 'https://huggingface.co/pncqq/ag_emotion_predictor/blob/main/ag-20241112_165247/model.ckpt'
local_path = "AutogluonModels/ag-20241112_165247/model.ckpt"

if not os.path.exists(local_path):
    print("Downloading model...")
    r = requests.get(url, stream=True)
    with open(local_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Download complete.")

model = MultiModalPredictor.load(local_path)

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
    

    