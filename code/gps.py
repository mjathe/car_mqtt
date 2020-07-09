import paho.mqtt.client as mqtt
from random import *
import time
import sys
import math
import json
alpha = 0
radius = 1
locations = [
[51.671469, 8.348558],
[51.671971, 8.348655],
[51.672487, 8.348778],
[51.673013, 8.348912],
[51.673434, 8.348990],
[51.674019, 8.349097],
[51.674491, 8.349194],
[51.675050, 8.349274],
[51.675702, 8.349360],
[51.676124, 8.348577],
[51.676124, 8.348577],
[51.676240, 8.346635],
[51.676237, 8.345589],
[51.676254, 8.344446],
[51.676168, 8.343657],
[51.675962, 8.342407],
[51.675413, 8.342702],
[51.674934, 8.342938],
[51.674398, 8.343035],
[51.673703, 8.343148],
[51.672994, 8.343239],[51.672369, 8.343432],[51.671764, 8.343362],[51.671325, 8.343378],[51.671023, 8.344865],[51.670790, 8.345884],[51.670837, 8.347365],[51.671020, 8.348352]]
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(("/car/gps", 2))

def on_message(client, userdata, msg):
    print(json.loads(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1882, 60)

client.loop_start()
while True:

    for l in locations:
        client.publish("/car/gps", json.dumps(l))
        time.sleep(10)
