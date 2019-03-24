import socket, time
#from sense_hat import SenseHat
import time
from datetime import datetime
import threading
import random as r
import math
import json

def startup():
    global sense, sock
#    sense = SenseHat()
    TCP_IP = '127.0.0.1' #Need to change to IP of groundstation
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    MESSAGE = "Hello, World!"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))

def orientation():
    try:
        start = time.time()
        while True:
#            x, y, z = sense.get_accelerometer_raw().values()
            x = r.randint(0,10);
            y = r.randint(0,10);
            z = r.randint(0,10);

            x = round(x, 0)
            y = round(y, 0)
            z = round(z, 0)

#            print("x=%s, y=%s, z=%s" % (x, y, z))
#            o = sense.get_orientation()
            o = {"pitch": r.random()*math.pi*2, "roll": r.random()*math.pi*2, "yaw": r.random()*math.pi*2}
            pitch = o["pitch"]
            roll = o["roll"]
            yaw = o["yaw"]
            a = {"x":x,"y":y,"z":z}
#            print("Pitch: {0:6.3f}".format(pitch), '\t', "Roll: {0:6.3f}".format(roll), '\t', "Yaw: {0:6.3f}".format(yaw))
            message = {"o":o,"a":a}
            sock.send(json.dumps(message).encode("utf-8"))
            confirmation = sock.recv(1024)
            now = time.time()
    except KeyboardInterrupt:
        print("Operation complete.")
#        sense.clear()
        sock.close()
        exit(0)

if __name__ == "__main__":
    startup()
    t2 = threading.Thread(target=orientation, args=(), daemon=True)
    t2.start()
    t2.join()
