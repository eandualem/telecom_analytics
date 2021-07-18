import overview
import user_engagement
import user_experience
import user_satisfaction
import streamlit as st

PAGES = {
    "Data Overview": overview,
    "User Engagement Analysis":  user_engagement,
    "User Experience Analytics": user_experience,
    "User Satisfaction Analysis": user_satisfaction,
}

selection = st.sidebar.radio("Go to page", list(PAGES.keys()))
page = PAGES[selection]
page.app()
