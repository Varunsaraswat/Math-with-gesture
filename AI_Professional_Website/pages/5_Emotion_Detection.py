import streamlit as st
import os
import subprocess

st.title("😊 Emotion Detection")

st.write("This version now runs inside Streamlit. Please open `emotion_detector_streamlit.py` directly.")

if st.button("Open Streamlit Emotion Detector"):
    script_path = os.path.abspath("emotion_detector_streamlit.py")
    subprocess.Popen(["streamlit", "run", script_path], shell=True)
    st.success("Emotion Detector is launching in a new tab...")
