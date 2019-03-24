from flask import Flask, jsonify, render_template, request
app = Flask("__name__")

@app.route("/")
def index():
    return "Hello, Project Caelus"

@app.route("/data")
def data():
    return jsonify(pitch=0, roll=1, yaw=2)

if __name__ == "__main__":
    app.run()
