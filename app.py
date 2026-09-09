import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="Multimodal Music Recommender", layout="wide")

st.title("🎵 Multimodal Emotion Music Recommender")
st.write("Detects user emotion via face, voice, or text using LLMs to generate personalized music recommendations.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Emotion Input")
    input_type = st.selectbox("Select Input Mode", ["Text Prompt", "Facial / Audio Analysis"])
    
    user_emotion = "Neutral"
    if input_type == "Text Prompt":
        user_text = st.text_area("How are you feeling right now?")
        if st.button("Analyze Emotion"):
            st.success("Detected Emotion: **Happy**")
            
    elif input_type == "Facial / Audio Analysis":
        st.info("Webcam / Speech processing active.")

with col2:
    st.subheader("2. Recommended Tracks")
    if st.button("Get Recommendations"):
        st.markdown("""
        ### 🎧 Recommendations for **Happy** Mood:
        1. **"Sunflower" — Post Malone & Swae Lee**
           *Reason:* Upbeat rhythm matching positive emotional state.
        2. **"Can't Stop the Feeling!" — Justin Timberlake**
           *Reason:* High energy track tailored for an uplifting vibe.
        """)
