# Import necessary libraries
from tensorflow import keras  # TensorFlow deep learning library
import cv2  # OpenCV library for image processing
import numpy as np  # NumPy library for numerical operations
import json  # Library for handling JSON data

# Function to test a machine learning model for plant disease detection
def test_model(plant, img_path):
    # Construct the path to the saved model for the specified plant
    model_path = f"Green/static/models/model_{plant}"
    # Load the trained Keras model from the specified path
    model = keras.models.load_model(model_path)

    # Load the mapping of prediction labels from a JSON file associated with the model
    with open(f"{model_path}/labels.json", 'r') as f:
        data = json.load(f)
        keys_to_labels = data['keys_to_labels']
        print(f'keys_to_labels={keys_to_labels}')  # Print the loaded label mapping

    # Read the input image from the specified path using OpenCV
    input_image = cv2.imread(img_path)
    # Resize the input image to the required dimensions for model input (224x224)
    input_image_resize = cv2.resize(input_image, (224, 224))
    # Scale pixel values to be between 0 and 1 for neural network input
    input_image_scaled = input_image_resize / 255.0
    # Reshape the image data to match the expected input shape of the model
    image_reshaped = np.reshape(input_image_scaled, [1, 224, 224, 3])
    # Perform inference on the reshaped image using the loaded model
    input_prediction = model.predict(image_reshaped)
 
    # Get the predicted label index (class) with the highest probability
    input_pred_label = str(np.argmax(input_prediction))
    # Retrieve the corresponding disease label using the mapping
    return keys_to_labels.get(input_pred_label)

# Function to retrieve data associated with a specific disease name from a JSON file
def get_data_for_disease(disease_name):
    # Load the disease data JSON file containing information about various diseases
    with open('Green/static/diseases/data.json', 'r') as f:
        data = json.load(f)
    # Retrieve and return the data for the specified disease name
    return data.get(disease_name)
