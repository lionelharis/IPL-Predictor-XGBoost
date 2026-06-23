import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Load Model and Encoders
# -----------------------------
model = pickle.load(open("ipl_model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="IPL Winner Predictor",
    page_icon="🏏",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🏏 IPL Match Winner Predictor")
st.markdown(
    "Predict the winner of an IPL match using Machine Learning (XGBoost)"
)

st.divider()

# -----------------------------
# Current IPL Teams
# -----------------------------
teams = [
    "Chennai Super Kings",
    "Delhi Capitals",
    "Gujarat Titans",
    "Kolkata Knight Riders",
    "Lucknow Super Giants",
    "Mumbai Indians",
    "Punjab Kings",
    "Rajasthan Royals",
    "Royal Challengers Bengaluru",
    "Sunrisers Hyderabad"
]

# -----------------------------
# Current IPL Venues
# -----------------------------
allowed_venues = [
    "MA Chidambaram Stadium, Chepauk, Chennai",
    "Arun Jaitley Stadium, Delhi",
    "Narendra Modi Stadium, Ahmedabad",
    "Eden Gardens, Kolkata",
    "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
    "Wankhede Stadium, Mumbai",
    "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
    "Sawai Mansingh Stadium, Jaipur",
    "M Chinnaswamy Stadium, Bengaluru",
    "Rajiv Gandhi International Stadium, Uppal"
]

venues = [
    v for v in allowed_venues
    if v in encoders['venue'].classes_
]

# -----------------------------
# Input Section
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox(
        "Select Team 1",
        teams
    )

    team2 = st.selectbox(
        "Select Team 2",
        teams
    )

with col2:
    toss_winner = st.selectbox(
        "Toss Winner",
        teams
    )

    toss_decision = st.selectbox(
        "Toss Decision",
        ["bat", "field"]
    )

venue = st.selectbox(
    "Select Venue",
    venues
)

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Winner 🏆"):

    if team1 == team2:
        st.error(
            "Please select two different teams."
        )

    else:
        match = pd.DataFrame({
            "team1": [
                encoders["team1"]
                .transform([team1])[0]
            ],
            "team2": [
                encoders["team2"]
                .transform([team2])[0]
            ],
            "toss_winner": [
                encoders["toss_winner"]
                .transform([toss_winner])[0]
            ],
            "toss_decision": [
                encoders["toss_decision"]
                .transform([toss_decision])[0]
            ],
            "venue": [
                encoders["venue"]
                .transform([venue])[0]
            ]
        })

        prediction = model.predict(match)
        winner = (
            encoders["winner"]
            .inverse_transform(prediction)[0]
        )

        probability = model.predict_proba(match)[0]
        confidence = max(probability) * 100

        st.success(
            f"🏆 Predicted Winner: {winner}"
        )

        st.info(
            f"Winning Probability: "
            f"{confidence:.2f}%"
        )

        st.progress(int(confidence))

        st.balloons()