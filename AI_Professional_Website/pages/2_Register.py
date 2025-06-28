import streamlit as st
import sqlite3
import hashlib
import re

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_users_table():
    conn = sqlite3.connect('users.db', check_same_thread=False)
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                email TEXT UNIQUE,
                password TEXT
            )
        ''')
    conn.close()

def is_valid_username(username):
    return bool(re.match(r'^[A-Za-z0-9_]{3,20}$', username))  # 3-20 chars, letters, numbers, underscore

def is_valid_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

def is_strong_password(password):
    return (
        len(password) >= 6 and
        re.search(r'[A-Za-z]', password) and
        re.search(r'[0-9]', password)
    )

def username_exists(username):
    conn = sqlite3.connect('users.db', check_same_thread=False)
    cur = conn.cursor()
    cur.execute('SELECT 1 FROM users WHERE username = ?', (username,))
    exists = cur.fetchone() is not None
    conn.close()
    return exists

def email_exists(email):
    conn = sqlite3.connect('users.db', check_same_thread=False)
    cur = conn.cursor()
    cur.execute('SELECT 1 FROM users WHERE email = ?', (email,))
    exists = cur.fetchone() is not None
    conn.close()
    return exists

def register_user(username, email, password):
    conn = sqlite3.connect('users.db', check_same_thread=False)
    try:
        with conn:
            conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                         (username, email, hash_password(password)))
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

create_users_table()

st.title("Register")

reg_username = st.text_input("Username")
reg_email = st.text_input("Email")
reg_password = st.text_input("Password", type="password")

if st.button("Register"):
    # Validate fields
    if not reg_username or not reg_email or not reg_password:
        st.error("Please fill all fields.")
    elif not is_valid_username(reg_username):
        st.error("Username must be 3-20 characters and contain only letters, numbers, or underscores.")
    elif not is_valid_email(reg_email):
        st.error("Please enter a valid email address.")
    elif not is_strong_password(reg_password):
        st.error("Password must be at least 6 characters and contain both letters and numbers.")
    elif username_exists(reg_username):
        st.error("Username already exists. Please choose another.")
    elif email_exists(reg_email):
        st.error("Email already registered. Please use another.")
    else:
        if register_user(reg_username, reg_email, reg_password):
            st.success("Registration successful! You can now log in.")
        else:
            st.error("Registration failed. Please try again.")
