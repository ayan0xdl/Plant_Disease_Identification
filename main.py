# main_streamlit.py
import streamlit as st
import requests

st.set_page_config(page_title="🌿 Plant Disease Detector", layout="centered")

st.title("🌿Plant Disease Recognition ")

menu = st.sidebar.selectbox("Select View", ["About", "Disease Detection"])

if menu == "About":
    st.markdown("""
    ## 🌿 Welcome!
    This app identifies plant diseases from leaf images and suggests treatments using Gemini.

    **Tech Stack:**
    - TensorFlow 2.x for disease classification
    - Gemini (via FastAPI backend) for treatment recommendations
    - Streamlit for frontend

    **Author:** Ayan (GitHub: [Lighting-pixel](https://github.com/Lighting-pixel))
    """)

elif menu == "Disease Detection":
    uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image")

        with st.spinner("Predicting..."):
            files = {"file": uploaded_file.getvalue()}
            response = requests.post("http://localhost:8000/predict", files=files)
            result = response.json()

            disease = result["disease"]
            confidence = round(result["confidence"] * 100, 2)

        st.success(f"🩺 Predicted: **{disease}** ({confidence}%)")

        if st.button("💡 Learn more from Gemini"):
            with st.spinner("Gemini is thinking..."):
                response = requests.post("http://localhost:8000/gemini_disease_info", json={"disease": disease})
                advice = response.json().get("reply", "❌ Couldn’t fetch Gemini’s response.")

            st.markdown("### 🌿 Gemini's Advice")
            st.markdown(f"<div style='background:#e8f5e9;padding:15px;border-left:4px solid #4CAF50;border-radius:5px; color:black;'>{advice}</div>", unsafe_allow_html=True)

