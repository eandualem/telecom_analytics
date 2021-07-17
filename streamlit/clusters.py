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


def loadWholeData():
    df = pd.read_csv("../data/clean_data.csv")
    user_engagement = pd.read_csv("../data/user_engagement.csv")
    return df


def loadEngagementData():
    df = pd.read_csv("../data/user_engagement.csv")
    return df


def loadExperienceData():
    df = pd.read_csv("../data/user_experiance.csv")
    return df

def loadSatisfactionData():
    df = pd.read_csv("../data/user_satisfaction.csv")
    return df


def scatter(df, x, y, c=None, s=None, mx=None, my=None, af=None, fit=None):
    fig = px.scatter(df, x=x, y=y, color=c, size=s, marginal_y=my,
                     marginal_x=mx, trendline=fit, animation_frame=af)
    st.plotly_chart(fig)


def scatter3D(df, x, y, z, c=None, s=None, mx=None, my=None, af=None, fit=None):
    fig = px.scatter_3d(df, x=x, y=y, z=z, color=c, size=s,
                        animation_frame=af, size_max=18)
    st.plotly_chart(fig)


def app():
    st.title('User Experience cluster')
    df = loadEngagementData()
    scatter3D(df, x="total_data_volume",
              y="duration", z="sessions", c="cluster")

    st.title('User Engagement cluster')
    df = loadExperienceData()
    scatter3D(df, x="total_avg_tcp", y="total_avg_rtt", z="total_avg_tp",
              c="cluster")

    st.title('User Satisfaction cluster')
    df = loadSatisfactionData()
    fig = px.scatter(df, x='engagement_score', y="experience_score",
                     color='cluster')
    st.plotly_chart(fig)
