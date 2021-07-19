import sys
import os
import sys
import pickle
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_plot import *
from sklearn.cluster import KMeans

sys.path.insert(1, '../scripts')
from df_helper import DfHelper
from df_utils import DfUtils
from df_overview import DfOverview
from df_outlier import DfOutlier
from constants import *
from streamlit_plot import *

utils = DfUtils()
helper = DfHelper()

@st.cache
def loadCleanData():
    df = pd.read_csv("../data/clean_data.csv")
    return df


@st.cache
def getEngagemetData():
    df = loadCleanData().copy()
    user_engagement_df = df[['msisdn_number', 'bearer_id', 'dur_(ms)', 'total_data']].copy(
    ).rename(columns={'dur_(ms)': 'duration', 'total_data': 'total_data_volume'})
    user_engagement = user_engagement_df.groupby(
        'msisdn_number').agg({'bearer_id': 'count', 'duration': 'sum', 'total_data_volume': 'sum'})
    user_engagement = user_engagement.rename(
        columns={'bearer_id': 'sessions'})
    return user_engagement


@st.cache
def getNormalData(df):
    res_df = utils.scale_and_normalize(df)
    return res_df


@st.cache
def get_distortion_and_inertia(df, num):
    distortions, inertias = utils.choose_kmeans(df.copy(), num)
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
    distortions, inertias = get_distortion_and_inertia(df, num)
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
    user_engagement = getEngagemetData().copy()
    df_outliers = DfOutlier(user_engagement)
    cols = ['sessions', 'duration', 'total_data_volume']
    df_outliers.replace_outliers_with_iqr(cols)
    user_engagement = df_outliers.df
    plotTop10(user_engagement)

    st.header("Clustering customers based on their engagement metric")
    st.markdown(
        '''
    Here we will try to cluster customers based on their engagement.
    To find optimized value of k first let's plot an elbow curve graph.
    We choose number of clusters by using elbow method. 
    To start choose number max number of clusters to test for.
    ''')
    num = st.selectbox('Select', range(0, 20))
    select_num = 1
    if(num != 0):
        normal_df = getNormalData(user_engagement)
        elbowPlot(normal_df, num+1)

        st.markdown(
            '''
            Select the optimized values for k
        ''')
        select_num = st.selectbox('Select', range(1, num+1))

    if(select_num != 1):

        kmeans = KMeans(n_clusters=select_num, random_state=0).fit(normal_df)
        user_engagement.insert(0, 'cluster', kmeans.labels_)

        st.markdown(
        '''
            Number of elements in each cluster
        ''')
        st.write(user_engagement['cluster'].value_counts())

        st.markdown(
        '''
            2D visualization of cluster
        ''')
        scatter(user_engagement, x='total_data_volume', y="duration",
                c='cluster', s='sessions')

        st.markdown(
        '''
            3D visualization of cluster
        ''')
        scatter3D(user_engagement, x="total_data_volume", y="duration", z="sessions",
                  c="cluster", interactive=True)
        
        st.warning('Remamber cluster with the list engagement. we need that for satisfaction analysis')
        st.markdown(
        '''
            Save the model for satisfaction analysis
        ''')
        if st.button('Save Model'):
            helper.save_csv(user_engagement,
                            '../data/user_engagement.csv', index=True)

            with open("../models/user_engagement.pkl", "wb") as f:
                pickle.dump(kmeans, f)
