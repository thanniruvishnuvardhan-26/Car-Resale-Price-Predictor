# 🚗 Car Resale Price Predictor

A Machine Learning based web application that predicts the resale price of used cars.

The project provides two prediction modes:

- **Basic Prediction** – uses essential car information.
- **Advanced Prediction** – additionally uses the original purchase price.

The trained ML pipelines are deployed through a Flask web application with an HTML/CSS/JavaScript frontend.

---

# 📌 Project Overview

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

The project was developed through multiple experiments involving:

- Data cleaning
- Feature investigation
- Outlier investigation
- Feature selection
- Model comparison
- Preprocessing pipelines
- Hyperparameter tuning
- Model evaluation
- Flask web deployment

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

The final Basic model uses **Random Forest**.

### Basic Model Performance

| Metric | Result |
|---|---:|
| R² | **0.921433** |
| MAE | **₹43,871** |
| RMSE | **₹78,841** |

The Basic model provides a resale estimate using essential vehicle information without requiring the original purchase price.

---

## 🟩 Advanced Prediction

The Advanced model uses all Basic features plus:

- Original purchase price

Different tree-based models were evaluated for the Advanced pipeline.

### Advanced Model Comparison

| Model | R² | MAE | RMSE |
|---|---:|---:|---:|
| Decision Tree | 0.967410 | ₹32,481 | ₹50,033 |
| Random Forest | 0.978933 | ₹29,691 | ₹40,226 |
| Gradient Boosting | **0.980771** | ₹29,420 | ₹38,432 |

Gradient Boosting produced the best initial Advanced-model performance.

---

# ⚙️ Hyperparameter Tuning

Hyperparameter tuning was performed to investigate whether the Advanced model could be improved further.

The tuned Gradient Boosting model achieved:

| Metric | Tuned Gradient Boosting |
|---|---:|
| R² | **0.981890** |
| MAE | **₹28,457** |
| RMSE | **₹37,297** |

The tuned Gradient Boosting model was selected as the final Advanced model.

---

# 🏆 Final Models

| Prediction Mode | Final Model | R² |
|---|---|---:|
| Basic | Random Forest | **0.921433** |
| Advanced | Tuned Gradient Boosting | **0.981890** |

The Advanced model achieved stronger performance on the evaluation data used during development.

> **Note:** R² is a regression evaluation metric. It should not be interpreted as classification accuracy.

---

# 🧠 Why Two Prediction Modes?

The project provides two different prediction modes because the amount of information available about a vehicle can vary.

### Basic Model

The Basic model requires only essential vehicle information.

It is useful when the original purchase price is unknown or unavailable.

### Advanced Model

The Advanced model additionally uses the original purchase price.

The experiments showed that this feature provided useful predictive information for the dataset and contributed to the stronger Advanced-model performance.

---

# 🔬 Machine Learning Workflow

The project followed this workflow:

