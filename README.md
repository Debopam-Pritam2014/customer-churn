# Bank Churn Prediction using MLflow and Flask

This project is an end-to-end machine learning system for predicting bank customer churn based on a set of key features such as age, tenure, active membership, and credit score. It uses a pipeline for data ingestion, validation, transformation, model training, and evaluation. The model is deployed via a Flask web application that allows for real-time predictions.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Evaluation](#model-evaluation)

## Project Overview
This system predicts whether a customer will churn based on various features like:
- Age
- Tenure
- IsActiveMember status
- Gender
- Geography
- CreditScore
- NumOfProducts

The dataset is highly imbalanced, so **SMOTE** (Synthetic Minority Over-sampling Technique) was applied to handle the imbalance. Multiple machine learning algorithms were tested, and **Gradient Boosting Classifier** was found to be the best-performing model based on accuracy, precision, recall, and F1-score.

The project is structured as a modular pipeline and includes data ingestion, validation, feature engineering, model training, and evaluation.

## Features
- **Data Ingestion**: Handles reading and loading data for training and testing.
- **Data Validation**: Ensures data quality and consistency.
- **Data Transformation**: Preprocessing and feature engineering using techniques like scaling, encoding, etc.
- **Model Training**: A range of models are tested, and Gradient Boosting Classifier is used for final predictions.
- **Model Evaluation**: Metrics like accuracy, precision, recall, and F1-score are calculated.
- **Flask Web App**: Provides two URLs: one for the default route and another for making predictions.

## Technologies Used
- **Python** (for building the pipeline and machine learning models)
- **Flask** (for deploying the model as a web app)
- **MLflow** (for tracking model metrics and artifacts)
- **Pandas** (for data manipulation)
- **Scikit-learn** (for model building and evaluation)
- **SMOTE** (for handling imbalanced data)
- **Conda** (for environment management)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Debopam-Pritam2014/customer-churn.git
    cd customer-churn
    ```

2. Create and activate the Conda environment:
    ```bash
    conda create --name churn_prediction python=3.10
    conda activate churn_prediction
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Run the Flask app:
    ```bash
    python app.py
    ```

2. The app will start on `http://127.0.0.1:5000/`.

### Flask URLs:
- **Default route** (`/`): For testing the app.
- **Prediction route** (`/predict`): Accepts input features for making predictions.

## Usage

Once the application is running, you can access the following:

- Default route: `http://127.0.0.1:5000/`
- Prediction route: `http://127.0.0.1:5000/predict`

You can use the `/predict` route to input features like `age`, `tenure`, `creditscore`, etc., and get back whether the customer is predicted to churn or not.

## Project Structure
├── app.py                # Flask application
├── setup.py              # Setup file for the project
├── requirements.txt      # Project dependencies
├── artifacts/            # Folder for storing models, preprocessor, and data
│   ├── model.pkl         # Trained model
│   ├── preprocessor.pkl  # Data preprocessor
│   ├── train.csv         # Training data
│   └── test.csv          # Test data
├── experiments/          # Jupyter notebooks for EDA and experiments
├── src/ 
│   ├── components/       # ingestion, validation transformation, etc.
│   ├── pipeline/         # Pipeline training and prediction
              
└── README.md             # Project documentation
└── main.py               # Testing training pipeline

## Model Evaluation
The model was evaluated using various metrics:
- **Accuracy**  : 86%
- **Precision** : 66%
- **Recall**    : 62%
- **F1-score**  : 60%

The Gradient Boosting Classifier was found to be the best-performing model for predicting churn.
