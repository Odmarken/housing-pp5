import streamlit as st
import pandas as pd
from src.data_management import housing_data, load_pkl_file, inherited_house_data
from src.machine_learning.prediction_analysis import predict_sale_price


def page_prediction_body():
    # Load model and data
    pipeline = load_pkl_file("outputs/ml_pipeline/predict_SalePrice/v1/pipeline.pkl")
    sale_price_features = (pd.read_csv("outputs/ml_pipeline/predict_SalePrice/v1/X_train.csv").columns.to_list())

    st.write("## House Price Prediction")
    st.subheader("Business Requirement 2")
    st.write(
        "2.1 The client is interested to predict the sale price for her 4 "
        "inherited houses.\n\n"
        "2.2 As well as any other house in Ames, Iowa."
    )

    # Predict prices for inherited houses
    in_df = inherited_house_data()
    features = ['GarageArea', 'GrLivArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt']

    for i, house in enumerate(in_df.iterrows(), start=1):
        st.write(f"### House {i} Attributes")
        st.code(house[1][features])
        predict_sale_price(house[1:2], features, pipeline)

    # Real-time prediction
    st.write("---")
    st.subheader("Predict Housing Sale Prices")
    X_live = DrawInputsWidgets()

    if st.button('Predict Sale Price'):
        st.write("**The Predicted Sale Price:**")
        predict_sale_price(X_live, sale_price_features, pipeline)


def DrawInputsWidgets():
    df = housing_data()

    # Create widgets for input
    col1, col2 = st.columns(2)
    col3, col4, col5 = st.columns(3)

    X_live = pd.DataFrame([], index=[0])  # Live data input

    with col1:
        X_live["OverallQual"] = st.number_input("Overall Quality (1-10)", 1, 10, step=1)
    with col2:
        X_live["GrLivArea"] = st.number_input("Above grade living area (sqft)", 334, 5642, step=10)
    with col3:
        X_live["TotalBsmtSF"] = st.number_input("Total basement area (sqft)", 0, 6110, step=10)
    with col4:
        X_live["GarageArea"] = st.number_input("Garage area (sqft)", 0, 1418, step=10)
    with col5:
        X_live["YearBuilt"] = st.number_input("Year Built (1872-2010)", 1872, 2010, step=1)

    return X_live
