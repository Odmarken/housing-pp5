import streamlit as st
from app_pages import page_summary, page_hypothesis, page_study, page_prediction, page_model_performance


pages = {
    "Summary": page_summary.app,
    "Hypothesis": page_hypothesis.app,
    "Study": page_study.app,
    "Prediction": page_prediction.app,
    "Model Performance": page_model_performance.app,
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Load the selected page
pages[selection]()
