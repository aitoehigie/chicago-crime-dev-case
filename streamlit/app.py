import time
import datetime
import urllib.parse

import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np


DATE_COLUMN = 'date'
BASE_URL = "http://myapi:8000/chicago_crimes/"

st.title("Welcome to the Real-Time Chicago Crime Dashboard!")

# Filter fields
crime_committed_start_date = st.date_input("Start Date", value=pd.to_datetime("2005-01-31 06:00:00+00:00", format='%Y-%m-%dT%H:%M:%S%Z'))
crime_committed_end_date = st.date_input("End Date", value=pd.to_datetime("2021-01-31 06:00:00+00:00", format='%Y-%m-%dT%H:%M:%S%Z'))
crime_committed_type_filter = st.selectbox("Select the Crime Type", ("HOMICIDE", "CRIMINAL SEXUAL ASSAULT",
                                                                     "CRIM SEXUAL ASSAULT", "ROBBERY",
                                                                     "PUBLIC PEACE VIOLATION",
                                                                     "DECEPTIVE PRACTICE", 
                                                                     "BATTERY"))

def generate_url():
    params = {
              "crime_committed_start_date": f"{crime_committed_start_date}",
              "crime_committed_end_date": f"{crime_committed_end_date}",
              "crime_committed_type_filter": f"{crime_committed_type_filter}"
              }
    params = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    return f"{BASE_URL}?{params}"

@st.cache
def load_data():
    return pd.read_json(generate_url())


# format date input
#start = crime_committed_start_date.strftime('%Y-%m-%dT%H:%M:%S%Z')
#end = crime_committed_end_date.strftime('%Y-%m-%dT%H:%M:%S%Z')

# Read in the data
data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done Loading!")

df = pd.DataFrame(data, columns=["latitude", "longitude", "date", "primary_type"])

# Empty map container
placeholder = st.map()

#df = df[df["primary_type"] == crime_committed_type_filter]
#df = df[df["date"] == crime_committed_date_filter]

with placeholder.container():
    st.map(df)
    st.sidebar.title("Filter by Date of Crime/Crime Type")
    st.sidebar.markdown("Select the filters accordingly:")
    