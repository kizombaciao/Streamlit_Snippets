import pandas as pd
import streamlit as st

add_selectbox = st.sidebar.selectbox(
    'How would you be like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first column']
)
'You selected:  ', option

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)