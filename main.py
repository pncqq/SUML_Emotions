import numpy as np
import streamlit as st
from streamlit import columns
import data_model
import pandas as pd

#data placeholder
chart_data = pd.DataFrame(
    {
        'emotions': ['Sad', 'Angry', 'Faithful', 'Disgusted'],
        'probability': [0.1, 0.2, 0.3, 0.4]
    }
)
st.title("Emotion detection app")
user_input = st.text_input('Enter a text to recognize emotion')

# TODO: Get result from model
# result = data_model.get_result(user_input)
# chart_data = pd.DataFrame({<result>})

output = chart_data.style.format({'probability': "{:.1%}".format})
st.write(user_input)

if user_input:
    st.session_state['show_chart'] = True
else:
    st.session_state['show_chart'] = False

if st.session_state.get('show_chart'):
    st.bar_chart(output, x='emotions', y='probability')
    st.write(output)

