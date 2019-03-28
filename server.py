from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import random
import math
import socket
import json
import time
import argparse

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 512  # Can make this lower if we need speed

app = Flask("__name__", static_folder="assets")
# Prevent CORS errors
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def data():
    sock_data = conn.recv(BUFFER_SIZE)
    print(sock_data)
    sock_data = json.loads(sock_data.decode("utf-8"))
    # {"pitch": random.random()*math.pi*2, "roll": random.random()*math.pi*2, "yaw": random.random()*math.pi*2}
    orientation = sock_data["o"]
    # {"x": random.randint(0, 10), "y": random.randint(0, 10), "z": random.randint(0, 10)}
    acceleration = sock_data["a"]
    conn.send("Data Received".encode('utf-8'))
    return jsonify({"a": acceleration, "o": orientation})


if __name__ == "__main__":
    # Get groundstation IP
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", required=False)
    args, other = parser.parse_known_args()
    if (args.ip is not None):
        TCP_IP = args.ip
    else:
        TCP_IP = '127.0.0.1'
    print("IP:", TCP_IP)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((TCP_IP, TCP_PORT))
    sock.listen(1)

    conn, addr = sock.accept()

    app.run()
