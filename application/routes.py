from application import app
from flask import render_template

@app.route("/home")
def home():
    # Accept image data from user



    # Call the model selected to perform prediction


    # Create the value to return to the uesr based on the model prediction

    return render_template(
        "home.html"
    )
