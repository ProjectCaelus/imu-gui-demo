from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import random, math

app = Flask("__name__", static_folder="assets")
# Prevent CORS errors
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    orientation = {"pitch": random.random()*math.pi*2, "roll": random.random()*math.pi*2, "yaw": random.random()*math.pi*2}
    acceleration = {"x": random.randint(0, 10), "y": random.randint(0, 10), "z": random.randint(0, 10)}
    return jsonify({"a": acceleration, "o": orientation})

if __name__ == "__main__":
    app.run()
