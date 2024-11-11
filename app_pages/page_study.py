import streamlit as st
import matplotlib.pyplot as plt
from src.data_management import housing_data


def page_study_body():
    # Load data
    df = housing_data()

    # Display dataset metadata
    st.write("## Sale Price Correlation Study")
    st.write(
        "The client is interested in understanding how house attributes correlate with sale prices. This page visualizes the most relevant variables."
    )

    if st.checkbox("Inspect Dataset"):
        st.write(f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
        st.write(df.head())

    # Correlation visualizations
    st.write("### Correlation Plots")
    spearman = plt.imread("outputs/study_plots/spearman.png")
    pearson = plt.imread("outputs/study_plots/pearson.png")

    st.image(spearman, caption="Spearman Correlation")
    st.image(pearson, caption="Pearson Correlation")

    # Positive and negative correlation studies
    st.write("---")
    st.write("**Positive Correlations:** Attributes like 'Overall Quality' and 'GrLivArea' increase sale price.")
    st.write("**Negative Correlations:** Attributes like 'KitchenQual_TA' reduce sale price.")
