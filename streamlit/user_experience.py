import sys
import os
import sys
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_plot import *
from sklearn.cluster import KMeans

sys.path.insert(1, '../scripts')
from constants import *
from df_outlier import DfOutlier
from df_overview import DfOverview
from df_utils import DfUtils
from df_helper import DfHelper

df_utils = DfUtils()
df_helper = DfHelper()


@st.cache
def loadCleanData():
    df = pd.read_csv("../data/clean_data.csv")
    return df


@st.cache
def getExperienceDataFrame():
    df = loadCleanData()
    user_experience_df = df[[
        "msisdn_number",
        "avg_rtt_dl_(ms)",
        "avg_rtt_ul_(ms)",
        "avg_bearer_tp_dl_(kbps)",
        "avg_bearer_tp_ul_(kbps)",
        "tcp_dl_retrans_vol_(bytes)",
        "tcp_ul_retrans_vol_(bytes)",
        "handset_type"]].copy()
    user_experience_df['total_avg_rtt'] = user_experience_df[
        'avg_rtt_dl_(ms)'] + user_experience_df['avg_rtt_ul_(ms)']
    user_experience_df['total_avg_tp'] = user_experience_df[
        'avg_bearer_tp_dl_(kbps)'] + user_experience_df['avg_bearer_tp_ul_(kbps)']
    user_experience_df['total_avg_tcp'] = user_experience_df[
        'tcp_dl_retrans_vol_(bytes)'] + user_experience_df['tcp_ul_retrans_vol_(bytes)']
    return user_experience_df


@st.cache
def getExperienceData():
    df = getExperienceDataFrame()
    _user_experience = df.groupby('msisdn_number').agg({
        'total_avg_rtt': 'sum',
        'total_avg_tp': 'sum',
        'total_avg_tcp': 'sum',
        'handset_type': [lambda x: x.mode()[0]]})
    user_experience = pd.DataFrame(columns=[
        "total_avg_rtt",
        "total_avg_tp",
        "total_avg_tcp",
        "handset_type"])
    user_experience["total_avg_rtt"] = _user_experience["total_avg_rtt"]['sum']
    user_experience["total_avg_tp"] = _user_experience["total_avg_tp"]['sum']
    user_experience["total_avg_tcp"] = _user_experience["total_avg_tcp"]['sum']
    user_experience["handset_type"] = _user_experience["handset_type"]['<lambda>']
    return user_experience


@st.cache
def getNormalData(df):
    df_outliers = DfOutlier(df)
    cols = ['sessions', 'duration', 'total_data_volume']
    df_outliers.replace_outliers_with_iqr(cols)
    df = df_utils.scale_and_normalize(df_outliers.df, cols)
    return df


@st.cache
def get_distortion_andinertia(df, num):
    distortions, inertias = df_utils.choose_kmeans(df, num)
    return distortions, inertias
    

def plot10(df):
    col = st.selectbox("Compute & list 10 of the top, bottom and most frequent: from", (
        [
            "TCP values",
            "Duration", 
            "Throughput values"
        ]))
    if col == "TCP values":
        sorted_by_tcp = df.sort_values('total_avg_tcp', ascending=False)
        return plot10Sorted(sorted_by_tcp, 'total_avg_tcp')
    elif col == "RTT values":
        sorted_by_rtt = df.sort_values('total_avg_rtt', ascending=False)
        return plot10Sorted(sorted_by_rtt, 'total_avg_rtt')
    else:
        sorted_by_tp = df.sort_values('total_avg_tp', ascending=False)
        return plot10Sorted(sorted_by_tp, 'total_avg_tp')

def plot10Sorted(df, col_name):
    col = st.selectbox("Select from: from", (
        [
            "Top 10",
            "Last 10",
        ]))
    if col == "Top 10":
        _sorted = df.head(10)[col_name]
        return hist(_sorted)

    else:
        _sorted = df.tail(10)[col_name]
        return hist(_sorted)



def app():
    st.title('User Experience Analytics')
    df = getExperienceData()
    plot10(df)


