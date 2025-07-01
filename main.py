import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

#model prediction

def model_pred(test_image):
    model = load_model('trained_model.keras')
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=[128,128])
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])

    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

#sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Choose Page", ["🌿 About", "🦠 Disease Recognition"])

# About Page
if app_mode == "🌿 About":
    st.title("🌱 Plant Disease Recognition System")
    st.image("https://cdn.pixabay.com/photo/2018/05/06/08/00/ferns-3378058_1280.jpg")
    st.markdown("""
        Welcome to the **Plant Disease Recognition System**!  
        Upload an image of a plant leaf and let our deep learning model predict what disease it may have.

        🔍 **What it does:**
        - Detects 38 plant diseases
        - Supports multiple crop types
        - Fast and accurate using deep learning (CNN)

        🚀 **Tech stack:**
        - TensorFlow 2.x
        - Streamlit UI
        - PlantVillage dataset
        
        **Created by Ayan**  
        GitHub: [lighting-pixel](https://github.com/Lighting-pixel)
    """)

# Prediction Page
elif app_mode == "🦠 Disease Recognition":
    st.title("🧬 Identify Plant Disease")
    uploaded_file = st.file_uploader("Upload a plant leaf image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image")
        st.write("Processing...")
        result_index = model_pred(uploaded_file)

        #class names
        class_names = ['Apple_scab', 'Black_rot', 'Cedar_apple_rust', 'Apple_healthy', 'Blueberry_healthy',
                  'Cherry_Powdery_mildew', 'Cherry_healthy', 'Corn_Cercospora_leaf_spot', 'Corn_Common_rust',
                  'Corn_Northern_Leaf_Blight', 'Corn_healthy', 'Grape_Black_rot', 'Grape_Esca',
                  'Grape_Leaf_blight', 'Grape_healthy', 'Orange_Huanglongbing', 'Peach_Bacterial_spot',
                  'Peach_healthy', 'Pepper_Bacterial_spot', 'Pepper_healthy', 'Potato_Early_blight',
                  'Potato_Late_blight', 'Potato_healthy', 'Raspberry_healthy', 'Soybean_healthy',
                  'Squash_Powdery_mildew', 'Strawberry_Leaf_scorch', 'Strawberry_healthy',
                  'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_Leaf_Mold',
                  'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites', 'Tomato_Target_Spot',
                  'Tomato_Yellow_Leaf_Curl_Virus', 'Tomato_mosaic_virus', 'Tomato_healthy']

        st.success(f"🩺 **Prediction**: `{class_names[result_index]}`")

