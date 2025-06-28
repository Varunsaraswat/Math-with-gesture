import streamlit as st
import yagmail

if not st.session_state.get("authentication_status"):
    st.warning("Please log in to access this page.")
    st.stop()

st.title("📬 Contact Us")
st.write("Have questions or feedback? We'd love to hear from you!")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send Message")

    if submitted:
        if name and email and message:
            try:
                # Load email credentials from Streamlit secrets
                sender = st.secrets["email"]["address"]
                app_password = st.secrets["email"]["app_password"]
                to_address = st.secrets["email"]["to_address"]

                # Compose the email
                subject = f"Contact Form Submission from {name}"
                body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

                # Send the email
                yag = yagmail.SMTP(sender, app_password)
                yag.send(to=to_address, subject=subject, contents=body)
                st.success(f"Thanks {name}! Your message has been sent.")
            except Exception as e:
                st.error(f"Failed to send message. Error: {e}")
        else:
            st.error("Please fill out all fields before submitting.")
