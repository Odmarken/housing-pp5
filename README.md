# Housing Price Prediction

This is a Machine Learning project designed to predict house prices in Ames, Iowa, using a dataset containing various features about the houses.

* The App live link is: [Housing Price Prediction](https://housingpp5-d4abd052a83c.herokuapp.com)

---

## Business Case

You are tasked with helping a real estate agency optimize their property pricing in Ames, Iowa. The agency has provided a dataset containing detailed house attributes and their corresponding sale prices. They aim to:

1. Identify key features that influence house prices.
2. Predict sale prices for their listed properties accurately.

With this solution, the agency will enhance its pricing strategy, ensuring competitiveness and maximizing profits.

---

## Dataset Content

The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). It contains housing records from Ames, Iowa, providing detailed information about houses, including their size, quality, and additional features, along with their sale prices.

| Variable        | Meaning                                                 | Units        |
|:----------------|:--------------------------------------------------------|:------------:|
| 1stFlrSF        | First Floor square feet                                 | 334 - 4692   |
| GrLivArea       | Above grade (ground) living area square feet            | 334 - 5642   |
| OverallQual     | Rates the overall material and finish of the house      | 1 - 10       |
| GarageArea      | Size of garage in square feet                           | 0 - 1418     |
| YearBuilt       | Original construction date                              | 1872 - 2010  |
| SalePrice       | Sale Price                                              | 34900 - 755000 |

---

## Hypothesis and Validation

**Hypothesis:**

Certain factors significantly influence house prices, including:

- The overall quality and finish of the house.
- The total square footage and layout.
- The condition and size of essential areas like kitchens and garages.
- The construction year, as newer homes often command higher prices.

**Validation:**

Correlation studies and data visualizations will be used to validate these hypotheses. We will also analyze model performance metrics to assess prediction accuracy.

---

## Requirements Mapping

**Business Requirement 1:**  
- Explore correlations between house features and sale prices using visualizations.
- Summarize insights from high-correlation variables.

**Business Requirement 2:**  
- Build a machine learning model to predict house prices with a target accuracy of at least 75%.

---

## Machine Learning Workflow

1. **Data Preprocessing:** Clean, transform, and encode the data for modeling.
2. **Model Training:** Train a pipeline using algorithms like Random Forest.
3. **Validation:** Test the model's performance and fine-tune as necessary.
4. **Deployment:** Deploy the model on an interactive dashboard.

---

## Dashboard Features

1. **Project Summary:**  
   Overview of the dataset and project objectives.

2. **Correlation Insights:**  
   Visualizations highlighting the strongest correlations with house prices.

3. **Prediction Page:**  
   - Predict prices for specific houses.
   - Interactive input widgets for real-time predictions.

4. **Model Performance Page:**  
   - Details on pipeline steps.
   - Feature importance and performance metrics.

---

## Libraries Used

- **Pandas:** Data manipulation and analysis.
- **Matplotlib & Seaborn:** Data visualization.
- **Scikit-learn:** Machine learning pipeline and model training.
- **Streamlit:** Building the interactive dashboard.

---

## Deployment

The app is deployed on Heroku using the following steps:

1. Log in to Heroku and create an app.
2. Connect your GitHub repository.
3. Deploy the branch containing your project code.
4. Open the deployed app using the Heroku interface.

---

## Acknowledgments

- Special thanks to the CI community 
- Huge thanks to Riman with her I would not have made it! link to her project (https://github.com/rimanfarhood/HeritageHousePrediction)
- This was probably the hardest project yet to grasp and understand
- It was hard to get help since I couldn’t access a tutor for this project; I could only use Slack and my mentor, which felt underwhelming, making the process extremely challenging.


