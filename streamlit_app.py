import streamlit as st
import joblib
import pandas as pd


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CarValue AI",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# PREMIUM DARK UI
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- APP ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 15% 0%,
                rgba(37, 99, 235, 0.13),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 5%,
                rgba(124, 58, 237, 0.10),
                transparent 25%
            ),
            #080b12;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }


    /* ---------- TYPOGRAPHY ---------- */

    h1, h2, h3 {
        letter-spacing: -0.02em;
    }


    /* ---------- HERO ---------- */

    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        line-height: 1.7;
        max-width: 760px;
        margin-bottom: 1.5rem;
    }


    /* ---------- BADGE ---------- */

    .badge {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: rgba(37, 99, 235, 0.13);
        border: 1px solid rgba(96, 165, 250, 0.28);
        color: #93c5fd;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.7rem;
    }


    /* ---------- DIVIDER ---------- */

    .line {
        height: 1px;
        background: rgba(148, 163, 184, 0.13);
        margin: 1.8rem 0;
    }


    /* ---------- STREAMLIT CONTAINERS ---------- */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(15, 23, 42, 0.58);
        border: 1px solid rgba(148, 163, 184, 0.13);
        border-radius: 20px;
    }


    /* ---------- INPUTS ---------- */

    div[data-baseweb="input"] {
        border-radius: 10px;
    }

    div[data-baseweb="select"] {
        border-radius: 10px;
    }

    input {
        border-radius: 10px !important;
    }


    /* ---------- BUTTON ---------- */

    .stButton > button {
        width: 100%;
        min-height: 3.2rem;
        border-radius: 12px;
        font-weight: 700;
        font-size: 1rem;

        background:
            linear-gradient(
                135deg,
                rgba(37, 99, 235, 0.20),
                rgba(30, 41, 59, 0.70)
            );

        border: 1px solid rgba(96, 165, 250, 0.38);

        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #60a5fa;
        transform: translateY(-1px);
    }


    /* ---------- RADIO ---------- */

    div[role="radiogroup"] {
        gap: 1.2rem;
    }


    /* ---------- METRIC ---------- */

    div[data-testid="stMetric"] {
        background: rgba(15, 23, 42, 0.70);
        border: 1px solid rgba(148, 163, 184, 0.13);
        padding: 1.2rem;
        border-radius: 16px;
    }


    /* ---------- RESULT ---------- */

    .result-title {
        text-align: center;
        color: #94a3b8;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    .result-price {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 800;
        color: #f8fafc;
        margin: 0.4rem 0;
    }

    .result-mode {
        text-align: center;
        color: #60a5fa;
        font-size: 0.9rem;
        font-weight: 600;
    }


    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.78rem;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(148, 163, 184, 0.10);
    }


    /* ---------- MOBILE ---------- */

    @media (max-width: 768px) {

        .hero-title {
            font-size: 2.2rem;
        }

        .result-price {
            font-size: 2.5rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD MODELS
# ============================================================

@st.cache_resource
def load_models():

    basic_model = joblib.load("models/basic_model.pkl")
    advanced_model = joblib.load("models/advanced_model.pkl")

    return basic_model, advanced_model


try:

    basic_model, advanced_model = load_models()

except Exception as e:

    st.error("Unable to load the trained ML models.")
    st.exception(e)
    st.stop()


# ============================================================
# HERO
# ============================================================

st.markdown(
    '<div class="badge">Machine Learning • Used Cars</div>',
    unsafe_allow_html=True
)

st.markdown(
    "# 🚗 CarValue AI"
)

st.markdown(
    """
    <div class="hero-subtitle">
    Estimate the resale value of a used car using trained
    machine-learning pipelines built from real-world vehicle
    attributes.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MODEL SELECTION
# ============================================================

st.markdown("## Choose Your Prediction Model")

st.caption(
    "Select the prediction mode based on the information available "
    "about your vehicle."
)


card1, card2 = st.columns(2)


with card1:

    with st.container(border=True):

        st.markdown("### ⚡ Basic Model")

        st.caption("Quick estimate")

        st.write(
            "Uses standard vehicle information including "
            "manufacture year, fuel type, kilometres driven, "
            "city, body type, transmission, make, model and ownership."
        )


with card2:

    with st.container(border=True):

        st.markdown("### 🧠 Advanced Model")

        st.caption("More information")

        st.write(
            "Uses all Basic Model information plus the original "
            "purchase price of the vehicle."
        )


st.markdown(
    '<div class="line"></div>',
    unsafe_allow_html=True
)


# ============================================================
# MODE
# ============================================================

mode = st.radio(
    "Prediction Mode",
    ["Basic", "Advanced"],
    horizontal=True
)


# ============================================================
# VEHICLE INFORMATION
# ============================================================

st.markdown("## Vehicle Information")

st.caption(
    "Enter the details of the vehicle below."
)


col1, col2 = st.columns(2)


# ============================================================
# LEFT COLUMN
# ============================================================

with col1:

    yr_mfr = st.number_input(
        "Manufacture Year",
        min_value=1990,
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
        [
            "Petrol",
            "Diesel",
            "CNG",
            "LPG",
            "Electric"
        ]
    )


    transmission = st.selectbox(
        "Transmission",
        [
            "Manual",
            "Automatic"
        ]
    )


    total_owners = st.number_input(
        "Total Owners",
        min_value=1.0,
        value=1.0,
        step=1.0
    )


# ============================================================
# RIGHT COLUMN
# ============================================================

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


    if mode == "Advanced":

        original_price = st.number_input(
            "Original Purchase Price (₹)",
            min_value=1.0,
            value=800000.0,
            step=10000.0
        )

    else:

        original_price = None


# ============================================================
# PREDICT
# ============================================================

st.write("")

predict = st.button(
    "🔮  Estimate Resale Value",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if predict:

    # ---------------- VALIDATION ----------------

    if not city.strip():

        st.error("Please enter the city.")
        st.stop()


    if not body_type.strip():

        st.error("Please enter the body type.")
        st.stop()


    if not make.strip():

        st.error("Please enter the car make.")
        st.stop()


    if not model.strip():

        st.error("Please enter the car model.")
        st.stop()


    if total_owners < 1:

        st.error("Total owners must be at least 1.")
        st.stop()


    # ---------------- BASIC ----------------

    if mode == "Basic":

        data = {
            "yr_mfr": float(yr_mfr),
            "fuel_type": fuel_type,
            "kms_run": float(kms_run),
            "city": city.strip(),
            "body_type": body_type.strip(),
            "transmission": transmission,
            "make": make.strip(),
            "model": model.strip(),
            "total_owners": float(total_owners)
        }

        input_data = pd.DataFrame([data])


        try:

            prediction = basic_model.predict(input_data)[0]

        except Exception as e:

            st.error(
                "The Basic Model could not process these inputs."
            )

            st.exception(e)
            st.stop()


    # ---------------- ADVANCED ----------------

    else:

        if original_price is None or original_price <= 0:

            st.error(
                "Original purchase price must be greater than ₹0."
            )

            st.stop()


        data = {
            "yr_mfr": float(yr_mfr),
            "fuel_type": fuel_type,
            "kms_run": float(kms_run),
            "city": city.strip(),
            "body_type": body_type.strip(),
            "transmission": transmission,
            "make": make.strip(),
            "model": model.strip(),
            "total_owners": float(total_owners),
            "original_price": float(original_price)
        }


        input_data = pd.DataFrame([data])


        try:

            prediction = advanced_model.predict(input_data)[0]

        except Exception as e:

            st.error(
                "The Advanced Model could not process these inputs."
            )

            st.exception(e)
            st.stop()


    # ========================================================
    # RESULT
    # ========================================================

    prediction = max(0, float(prediction))


    st.write("")


    with st.container(border=True):

        st.markdown(
            '<div class="result-title">Estimated Resale Value</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="result-price">₹{prediction:,.0f}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="result-mode">'
            f'Prediction generated using the {mode} ML Pipeline'
            f'</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # PERFORMANCE
    # ========================================================

    st.write("")

    st.markdown("## Model Performance")

    st.caption(
        "Evaluation metrics obtained during model development."
    )


    if mode == "Advanced":

        st.info(
            "Advanced Model — Gradient Boosting"
        )

        m1, m2, m3 = st.columns(3)

        with m1:

            st.metric(
                "R² Score",
                "0.9819"
            )

        with m2:

            st.metric(
                "MAE",
                "₹28,457"
            )

        with m3:

            st.metric(
                "RMSE",
                "₹37,297"
            )

    else:

        st.info(
            "Basic Model prediction generated successfully. "
            "See the Model Comparison notebook for the complete "
            "evaluation of the Basic pipeline."
        )


    st.caption(
        "These metrics describe model performance on the evaluation "
        "data used during development. They do not guarantee the "
        "actual market resale price of an individual vehicle."
    )


# ============================================================
# HOW IT WORKS
# ============================================================

st.write("")

st.markdown("## How It Works")

st.caption(
    "From vehicle information to a machine-learning estimate."
)


step1, step2, step3 = st.columns(3)


with step1:

    with st.container(border=True):

        st.markdown("### 01 · Details")

        st.write(
            "Enter vehicle information such as age, mileage, "
            "fuel type, location and ownership history."
        )


with step2:

    with st.container(border=True):

        st.markdown("### 02 · ML Prediction")

        st.write(
            "The trained machine-learning pipeline processes "
            "the vehicle attributes."
        )


with step3:

    with st.container(border=True):

        st.markdown("### 03 · Estimate")

        st.write(
            "The model generates an estimated resale value "
            "based on the selected prediction mode."
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        <strong>CarValue AI</strong> · Car Resale Price Predictor<br>
        Built with Python · Pandas · Scikit-learn · Streamlit
    </div>
    """,
    unsafe_allow_html=True
)