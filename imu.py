import socket
import time
# from sense_hat import SenseHat
import time
from datetime import datetime
import threading
import random as r
import math
import json
import argparse


def startup():
    global sense, sock, BUFFER_SIZE
    # sense = SenseHat()

    # Get groundstation IP
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", required=False)
    args, other = parser.parse_known_args()
    if (args.ip is not None):
        TCP_IP = args.ip
    else:
        TCP_IP = '127.0.0.1'

    TCP_PORT = 5005
    BUFFER_SIZE = 512
    MESSAGE = "Hello, World!"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))


def orientation():
    try:
        start = time.time()
        while True:
            # x, y, z = sense.get_accelerometer_raw().values()
            x = r.randint(0, 10)
            y = r.randint(0, 10)
            z = r.randint(0, 10)

            # o = sense.get_orientation()
            o = {"pitch": r.random()*math.pi*2, "roll": r.random() *
                 math.pi*2, "yaw": r.random()*math.pi*2}
            a = {"x": x, "y": y, "z": z}

            for k, v in o.items():
                o[k] = round(v, 2)
                o[k] = math.degrees(o[k])  # Convert to degrees
            for k, v in a.items():
                a[k] = round(v, 1)

            message = {"o": o, "a": a}

            sock.send(json.dumps(message).encode("utf-8"))
            confirmation = sock.recv(BUFFER_SIZE)
            now = time.time()
            time.sleep(.01)
    except KeyboardInterrupt:
        print("Operation complete.")
        # sense.clear()
        sock.close()
        exit(0)


if __name__ == "__main__":
    startup()
    thread = threading.Thread(target=orientation, args=(), daemon=True)
    thread.start()
    thread.join()
