from tensorflow import keras
import tensorflow as tf
import os
import numpy as np
from create_recipies import *


#model = keras.models.load_model('object_recognition_fruit.tflite')
interpreter = tf.lite.Interpreter(model_path='object_recognition_fruit_v7.tflite')
interpreter.allocate_tensors()


# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
'''
# Load and preprocess the input image
image = tf.keras.preprocessing.image.load_img('images/mango fruit/Image_31.jpg', target_size=(64, 64))
image = tf.keras.preprocessing.image.img_to_array(image)
image = np.expand_dims(image, axis=0)
image = image / 255.0  # Normalize the pixel values (if required)

# Set the input tensor
interpreter.set_tensor(input_details[0]['index'], image)

# Run the inference
interpreter.invoke()

# Get the output tensor
output_tensor = interpreter.get_tensor(output_details[0]['index'])

# Process the output
predicted_class = np.argmax(output_tensor)
print(predicted_class)
'''
# Folder path containing the images
folder_path = 'fruits'


detected_ingredients = []

# Iterate through the images in the folder
print("Starting iteration")
for filename in os.listdir(folder_path):
    print("File name: ", filename)
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Adjust file extensions as needed
        # Load and preprocess the input image
        image_path = os.path.join(folder_path, filename)
        image = tf.keras.preprocessing.image.load_img(image_path, target_size=(64, 64))
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = image / 255.0  # Normalize the pixel values (if required)

        # Set the input tensor
        interpreter.set_tensor(input_details[0]['index'], image)

        # Run the inference
        interpreter.invoke()

        # Get the output tensor
        output_tensor = interpreter.get_tensor(output_details[0]['index'])

        # Process the output
        predicted_class = np.argmax(output_tensor)

        print(f"Image: {filename}, Predicted class: {predicted_class}")
        detected_ingredients.append(predicted_class)

ingredients_codes = {0: 'Apple', 1: 'Banana', 2: 'Cabbage', 3: 'Cucumber', 4: 'Garlic', 5: 'Ginger', 6: 'Grape', 7: 'Kiwi', 8: "Orange",
                      9: "Bell Pepper"}
recipies = initialize_recipies()


#remove all duplicates from the list, alternatively store duplicates in a separate list
detected_ingredients = list(dict.fromkeys(detected_ingredients))
#convert the list of codes to list of ingredients
for i in range(len(detected_ingredients)):
    detected_ingredients[i] = ingredients_codes[detected_ingredients[i]]

print("Detected ingredients: ",detected_ingredients)
detected_recipies = []
#check if the detected ingredients match any of the recipies
for recipe in recipies:
    ingredients = recipe["ingredients"]

    if(set(ingredients).issubset(set(detected_ingredients))):
        print("Recipe found: ", recipe["name"])
        detected_recipies.append(recipe)


