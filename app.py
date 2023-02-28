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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")