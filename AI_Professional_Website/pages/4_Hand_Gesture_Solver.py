import streamlit as st
import subprocess
import os

if not st.session_state.get("authentication_status"):
    st.warning("Please log in to access this page.")
    st.stop()

st.title("✍️ Hand Gesture Math Solver")

st.write("This app uses your hand gestures to write math problems and solve them .")

if st.button("Launch Math Solver App"):
    st.info("Launching... Please wait.")
    script_path = os.path.abspath("main1_refactored_streamlit.py")
    subprocess.Popen(["streamlit", "run", script_path], shell=True)
    st.success("Math Solver is launching in a new tab...")

st.markdown("""
    <style>
    .stApp {
        background-image: url("static/img1.png");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }
    </style>
""", unsafe_allow_html=True)

