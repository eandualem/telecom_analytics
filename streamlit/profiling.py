import sys
import os
import sys
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report


def loadWholeData():
    df = pd.read_csv("../data/clean_data.csv")
    df = df[["msisdn_number",
             "handset_manufacturer",
             "bearer_id",
             "dur_(ms)",
             'social_media',
             'google',
             'email',
             'youtube',
             'netflix',
             'gaming',
             'other',
             'total_data']]
    return df

def app():
    st.title('Telcom Analytics Profiling')
    df = loadWholeData()
    pr = df.profile_report()
    st_profile_report(pr)
