import sys
import os
import sys
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_plot import *


def loadWholeData():
    df = pd.read_csv("../data/clean_data.csv")
    return df


def getEngagemetData():
    df = loadWholeData()
    user_engagement_df = df[['msisdn_number', 'bearer_id', 'dur_(ms)', 'total_data']].copy(
    ).rename(columns={'dur_(ms)': 'duration', 'total_data': 'total_data_volume'})
    return user_engagement_df


def app():
    st.title('User Satisfaction Analysis')
    st.header("Top 10 customers per engagement metrics")
    user_engagement = getEngagemetData()
    sessions = user_engagement.nlargest(10, "sessions")['sessions']
    duration = user_engagement.nlargest(10, "duration")['duration']
    total_data_volume = user_engagement.nlargest(
        10, "total_data_volume")['total_data_volume']
    mult_hist([sessions, duration, total_data_volume], 1,
              3, "User metrix", ['sessions', 'duration', 'total_data_volume'])
