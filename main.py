import streamlit as st
import data_model
import pandas as pd

# Sprawdzenie połączonych
st.write(data_model.df_1.columns)
st.write(data_model.df_2.columns)

st.write(data_model.combined_df.head())
chart_data = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 20, 30, 40]
})
user_input = st.text_input('Enter a text to recognize emotion')
st.write(user_input)

if user_input:
    st.session_state['show_chart'] = True
else:
    st.session_state['show_chart'] = False

if st.session_state.get('show_chart'):
    st.bar_chart(chart_data)
