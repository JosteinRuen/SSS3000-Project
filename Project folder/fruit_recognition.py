from tensorflow import keras
import tensorflow as tf
import os
import numpy as np


#model = keras.models.load_model('object_recognition_fruit.tflite')
interpreter = tf.lite.Interpreter(model_path='object_recognition_fruit.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Load and preprocess the input image
image = tf.keras.preprocessing.image.load_img('images/mango fruit/Image_30.jpg', target_size=(64, 64))
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