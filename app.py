import streamlit as st

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Housing Project",
    page_icon="🖥️",
    layout="wide"
)

from app_pages.page_model_performance import app as page_model_performance_body
from app_pages.page_prediction import page_prediction_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.page_study import page_study_body
from app_pages.page_summary import page_summary_body


class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

    def app_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()


# Main App
app = MultiPage("Housing Project")

# Add pages
app.app_page("Hypothesis and Validation", page_hypothesis_body)
app.app_page("Model Performance", page_model_performance_body)
app.app_page("House Price Prediction", page_prediction_body)
app.app_page("Study Correlation", page_study_body)
app.app_page("Summary", page_summary_body)

app.run()
