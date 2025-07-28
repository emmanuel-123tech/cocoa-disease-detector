import streamlit as st
import numpy as np
import os
import requests
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# === Download model from Google Drive if not present ===
MODEL_URL = "https://drive.google.com/uc?id=105xnxkx9Tpbh36Sww6IT2YozzPk0vK79"
MODEL_PATH = "model_tertinggi.h5"

if not os.path.exists(MODEL_PATH):
    with st.spinner("📦 Downloading model, please wait..."):
        response = requests.get(MODEL_URL)
        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)
        st.success("✅ Model downloaded successfully!")

# === Load model ===
model = load_model(MODEL_PATH)

# === Class names (adjust as needed) ===
class_names = ['Healthy', 'Monilia', 'OtherDisease']  # Customize if needed

# === Streamlit App ===
st.set_page_config(page_title="Cocoa Disease Detector", layout="centered")
st.title("🍫 Cocoa Leaf Disease Detection")
st.write("Upload a cocoa leaf image to detect whether it's healthy or infected.")

uploaded_file = st.file_uploader("📷 Upload a cocoa leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    img_resized = img.resize((224, 224))
    st.image(img_resized, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img_array = image.img_to_array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]

    st.success(f"🌿 Prediction: **{predicted_class}**")
