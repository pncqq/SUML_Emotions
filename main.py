import pandas as pd
import streamlit as st
import numpy as np

# Przygotowanie danych
splits_1 = {'train': 'train.csv', 'validation': 'dev.csv', 'test': 'test.csv'}
df_1 = pd.read_csv("hf://datasets/Adapting/empathetic_dialogues_v2/" + splits_1["train"])

splits_2 = {'train': 'train.jsonl', 'validation': 'validation.jsonl', 'test': 'test.jsonl'}
df_2 = pd.read_json("hf://datasets/SetFit/emotion/" + splits_2["train"], lines=True)

df_1.drop(columns=['id', 'chat_history', 'sys_response', 'question or not', 'behavior'], inplace=True)
df_2.drop(columns=['label'], inplace=True)

df_1.rename(columns={'situation': 'text'}, inplace=True)
df_2.rename(columns={'label_text': 'emotion'}, inplace=True)

st.write(df_1.columns)
st.write(df_2.columns)

combined_df = pd.concat([df_1, df_2])

# Sprawdzenie połączonych
st.write(combined_df.head())
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



