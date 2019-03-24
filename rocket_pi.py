import socket, time
from sense_hat import SenseHat
import time
from datetime import datetime
import threading
import random as r
import josn

def startup():
    global sense, sock
    sense = SenseHat()
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
            x, y, z = sense.get_accelerometer_raw().values()

            x = round(x, 0)
            y = round(y, 0)
            z = round(z, 0)

            print("x=%s, y=%s, z=%s" % (x, y, z))
            time.sleep(0.1)
            o = sense.get_orientation()
            pitch = o["pitch"]
            roll = o["roll"]
            yaw = o["yaw"]
            acceleration = {"x":x,"y":y,"z":z}
#            print("Pitch: {0:6.3f}".format(pitch), '\t', "Roll: {0:6.3f}".format(roll), '\t', "Yaw: {0:6.3f}".format(yaw))
            conn.send({"o":o,"a",a})
            now = time.time()
            time.sleep(.1)
    except KeyboardInterrupt:
        print("Operation complete.")
        sense.clear()
        exit(0)

if __name__ == "__main__":
    startup()
    t2 = threading.Thread(target=orientation, args=(), daemon=True)
    t2.start()
    t2.join()
