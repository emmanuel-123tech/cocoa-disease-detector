# 🍫 Cocoa Leaf Disease Detection App

This is a Streamlit web app that uses a deep learning model to detect diseases in cocoa leaves from uploaded images.

## 🌿 Features
- Upload a cocoa leaf image (JPG/PNG)
- Get instant predictions on whether the leaf is:
  - ✅ Healthy
  - ⚠️ Infected (e.g., Monilia or other disease)
- Clean and responsive interface
- Powered by TensorFlow and Streamlit

## 🚀 Live Demo
👉 [Click here to launch the app](https://share.streamlit.io/) *(Replace with your Streamlit Cloud link after deployment)*

---

## 🧠 Model Info
- Framework: TensorFlow / Keras
- Format: `.h5`
- Input shape: 224x224 RGB images
- Classes: `Healthy`, `Monilia`, `OtherDisease` *(customizable based on training data)*

---

## 🗂 Files in This Repo
| File                 | Purpose                                     |
|----------------------|---------------------------------------------|
| `app.py`             | Streamlit app script                        |
| `model_tertinggi.h5` | Trained Keras model for prediction          |
| `requirements.txt`   | List of Python packages for deployment      |
| `README.md`          | Project overview (you’re reading it!)       |

---

## 💻 How to Run Locally
```bash
# Clone the repo
git clone https://github.com/yourusername/cocoa-disease-detector
cd cocoa-disease-detector

# Install dependencies
pip install -r requirements.txt

# Run Streamlit
streamlit run app.py
