import streamlit as st
from datetime import datetime
import pandas as pd
import os

DATA_DIR = "data"
RSVP_FILE = os.path.join(DATA_DIR, "rsvps.csv")

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize RSVP file if it doesn't exist
if not os.path.exists(RSVP_FILE):
    pd.DataFrame(columns=["timestamp", "name", "email", "guests", "attending", "message"]).to_csv(RSVP_FILE, index=False)

def save_rsvp(data: dict):
    df = pd.read_csv(RSVP_FILE)
    # Use pd.concat instead of deprecated df.append
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(RSVP_FILE, index=False)

st.markdown("<a id='rsvp-section'></a>", unsafe_allow_html=True)
st.markdown("<h3 style='font-family: Playfair Display, serif;'>RSVP</h3>", unsafe_allow_html=True)

with st.form("rsvp_form"):
    name = st.text_input("Full name", max_chars=100)
    email = st.text_input("Email")
    guests = st.number_input("Number of guests (including you)", min_value=1, max_value=10, value=1)
    attending = st.radio("Will you attend?", ("Yes, we'll be there", "Sorry, we can't make it"))
    message = st.text_area("Message to the couple (optional)")
    submitted = st.form_submit_button("Submit RSVP")

    if submitted:
        if not name or not email:
            st.error("Please provide your name and email.")
        else:
            payload = {
                "timestamp": datetime.utcnow().isoformat(),
                "name": name,
                "email": email,
                "guests": int(guests),
                "attending": attending,
                "message": message,
            }
            save_rsvp(payload)
            st.success("Thank you — your RSVP has been recorded.")