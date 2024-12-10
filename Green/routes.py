from flask import render_template, request, url_for, jsonify, redirect
from Green import app  # Import the Flask app instance from the Green package
from Green.constants import *  # Import constants like TEAM_MEMBERS, PLANTS, PLANTS_IMGS
from random import shuffle, sample
import os
from .disease_detector import *  # Import the disease detection functions from disease_detector module

# Define a global variable to store the selected plant name
plant_name = None

@app.route('/home')
@app.route('/')
def home():
    # Shuffle the list of team members (assuming TEAM_MEMBERS is defined somewhere)
    shuffle(TEAM_MEMBERS)
    return render_template('home.html', TEAM_MEMBERS=TEAM_MEMBERS)

@app.route('/get-started/<plant>')
def get_started(plant=''):
    global plant_name
    if plant in PLANTS:  # Check if the provided plant is valid (in PLANTS list)
        plant_name = plant  # Set the global plant_name variable
        return render_template('get_started.html')
    else:
        return 'Invalid plant name'  # Return an error message if the plant name is invalid

@app.route('/choosing-plant', methods=['GET', 'POST'])
def choosing_plant():
    return render_template('choose_plant.html', PLANTS_IMGS=PLANTS_IMGS)

@app.route('/give-disease-name', methods=['POST'])
def give_disease_name():
    global plant_name
    if request.method == 'POST':
        # Retrieve form data: name, email, job, and plant image
        name = request.form.get('name')
        email = request.form.get('email')
        job = request.form.get('job')
        plant_img = request.files.get('plant-img')

        # Check if plant image and plant_name are both provided and valid
        if plant_img and plant_name is not None:
            # Define the path to save the uploaded plant image
            img_path = os.path.join('Green', 'static', 'img', 'user_plant', 'img.png')
            if os.path.exists(img_path):
                os.remove(img_path)  # Remove existing image at the path if it exists
            plant_img.save(img_path)  # Save the uploaded plant image to the specified path

            # Perform disease detection using the selected plant name
            response = test_model(plant_name, img_path)
            # Retrieve disease description based on the detected disease
            disease_description = get_data_for_disease(response)

            # Prepare data to display in the output template
            disease_data = {
                'name': response.replace('__', ' ').replace('_', ' '),
                'gallery_dir': response,
                'description': disease_description,
                'input_img': 'static/img/user_plant/img.png'  # Path to the uploaded plant image
            }

            # Randomly select a sample of doctors (assuming DOCTORS is defined somewhere)
            _DOCTORS = sample(DOCTORS, k=4)
            # Render the output template with selected doctors and disease data
            return render_template('output.html', DOCTORS=_DOCTORS, disease_data=disease_data)

    return 'Error: Missing required data.'  # Return an error message if data is missing or not valid
