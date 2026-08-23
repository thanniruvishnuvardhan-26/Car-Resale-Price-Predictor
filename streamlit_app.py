import streamlit as st
import joblib
import pandas as pd


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Car Resale Price Predictor",
    page_icon="🚗",
    layout="centered"
)


# --------------------------------------------------
# Load trained ML pipelines
# --------------------------------------------------

@st.cache_resource
def load_models():
    basic_model = joblib.load("models/basic_model.pkl")
    advanced_model = joblib.load("models/advanced_model.pkl")
    return basic_model, advanced_model


basic_model, advanced_model = load_models()


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🚗 Car Resale Price Predictor")
st.write(
    "Estimate the resale value of a used car using trained machine-learning models."
)


# --------------------------------------------------
# Prediction mode
# --------------------------------------------------

mode = st.radio(
    "Select Prediction Mode",
    ["Basic", "Advanced"],
    horizontal=True
)


st.divider()


# --------------------------------------------------
# Input fields
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    yr_mfr = st.number_input(
        "Manufacture Year",
        min_value=1900,
        max_value=2026,
        value=2018,
        step=1
    )

    kms_run = st.number_input(
        "Kilometers Driven",
        min_value=0.0,
        value=50000.0,
        step=1000.0
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
    )

    transmission = st.selectbox(
        "Transmission",
        ["Manual", "Automatic"]
    )


with col2:

    city = st.text_input(
        "City",
        value="Hyderabad"
    )

    body_type = st.text_input(
        "Body Type",
        value="Hatchback"
    )

    make = st.text_input(
        "Car Make",
        value="Maruti"
    )

    model = st.text_input(
        "Car Model",
        value="Swift"
    )

    total_owners = st.number_input(
        "Total Owners",
        min_value=1.0,
        value=1.0,
        step=1.0
    )


# --------------------------------------------------
# Advanced-only input
# --------------------------------------------------

original_price = None

if mode == "Advanced":

    st.divider()

    original_price = st.number_input(
        "Original Purchase Price (₹)",
        min_value=0.0,
        value=800000.0,
        step=10000.0
    )


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("🔮 Predict Resale Price", use_container_width=True):

    # Manufacture year validation
    if yr_mfr > 2026:
        st.error("Manufacture year cannot be in the future.")

    elif total_owners < 1:
        st.error("Total owners must be at least 1.")

    elif mode == "Advanced" and original_price <= 0:
        st.error("Original purchase price must be greater than 0.")

    else:

        if mode == "Basic":

            data = {
                "yr_mfr": float(yr_mfr),
                "fuel_type": fuel_type,
                "kms_run": float(kms_run),
                "city": city,
                "body_type": body_type,
                "transmission": transmission,
                "make": make,
                "model": model,
                "total_owners": float(total_owners)
            }

            input_data = pd.DataFrame([data])

            prediction = basic_model.predict(input_data)[0]

        else:

            data = {
                "yr_mfr": float(yr_mfr),
                "fuel_type": fuel_type,
                "kms_run": float(kms_run),
                "city": city,
                "body_type": body_type,
                "transmission": transmission,
                "make": make,
                "model": model,
                "total_owners": float(total_owners),
                "original_price": float(original_price)
            }

            input_data = pd.DataFrame([data])

            prediction = advanced_model.predict(input_data)[0]


        # --------------------------------------------------
        # Result
        # --------------------------------------------------

        st.success("Prediction completed!")

        st.metric(
            label="Estimated Resale Value",
            value=f"₹{prediction:,.0f}"
        )

        st.caption(f"Prediction Mode: {mode}")