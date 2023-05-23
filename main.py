import os
import streamlit as st
from application import PARENT_DIR, APPLICATION_DIR, DATA_DIR, WEIGHTS_DIR, MODELS_DIR
from application.models.YOLOv5 import YOLOv5
from PIL import Image

# Configure the weights in .pt format to be loaded into the model
# The weights are stored in the applicaiton/data/weights/best.pt location
model = YOLOv5(os.path.join(WEIGHTS_DIR, 'best.pt'))

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
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = model.predict(uploaded_file)
    st.write('%s (%.2f%%)' % (label[1], label[2]*100))

# Create a section that displays the image labels and their corresponding confidence score
# "sculpture": 0, "drawings": 1, "iconography": 2, "engraving": 3, "painting": 4
st.write("This model is trained on the following labels: ")
st.write("0: sculpture\n, 1: drawings\n, 2: iconography\n, 3: engraving\n, 4: painting\n")




