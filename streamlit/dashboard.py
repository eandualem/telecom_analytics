import clusters
import distribution
import profiling
import streamlit as st
PAGES = {
    "Cluttering": clusters,
    "Distribution": distribution,
    "Telcom Dataframe Profiling": profiling
}
selection = st.sidebar.radio("Go to page", list(PAGES.keys()))
page = PAGES[selection]
page.app()