```text
Dataset
   ↓
Data Exploration
   ↓
Data Cleaning
   ↓
Missing-Value Handling
   ↓
Invalid-Value Investigation
   ↓
Outlier Investigation
   ↓
Feature Investigation
   ↓
Feature Selection
   ↓
Categorical Encoding
   ↓
Train/Test Split
   ↓
Preprocessing Pipeline
   ↓
Model Training
   ↓
Model Comparison
   ↓
Hyperparameter Tuning
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
Flask Deployment
🧪 Experiments

A major focus of this project was understanding how different data and modelling decisions affect prediction performance.

Experiment 1 — Basic Model

A Basic resale-price prediction pipeline was developed using essential vehicle features.

Different models were investigated and Random Forest produced the strongest final Basic-model performance.

Final Basic R²:

0.921433

Experiment 2 — Data and Outlier Investigation

Different data-cleaning decisions were investigated instead of automatically removing unusual observations.

This included investigating:

Zero-valued sale prices
Outliers
Missing values
Feature relationships
Model performance after data changes

Some changes that initially appeared reasonable did not necessarily improve the model.

This helped demonstrate the importance of validating data-cleaning decisions experimentally.

Experiment 3 — Tree-Based Model Comparison

Several tree-based regression algorithms were compared:

Decision Tree
Random Forest
Gradient Boosting

The models were evaluated using:

R²
MAE
RMSE

This allowed the final model to be selected based on measured performance rather than simply choosing a model beforehand.

Experiment 4 — Original Purchase Price

The original purchase price was investigated as an additional feature.

The reasoning was that the original price may contain useful information about the value of a vehicle.

This led to the development of the Advanced prediction model.

Experiment 5 — Advanced Model

The Advanced model includes original purchase price in addition to the Basic features.

The Advanced pipeline achieved an R² of approximately:

0.98

on the evaluation data used during development.

The results suggested that original purchase price contained useful predictive information for this dataset.

Experiment 6 — Hyperparameter Tuning

Hyperparameter tuning was performed on the selected Advanced model to investigate whether further improvement was possible.

The tuned Gradient Boosting model improved the evaluation metrics to:

R²: 0.981890
MAE: ₹28,457
RMSE: ₹37,297

This model was selected as the final Advanced model.

🧠 Machine Learning Models

The project investigated the following regression algorithms.

Decision Tree

A tree-based regression model that recursively splits the data according to feature values.

Random Forest

An ensemble of multiple decision trees whose predictions are combined to produce the final prediction.

Random Forest produced the strongest Basic-model result.

Gradient Boosting

An ensemble technique that builds models sequentially, with each new model attempting to improve upon the errors of previous models.

Gradient Boosting produced the strongest initial Advanced-model performance and remained the best model after tuning.

⚙️ Machine Learning Pipeline

The final application uses scikit-learn preprocessing pipelines.

Categorical features are encoded using OneHotEncoder.

Unknown categories are handled using:

handle_unknown="ignore"

This allows the deployed pipeline to handle previously unseen categorical values more robustly.

The preprocessing steps and trained model are stored together as serialized pipelines.

🌐 Web Application

The trained models are integrated into a Flask web application.

The application provides:

Home Page

Users can choose between:

Basic Prediction
Advanced Prediction
Basic Prediction

The user enters essential vehicle information and receives an estimated resale value.

Advanced Prediction

The user enters the same vehicle information along with the original purchase price.

Result Page

The application displays:

Estimated resale value
Prediction mode
Model used
Test R²
Explanation of the prediction
Important limitations
Option to return to the home page
🛡️ Input Validation

The application includes validation at both the frontend and backend levels.

Examples include:

Manufacture year boundaries
Kilometers-driven boundaries
Owner-count validation
Original-price validation
Required fields
Invalid numeric input handling

This prevents many unreasonable inputs from reaching the prediction pipeline.

🧪 Application Testing

The application was tested using several scenarios:

Normal vehicle inputs
Unknown car brand/model
Invalid numerical values
Negative values
Unrealistic manufacture years
Basic prediction
Advanced prediction
Refreshing the application
Returning from the result page to the home page
Flask terminal error checking

The final application successfully handled the tested scenarios.

📊 Evaluation Metrics

The project uses three main regression metrics.

R² Score

Measures how well the model explains the variance in the target variable.

Higher values generally indicate better performance.

MAE — Mean Absolute Error

Measures the average absolute difference between predicted and actual prices.

Lower values are better.

RMSE — Root Mean Squared Error

Measures prediction error while giving greater weight to larger errors.

Lower values are better.

🛠️ Technologies Used
Programming
Python
Machine Learning
Scikit-learn
Pandas
NumPy
Joblib
Web Development
Flask
HTML
CSS
JavaScript
Development / Experimentation
Jupyter Notebook
VS Code
📁 Project Structure
Car-Resale-Price-Predictor/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── models/
│   ├── basic_model.pkl
│   └── advanced_model.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── notebooks/
    ├── Backend.ipynb
    ├── Model improvement investigation.ipynb
    ├── Experiment 4 the comparision(Advanced).ipynb
    ├── Basic_Pipeline.ipynb
    └── Advanced_Pipeline.ipynb

The original dataset is excluded from the public repository.

🚀 How to Run
1. Clone the repository
git clone https://github.com/thanniruvishnuvardhan-26/Car-Resale-Price-Predictor.git
2. Navigate to the project
cd Car-Resale-Price-Predictor
3. Install dependencies
pip install -r requirements.txt
4. Run the Flask application
py app.py
5. Open the application

Open the local Flask address shown in the terminal.

⚠️ Limitations

The predicted value is an estimate generated from patterns learned from the training data.

Actual resale prices can vary depending on factors such as:

Vehicle condition
Service history
Accident history
Location
Market demand
Seller/buyer negotiation
Additional vehicle features
Current market conditions

The reported evaluation metrics are based on the evaluation data used during development and do not guarantee the same performance for every real-world vehicle.

🔮 Future Improvements

Possible future improvements include:

Larger and more diverse datasets
Additional vehicle features
Current market-price data
More extensive hyperparameter optimization
Cross-validation based model comparison
Model explainability
Prediction intervals
Cloud deployment
Database integration
User accounts and prediction history
Automated model retraining
📌 Project Status

Version 2.5 — Completed

The project currently includes:

Data preprocessing
Feature investigation
Multiple regression models
Model comparison
Hyperparameter tuning
Two prediction modes
Serialized ML pipelines
Flask deployment
Frontend interface
Input validation
Model-performance information
Result interpretation
Application testing
GitHub documentation
👨‍💻 Author

Thanniru Vishnu Vardhan

B.Tech CSE Student

📜 Disclaimer

This project is developed for educational and demonstration purposes.

The predicted resale value should be treated as an ML-based estimate rather than a guaranteed market price.


