import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load the trained model
model = load_model("model_tertinggi.h5")

# Define class names (update this if you have more or fewer classes)
class_names = ['Healthy', 'Monilia', 'OtherDisease']  # <-- Change if needed

# Streamlit UI
st.set_page_config(page_title="Cocoa Disease Detector", layout="centered")
st.title("🍫 Cocoa Leaf Disease Detection")
st.write("Upload a cocoa leaf image to detect whether it's healthy or infected.")

# Upload image
uploaded_file = st.file_uploader("Upload a cocoa leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    img_resized = img.resize((224, 224))
    st.image(img_resized, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    img_array = image.img_to_array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]

    st.success(f"🌿 Predicted Class: **{predicted_class}**")
