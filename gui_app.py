import streamlit as st
import tensorflow as tf
import os

# Define the path to the model
desktop_path = os.path.expanduser("~/Desktop/AI Model")
model_path = os.path.join(desktop_path, "saved_model")

# Check if the model directory exists
if not os.path.exists(model_path):
    st.error(f"Model directory does not exist at {model_path}")
else:
    st.write(f"Model directory found at {model_path}")

    # Load your model
    try:
        model = tf.saved_model.load(model_path)
        st.write('Model Loaded Successfully')
    except Exception as e:
        st.error(f"Error loading model: {e}")

# Your Streamlit code to interact with the model
st.title('Mosquito Identification App')
st.write('Upload an image to identify mosquito species.')

# Example code to handle image upload (if applicable)
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("Processing...")

    # Add your model inference code here
    # e.g., result = model.predict(uploaded_file)
    # st.write(f"Prediction: {result}")
