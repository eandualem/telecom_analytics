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
def getEngagemetData():
    df = loadCleanData()
    user_engagement_df = df[['msisdn_number', 'bearer_id', 'dur_(ms)', 'total_data']].copy(
    ).rename(columns={'dur_(ms)': 'duration', 'total_data': 'total_data_volume'})
    user_engagement = user_engagement_df.groupby(
        'msisdn_number').agg({'bearer_id': 'count', 'duration': 'sum', 'total_data_volume': 'sum'})
    user_engagement = user_engagement.rename(
        columns={'bearer_id': 'sessions'})
    return user_engagement


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

def plotTop10(df):
    col = st.sidebar.selectbox(
        "Select top 10 from", (["Sessions", "Duration", "Total data volume"]))
    if col == "Sessions":
        sessions = df.nlargest(10, "sessions")['sessions']
        return hist(sessions)
    elif col == "Duration":
        duration = df.nlargest(10, "duration")['duration']
        return hist(duration)
    else:
        total_data_volume = df.nlargest(
            10, "total_data_volume")['total_data_volume']
        return hist(total_data_volume)


def elbowPlot(df, num):
    distortions, inertias = get_distortion_andinertia(df, num)
    fig = make_subplots(
        rows=1, cols=2, subplot_titles=("Distortion", "Inertia")
    )
    fig.add_trace(go.Scatter(x=np.array(range(1, num)),
                y=distortions), row=1, col=1)
    fig.add_trace(go.Scatter(x=np.array(
        range(1, num)), y=inertias), row=1, col=2)
    fig.update_layout(title_text="The Elbow Method")
    st.plotly_chart(fig)


def app():
    st.title('User Engagement analysis')
    st.header("Top 10 customers per engagement metrics")
    user_engagement = getEngagemetData()
    plotTop10(user_engagement)
    
    st.header("Clustering customers based on their engagement")
    st.markdown(
    '''
    Here we will try to cluster customers based on their engagement.
    We choose number of clusters by using elbow method. 
    To start choose number of tries
    ''')
    num = st.selectbox('Select', range(0, 20))
    select_num = 1
    if(num != 0):
        normal_df = getNormalData(user_engagement)
        elbowPlot(normal_df, num)

        select_num = st.selectbox('Select', range(1, num))

    if(select_num != 1):
        st.markdown(
        '''
        Based on the image above choose number of clusters
        ''')
        kmeans = KMeans(n_clusters=select_num, random_state=0).fit(normal_df)
        user_engagement["cluster"]= kmeans.labels_
        user_engagement
        scatter3D(user_engagement, y="total_data_volume", x="duration", z="sessions",
                c="cluster", interactive=True, rotation=[-1.5, -1.5, 1])

        st.markdown(
        '''
        Save the cluster for satisfaction analysis
        ''')
        if st.button('Save CSV'):
            df_helper.save_csv(user_engagement, '../data/', 'test.csv')
