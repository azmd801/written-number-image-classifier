import streamlit as st
import numpy as np
from PIL import Image
import requests
import json

# Define the FastAPI endpoint URL
FASTAPI_URL = "http://127.0.0.1:8080/predict"  # Replace with your actual endpoint

# Streamlit app
st.title("Predict written text in the image")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file).convert("L")  # Convert to grayscale
    image = image.resize((256, 256))  # Resize to 256x256
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert image to numpy array
    image_array = np.array(image).astype(np.float32)
    image_array = np.expand_dims(image_array, axis=(0, -1))  # Shape: [1, 256, 256, 1]

    st.write(f"Image shape: {image_array.shape}")

    # Send the numpy array to FastAPI
    if st.button("predit written number"):
        data = {"input": image_array.tolist()}  # Convert to list for JSON serialization
        response = requests.post(FASTAPI_URL, json=data)
        if response.status_code == 200:
            st.success("Hoorah!!! your image successfully sent for prediction")
            prediction = response.json()["predictions"]
            st.write(f"Your image contains {prediction}")
        else:
            st.error("oops")
            st.write("Error:", response.text)
