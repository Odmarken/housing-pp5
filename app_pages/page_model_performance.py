import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file
from src.machine_learning.model_evaluation import regression_performance

def app():
    st.write("### Model Performance")
    pipeline = load_pkl_file("outputs/ml_pipeline/predict_SalePrice/v1/pipeline.pkl")
    X_train = pd.read_csv("outputs/ml_pipeline/predict_SalePrice/v1/X_train.csv")
    y_train = pd.read_csv("outputs/ml_pipeline/predict_SalePrice/v1/y_train.csv")
    X_test = pd.read_csv("outputs/ml_pipeline/predict_SalePrice/v1/X_test.csv")
    y_test = pd.read_csv("outputs/ml_pipeline/predict_SalePrice/v1/y_test.csv")

    regression_performance(X_train, y_train, X_test, y_test, pipeline)
