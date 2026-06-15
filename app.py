import streamlit as st
import joblib

# Load the trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# App Title
st.set_page_config(page_title="Spam Email Detector", page_icon="📧")

st.title("📧 Spam Email Detection")
st.write("Enter an email or message below to check whether it is Spam or Not Spam.")

# User Input
email = st.text_area("Enter Email Text")

if st.button("Predict"):

    if email.strip() == "":
        st.warning("Please enter some text.")

    else:
        transformed = vectorizer.transform([email])
        prediction = model.predict(transformed)

        if prediction[0] == 1:
            st.error("🚨 This is a Spam Email")
        else:
            st.success("✅ This is Not Spam")