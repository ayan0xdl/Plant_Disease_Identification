import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model("trained_model.keras")

class_names = ['Apple scab',
 'Apple Black rot',
 'Apple Cedar apple rust',
 'Apple healthy',
 'Blueberry healthy',
 'Cherry Powdery mildew',
 'Cherry healthy',
 'Corn Cercospora leaf spot Gray leaf spot',
 'Corn Common rust',
 'Corn Northern Leaf_Blight',
 'Corn healthy',
 'Grape Black rot',
 'Grape Esca_(Black_Measles)',
 'Grape Leaf blight (Isariopsis Leaf Spot)',
 'Grape healthy',
 'Orange Haunglongbing (Citrus_greening)',
 'Peach Bacterial spot',
 'Peach healthy',
 'Bell Pepper Bacterial_spot',
 'Bell Pepper healthy',
 'Potato Early blight',
 'Potato Late blight',
 'Potato healthy',
 'Raspberry healthy',
 'Soybean healthy',
 'Squash Powdery mildew',
 'Strawberry Leaf scorch',
 'Strawberry healthy',
 'Tomato Bacterial_spot',
 'Tomato Early blight',
 'Tomato Late blight',
 'Tomato Leaf Mold',
 'Tomato Septoria leaf spot',
 'Tomato Spider mites Two-spotted spider mite',
 'Tomato Target_Spot',
 'Tomato Yellow Leaf Curl Virus',
 'Tomato mosaic virus',
 'Tomato healthy']

def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)
    confidence = float(np.max(predictions))

    return class_names[class_index], confidence
