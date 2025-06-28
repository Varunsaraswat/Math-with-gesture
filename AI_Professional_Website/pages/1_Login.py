import streamlit as st
import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username, password):
    conn = sqlite3.connect('users.db', check_same_thread=False)
    cur = conn.cursor()
    cur.execute('SELECT password FROM users WHERE username = ?', (username,))
    row = cur.fetchone()
    conn.close()
    if row and row[0] == hash_password(password):
        return True
    return False

st.title("Login")

if st.session_state.get('authentication_status'):
    st.success(f"Already logged in as {st.session_state.get('username')}")
    if st.button("Logout"):
        st.session_state['authentication_status'] = False
        st.session_state['username'] = None
        st.experimental_rerun()
else:
    login_user = st.text_input("Username")
    login_pass = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_login(login_user, login_pass):
            st.session_state['authentication_status'] = True
            st.session_state['username'] = login_user
            st.success(f"Welcome, {login_user}!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password.")
            st.info("Don't have an account? [Register here](./2_Register)")

            # Optional: Button to go to Register page
            if st.button("Go to Registration"):
                st.switch_page("pages/2_Register.py")
