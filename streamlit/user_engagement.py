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
from streamlit_pandas_profiling import st_profile_report


def loadCleanData():
    df = pd.read_excel("../data/field_descriptions.xlsx")
    return df

def loadEngagementData():
    df = pd.read_excel("../data/field_descriptions.xlsx")
    return df


def app():
    st.title('User Engagement analysis')
    df = loadWholeData()
