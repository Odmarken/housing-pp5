import streamlit as st
from app_pages.multipage import MultiPage  # Import your multipage module
from app_pages import (
    page_summary,
    page_hypothesis,
    page_study,
    page_prediction,
    page_model_performance
)

# Initialize the app
app = MultiPage()

# Add all pages
app.add_page("Summary", page_summary.app)
app.add_page("Hypothesis", page_hypothesis.app)
app.add_page("Study", page_study.app)
app.add_page("Prediction", page_prediction.app)
app.add_page("Model Performance", page_model_performance.app)

# Run the app
app.run()
