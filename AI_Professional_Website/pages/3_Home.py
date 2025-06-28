# 1_Home.py page content
import streamlit as st

if not st.session_state.get("authentication_status"):
    st.warning("Please log in to access this page.")
    st.stop()

st.title("🏠 Home")

st.write("""
Welcome to the AI Project Hub! This platform integrates two exciting AI-powered tools:

- ✍️ **Hand Gesture Math Solver** – Write math expressions in the air with your fingers, and get them solved using Gemini AI.
- 😊 **Emotion Detection App** – Real-time emotion recognition through your webcam.

Use the navigation bar above to explore different sections of the site.

Enjoy the magic of AI! 🚀
""")
