import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.preprocessing import StandardScaler


def normalData(cols):
    df = pd.read_csv("../data/clean_data.csv")
    scaler = StandardScaler()
    scaled_array = scaler.fit_transform(df[cols])
    return pd.DataFrame(scaled_array, columns=cols)


def loadExperienceData():
    df = pd.read_csv("../data/clean_data.csv")
    df = df[[
        "msisdn_number",
        "avg_rtt_dl_(ms)",
        "avg_rtt_ul_(ms)",
        "avg_bearer_tp_dl_(kbps)",
        "avg_bearer_tp_ul_(kbps)",
        "tcp_dl_retrans_vol_(bytes)",
        "tcp_ul_retrans_vol_(bytes)",
        "handset_type"]].copy()
    df['total_avg_rtt'] = df['avg_rtt_dl_(ms)'] + \
        df['avg_rtt_ul_(ms)']
    df['total_avg_tp'] = df[
        'avg_bearer_tp_dl_(kbps)'] + df['avg_bearer_tp_ul_(kbps)']
    df['total_avg_tcp'] = df[
        'tcp_dl_retrans_vol_(bytes)'] + df['tcp_ul_retrans_vol_(bytes)']
    df.info()
    return df





def app():
    st.title('Data Distributions')
    cols = ['social_media',
            'google',
            'email',
            'youtube',
            'netflix',
            'gaming',
            'other',
            'total_data']
    df = normalData(cols)
    sample = df.sample(5000)
    sample = np.array(sample[cols]).reshape(8, -1)
    sample[0] = sample[0]-8
    sample[1] = sample[0]-6
    sample[2] = sample[0]-4
    sample[3] = sample[0]-2
    sample[4] = sample[0]-0
    sample[5] = sample[0]-2
    sample[6] = sample[0]-4
    sample[7] = sample[0]-6
    histogram(sample, cols, .1)

    df = loadExperienceData()
    handset_type_df = df.groupby('handset_type').agg(
        {'total_avg_tp': 'mean', 'total_avg_tcp': 'mean'})
    sorted_by_tp = handset_type_df.sort_values(
        'total_avg_tp', ascending=False)
    top_tp = sorted_by_tp['total_avg_tp']
    hist(top_tp)

    hist(top_tp.head(20))

    sorted_by_tcp = handset_type_df.sort_values(
        'total_avg_tcp', ascending=False)

    top_tcp = sorted_by_tcp['total_avg_tcp']
    hist(top_tcp)
    hist(top_tcp.head(20))
