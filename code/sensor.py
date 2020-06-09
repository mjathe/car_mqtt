import paho.mqtt.client as mqtt
from random import *
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(("hshl/car/sensor", 2))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1882, 60)

client.loop_start()
while True:
    time.sleep(3)
    client.publish("hshl/car/sensor", str(randint(0,100)))