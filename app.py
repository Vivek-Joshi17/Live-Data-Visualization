import streamlit as st # type: ignore
import numpy as np
import pandas as pd
import time #to simulate a real time data 
import plotly.express as px # type: ignore

df =  pd.pd.read_csv("bank.csv")

st.set_page_config( 
    page_title='Real time Data Science Dashboard',
    page_icon='Red',
    layout="wide"
)

st.title('Real-Time/Live Data Science Dashboard')

job_filter = st.selectbox("Select the Job",pd.unique(df['job']))

