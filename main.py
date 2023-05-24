import os
import streamlit as st
from application.models.YOLOv5 import YOLOv5
from PIL import Image
import yolov5
import pickle
import sklearn
import base64
import tensorflow as tf
from application import PARENT_DIR, APPLICATION_DIR, DATA_DIR, WEIGHTS_DIR, MODELS_DIR

# Load the saved model from the file
# open the pickle file located in the application/data/weigths/decision_tree_model.pkl location

# filename = 'decision_tree_model.pkl'
# filename = 'art_classifier_model.pkl'
# with open(os.path.join(WEIGHTS_DIR, filename), 'rb') as file:
#     model = pickle.load(file)
# with open(os.path.join(WEIGHTS_DIR, filename), 'rb') as file:
#     with open(file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# model = pickle.load(open(WEIGHTS_DIR, filename), 'rb')

# # Use the loaded model for prediction
# # Configure the weights in .pt and .pkl format to be loaded into the model
# # The weights are stored in the applicaiton/data/weights/best.pt location

model = YOLOv5(os.path.join(WEIGHTS_DIR, 'best.pt'))
# model = yolov5.load(os.path.join(WEIGHTS_DIR, 'best.pt'))
# model = yolov5.load(os.path.join(WEIGHTS_DIR, 'best.pt'))

# Create a title and sub-title
st.write("""
Artistic Image Classification model
""")
st.write("This is a simple image classification web app to predict the artistic style of the image")

# Create a section that allow users to upload their own image.
# Accepts all image formats: jpg, png, jpeg
st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Create a section that displays the image
if uploaded_file is not None:
    imageOr = Image.open(uploaded_file)

    # with open(imageOr, 'rb') as f:
    #     data = f.read()
    #     imageNew  = base64.b64encode(data).decode()
    # print(type(image))
    st.image(imageOr, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    label = model.predict(imageOr)
    # label = model.predict((str(imageNew)))
    st.write('%s (%.2f%%)' % (label[1], label[2]*100))

# Create a section that displays the image labels and their corresponding confidence score
# "sculpture": 0, "drawings": 1, "iconography": 2, "engraving": 3, "painting": 4
st.write("This model is trained on the following labels: ")
st.write("0: sculpture\n, 1: drawings\n, 2: iconography\n, 3: engraving\n, 4: painting\n")




