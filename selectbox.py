import numpy as np
import pandas as pd
import streamlit as st

"""
# SELECTBOX
st.selectbox()
"""

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected:  ', option
