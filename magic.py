import pandas as pd
import streamlit as st

"""
# Use Magic
Any time Streamlit sees a variable or a literal value on its own line, it automatically writes that to your app using st.write().
"""

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df