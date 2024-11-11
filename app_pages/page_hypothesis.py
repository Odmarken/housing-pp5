import streamlit as st


def page_hypothesis_body():
    st.write("### Hypothesis and Validation")
    st.write(
        "After researching the field of real estate and based on prior knowledge, here is the hypothesis."
    )
    st.write(
        "- **YearBuilt**: Original construction date\n"
        "- **TotalBsmtSF**: Total square feet of basement area\n"
        "- **GrLivArea**: Above grade (ground) living area square feet\n"
        "- **OverallQual**: Rates the overall material and finish of the house\n"
        "- **KitchenQual**: Kitchen quality\n"
    )
    st.write("---")

    st.write("**Hypothesis**")
    st.write(
        "The following factors are hypothesized to have the greatest impact on the sale price:\n"
        "- Overall quality\n"
        "- Size of the house\n"
        "- Number of bedrooms and bathrooms\n"
        "- Kitchen and bathroom conditions\n"
        "- Year built\n"
    )
    st.write("---")

    st.write("**Validation**")
    st.write(
        "We validate the hypothesis through a Correlation Study, confirming that overall quality, size, and year built are strongly correlated with sale price."
    )
