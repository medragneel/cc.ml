# predict.py
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import os


model_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'cells2.0.h5')


def predict_image(image_path):
    # Load the trained model
    model = load_model(model_path)  # Adjust the path

    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(80, 80))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    # Make predictions
    predictions = model.predict(img_array)

    # Get the predicted class
    class_index = np.argmax(predictions)
    classes = ['EOSINOPHIL', 'LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL']
    predicted_class = classes[class_index]

    return predicted_class
