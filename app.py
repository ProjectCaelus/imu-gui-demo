from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import random, math, socket

TCP_IP = '127.0.0.1' # Need to change to IP of groundstation
TCP_PORT = 5005
BUFFER_SIZE = 1024 # Can make this lower if we need speed

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)

conn, addr = sock.accept()

app = Flask("__name__", static_folder="assets")
# Prevent CORS errors
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    sock_data = conn.recv(BUFFER_SIZE)

    orientation = sock_data["o"]#{"pitch": random.random()*math.pi*2, "roll": random.random()*math.pi*2, "yaw": random.random()*math.pi*2}
    acceleration = sock_data["a"]#{"x": random.randint(0, 10), "y": random.randint(0, 10), "z": random.randint(0, 10)}
    return jsonify({"a": acceleration, "o": orientation})

if __name__ == "__main__":
    app.run()
