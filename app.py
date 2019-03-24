from flask import Flask, jsonify, render_template, request
app = Flask("__name__", static_folder="assets")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(pitch=0, roll=1, yaw=2)

if __name__ == "__main__":
    app.run()
