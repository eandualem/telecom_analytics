import page1
import page2
import streamlit as st
PAGES = {
    "Page 1": page1,
    "Page 2": page2
}
selection = st.sidebar.radio("Go to page", list(PAGES.keys()))
page = PAGES[selection]
page.app()
