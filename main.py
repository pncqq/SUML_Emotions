import numpy as np
import streamlit as st
from streamlit import columns
import pandas as pd
from autogluon.multimodal import MultiModalPredictor

model = MultiModalPredictor.load('AutogluonModels/ag-20241112_165247/model.ckpt')

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
    

    