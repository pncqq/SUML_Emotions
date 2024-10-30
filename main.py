import streamlit as st


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



