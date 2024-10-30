import numpy as np
import pandas as pd

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
