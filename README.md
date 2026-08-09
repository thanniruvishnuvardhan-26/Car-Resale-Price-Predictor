# 🚗 Car Resale Price Predictor

A Machine Learning based web application that predicts the resale price of used cars.

The project provides two prediction modes:

- **Basic Prediction** – uses essential car information.
- **Advanced Prediction** – additionally uses the original purchase price.

The trained ML pipelines are deployed through a Flask web application with an HTML/CSS/JavaScript frontend.

---

## 📌 Project Overview

Buying or selling a used car can make it difficult to determine a reasonable resale price.

This project attempts to estimate the resale value of a car using information such as:

- Manufacture year
- Fuel type
- Kilometers driven
- City
- Body type
- Transmission
- Car brand
- Car model
- Number of owners
- Original purchase price (Advanced mode)

The project was developed through multiple experiments involving data cleaning, feature investigation, model comparison, preprocessing pipelines, and web deployment.

---

# 🎯 Features

## 🟦 Basic Prediction

The Basic model uses:

- Manufacture year
- Fuel type
- Kilometers driven
- City
- Body type
- Transmission
- Car brand
- Car model
- Number of owners

Validation R²:

**≈ 0.84**

---

## 🟩 Advanced Prediction

The Advanced model uses all Basic features plus:

- Original purchase price

Validation R²:

**≈ 0.98**

The Advanced model performed better on the evaluation data used during development.

> R² is used as the evaluation metric here. It should not be interpreted as classification accuracy.

---

# 🧠 Machine Learning Workflow

The project followed this workflow:

Dataset
↓
Data exploration
↓
Data cleaning
↓
Missing-value handling
↓
Invalid-value investigation
↓
Outlier investigation
↓
Feature selection
↓
Categorical encoding
↓
Train/Test split
↓
ML Pipeline
↓
Model training
↓
Evaluation
↓
Model serialization
↓
Flask deployment

---

# 🔬 Experiments

A major focus of this project was understanding how different data decisions affect model performance.

## Experiment 1 — Basic Model

A basic resale-price prediction model was developed using the available car features.

The model achieved an R² of approximately:

**0.84**

---

## Experiment 2 — Data and Outlier Investigation

Different data-cleaning decisions were investigated instead of automatically removing unusual observations.

This included investigating:

- Zero-valued sale prices
- Outliers
- Missing values
- Feature relationships
- Model performance after data changes

Some changes that initially appeared reasonable did not necessarily improve the model.

This helped understand the importance of validating data-cleaning decisions experimentally.

---

## Experiment 3 — Original Purchase Price

The original purchase price was investigated as an additional feature.

The reasoning was that the original price may contain useful information about the value of the vehicle.

This led to the development of the Advanced prediction model.

---

## Experiment 4 — Advanced Model

The Advanced model includes original purchase price in addition to the Basic features.

The model achieved an R² of approximately:

**0.98**

on the evaluation data used during development.

The improvement suggested that original purchase price contained useful predictive information for this dataset.

---

# ⚙️ Machine Learning Pipeline

The final application uses scikit-learn preprocessing pipelines.

Categorical features are encoded using OneHotEncoder.

Unknown categories are handled using:

```python
handle_unknown="ignore"