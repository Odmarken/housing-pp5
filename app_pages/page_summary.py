import streamlit as st


def page_summary_body():
    st.write("## Project Summary")

    # Business Requirements
    st.subheader("Business Requirements")
    st.write(
        "- **Requirement 1**: The client is interested in discovering how house attributes correlate with sale prices.\n"
        "- **Requirement 2**: The client expects a machine learning model capable of predicting sale prices for houses with at least 75% accuracy."
    )
    st.write("---")

    # Metadata and Dataset Summary
    st.subheader("Dataset Metadata")
    st.write(
        "- **1stFlrSF**: First floor square feet\n"
        "- **GrLivArea**: Above grade living area square feet\n"
        "- **GarageYrBlt**: Year garage was built\n"
        "- **TotalBsmtSF**: Total basement area\n"
        "- **GarageArea**: Garage area in square feet\n"
        "- **YearBuilt**: Original construction date\n"
    )

    if st.checkbox("View Full Metadata"):
        st.write(
            "- **OverallQual**: Overall material and finish quality\n"
            "- **KitchenQual**: Kitchen quality\n"
            "- **LotArea**: Lot size in square feet\n"
            "- **MasVnrArea**: Masonry veneer area in square feet\n"
        )

    # Link to README
    st.write("---")
    st.write(
        "For additional information, refer to the [Project README](https://github.com/Odmarken/housing-pp5)."
    )
