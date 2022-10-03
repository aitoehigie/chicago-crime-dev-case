import time
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np


"# Welcome to the Real-Time Chicago Crime Dashboard!"

dataset_url = "http://myapi:8000/chicago_crimes/"

def get_data():
    return pd.read_json(dataset_url)

# Read in the data
df = get_data()
df = pd.DataFrame(get_data(), columns=["latitude", "longitude"])
placeholder = st.map()

with placeholder.container():
    st.map(df)
    