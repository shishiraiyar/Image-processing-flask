from flask import Flask, render_template, request, redirect
from os import path
from time import time
from image_processing import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/uploadImage", methods=["POST"])
def uploadImage():
    print(request.files)
    file = request.files['file']
    id = int(time())
    file.save(path.join("static/images", str(id) + ".png"))
    return {"id":id}

@app.route("/imageProcessing")
def imageProcessingPage():
    return render_template("imageProcessing.html")

@app.route("/imageProcessing", methods=["POST"])
def imageProcessing():
    id = request.json["id"]
    process = request.json["process"]
    path = "static/images/" + str(id) + ".png"
    if (process == "grayscale"):
        greyscale(path)
    if (process == "meanblur"):
        mean_blur(path)
    if (process == "gaussianblur"):
        gaussian_blur(path)
    if (process == "sobel"):
        sobel(path)
    if (process == "sharpen"):
        sharpen(path)
        
    return {"success":0}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")