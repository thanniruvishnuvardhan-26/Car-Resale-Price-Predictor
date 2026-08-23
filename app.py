from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained ML pipelines
basic_model = joblib.load("models/basic_model.pkl")
advanced_model = joblib.load("models/advanced_model.pkl")


# =========================
# VALIDATION SETTINGS
# =========================

MIN_YEAR = 1990
MAX_YEAR = 2026

MAX_KMS = 1_000_000
MAX_OWNERS = 10
MAX_ORIGINAL_PRICE = 10_00_00_000


# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# BASIC PREDICTION
# =========================

@app.route("/predict/basic", methods=["POST"])
def predict_basic():

    try:

        # -------------------------
        # Read input values
        # -------------------------

        yr_mfr = float(request.form["yr_mfr"])
        kms_run = float(request.form["kms_run"])
        total_owners = float(request.form["total_owners"])

        fuel_type = request.form["fuel_type"].strip()
        city = request.form["city"].strip()
        body_type = request.form["body_type"].strip()
        transmission = request.form["transmission"].strip()
        make = request.form["make"].strip()
        model = request.form["model"].strip()


        # -------------------------
        # Validate numeric values
        # -------------------------

        if not MIN_YEAR <= yr_mfr <= MAX_YEAR:
            return render_template(
                "index.html",
                error=f"Manufacture year must be between "
                      f"{MIN_YEAR} and {MAX_YEAR}."
            )


        if not 0 <= kms_run <= MAX_KMS:
            return render_template(
                "index.html",
                error="Kilometers driven must be between 0 and 10,00,000."
            )


        if not 1 <= total_owners <= MAX_OWNERS:
            return render_template(
                "index.html",
                error="Number of owners must be between 1 and 10."
            )


        # -------------------------
        # Validate text fields
        # -------------------------

        if not fuel_type:
            return render_template(
                "index.html",
                error="Please select a fuel type."
            )


        if not city:
            return render_template(
                "index.html",
                error="Please enter the city."
            )


        if not body_type:
            return render_template(
                "index.html",
                error="Please select a body type."
            )


        if not transmission:
            return render_template(
                "index.html",
                error="Please select a transmission type."
            )


        if not make:
            return render_template(
                "index.html",
                error="Please enter the car brand."
            )


        if not model:
            return render_template(
                "index.html",
                error="Please enter the car model."
            )


        # -------------------------
        # Create input DataFrame
        # -------------------------

        data = {
            "yr_mfr": yr_mfr,
            "fuel_type": fuel_type,
            "kms_run": kms_run,
            "city": city,
            "body_type": body_type,
            "transmission": transmission,
            "make": make,
            "model": model,
            "total_owners": total_owners
        }

        input_data = pd.DataFrame([data])


        # -------------------------
        # Make prediction
        # -------------------------

        prediction = basic_model.predict(input_data)[0]


        # -------------------------
        # Display result
        # -------------------------

        return render_template(
            "result.html",
            prediction=f"₹{prediction:,.0f}",
            mode="Basic"
        )


    except (ValueError, TypeError):

        return render_template(
            "index.html",
            error="Please enter valid values in all fields."
        )


    except Exception as e:

        print("Basic prediction error:", e)

        return render_template(
            "index.html",
            error="Something went wrong while making the prediction. "
                  "Please check your inputs and try again."
        )


# =========================
# ADVANCED PREDICTION
# =========================

@app.route("/predict/advanced", methods=["POST"])
def predict_advanced():

    try:

        # -------------------------
        # Read input values
        # -------------------------

        yr_mfr = float(request.form["yr_mfr"])
        kms_run = float(request.form["kms_run"])
        total_owners = float(request.form["total_owners"])
        original_price = float(request.form["original_price"])

        fuel_type = request.form["fuel_type"].strip()
        city = request.form["city"].strip()
        body_type = request.form["body_type"].strip()
        transmission = request.form["transmission"].strip()
        make = request.form["make"].strip()
        model = request.form["model"].strip()


        # -------------------------
        # Validate numeric values
        # -------------------------

        if not MIN_YEAR <= yr_mfr <= MAX_YEAR:
            return render_template(
                "index.html",
                error=f"Manufacture year must be between "
                      f"{MIN_YEAR} and {MAX_YEAR}."
            )


        if not 0 <= kms_run <= MAX_KMS:
            return render_template(
                "index.html",
                error="Kilometers driven must be between 0 and 10,00,000."
            )


        if not 1 <= total_owners <= MAX_OWNERS:
            return render_template(
                "index.html",
                error="Number of owners must be between 1 and 10."
            )


        if not 1 <= original_price <= MAX_ORIGINAL_PRICE:
            return render_template(
                "index.html",
                error="Original purchase price must be between "
                      "₹1 and ₹1,00,00,000."
            )


        # -------------------------
        # Validate text fields
        # -------------------------

        if not fuel_type:
            return render_template(
                "index.html",
                error="Please select a fuel type."
            )


        if not city:
            return render_template(
                "index.html",
                error="Please enter the city."
            )


        if not body_type:
            return render_template(
                "index.html",
                error="Please select a body type."
            )


        if not transmission:
            return render_template(
                "index.html",
                error="Please select a transmission type."
            )


        if not make:
            return render_template(
                "index.html",
                error="Please enter the car brand."
            )


        if not model:
            return render_template(
                "index.html",
                error="Please enter the car model."
            )


        # -------------------------
        # Create input DataFrame
        # -------------------------

        data = {
            "yr_mfr": yr_mfr,
            "fuel_type": fuel_type,
            "kms_run": kms_run,
            "city": city,
            "body_type": body_type,
            "transmission": transmission,
            "make": make,
            "model": model,
            "total_owners": total_owners,
            "original_price": original_price
        }

        input_data = pd.DataFrame([data])


        # -------------------------
        # Make prediction
        # -------------------------

        prediction = advanced_model.predict(input_data)[0]


        # -------------------------
        # Display result
        # -------------------------

        return render_template(
            "result.html",
            prediction=f"₹{prediction:,.0f}",
            mode="Advanced"
        )


    except (ValueError, TypeError):

        return render_template(
            "index.html",
            error="Please enter valid values in all fields."
        )


    except Exception as e:

        print("Advanced prediction error:", e)

        return render_template(
            "index.html",
            error="Something went wrong while making the prediction. "
                  "Please check your inputs and try again."
        )


# =========================
# RUN FLASK APPLICATION
# =========================

if __name__ == "__main__":
    app.run(debug=True)