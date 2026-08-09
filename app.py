from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained ML pipelines
basic_model = joblib.load("models/basic_model.pkl")
advanced_model = joblib.load("models/advanced_model.pkl")


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Basic prediction
@app.route("/predict/basic", methods=["POST"])
def predict_basic():

    data = {
        "yr_mfr": float(request.form["yr_mfr"]),
        "fuel_type": request.form["fuel_type"],
        "kms_run": float(request.form["kms_run"]),
        "city": request.form["city"],
        "body_type": request.form["body_type"],
        "transmission": request.form["transmission"],
        "make": request.form["make"],
        "model": request.form["model"],
        "total_owners": float(request.form["total_owners"])
    }

    input_data = pd.DataFrame([data])

    prediction = basic_model.predict(input_data)[0]

    return render_template(
        "result.html",
        prediction=f"₹{prediction:,.0f}",
        mode="Basic"
    )


# Advanced prediction
@app.route("/predict/advanced", methods=["POST"])
def predict_advanced():

    data = {
        "yr_mfr": float(request.form["yr_mfr"]),
        "fuel_type": request.form["fuel_type"],
        "kms_run": float(request.form["kms_run"]),
        "city": request.form["city"],
        "body_type": request.form["body_type"],
        "transmission": request.form["transmission"],
        "make": request.form["make"],
        "model": request.form["model"],
        "total_owners": float(request.form["total_owners"]),
        "original_price": float(request.form["original_price"])
    }

    input_data = pd.DataFrame([data])

    prediction = advanced_model.predict(input_data)[0]

    return render_template(
        "result.html",
        prediction=f"₹{prediction:,.0f}",
        mode="Advanced"
    )


# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)