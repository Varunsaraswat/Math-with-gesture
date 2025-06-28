# 2_About_Us.py page content
import streamlit as st

if not st.session_state.get("authentication_status"):
    st.warning("Please log in to access this page.")
    st.stop()

st.title("ℹ️ About Us")

st.write("""
We are a team of developers passionate about combining artificial intelligence with interactive technologies.

### 🤖 Our Projects:
- **Hand Gesture Math Solver:** Uses computer vision and Gemini AI to recognize and solve handwritten math in the air.
- **Emotion Detection App:** Identifies human emotions in real-time using deep learning and OpenCV.

This site is built using **Streamlit**, **Flask**, **TensorFlow**, and **Gemini AI** to bring innovative AI experiences to life.
""")
