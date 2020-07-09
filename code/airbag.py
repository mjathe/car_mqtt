import paho.mqtt.client as mqtt
from random import *
import time
import sys
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(("/car/reason", 2))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1882, 60)

client.loop_start()
while True:
    x = input("Something happend?\nha = heart attack\na = accident\naf = accident_fire\nao = accident_oil\nla = light_accident\nhard = hard_accident\np = police\nam = ambulance\nh = hospital\nn = None\n")

    if x == "ha":
        client.publish("/car/reason", "heart_attack")
    elif x == "a":
        client.publish("/car/reason", "accident")
    elif x == "af":
        client.publish("/car/reason", "accident_fire")
    elif x == "ao":
        client.publish("/car/reason", "accident_oil")
    elif x == "la":
        client.publish("/car/reason", "light_accident")
    elif x == "hard":
        client.publish("/car/reason", "hard_accident")
    elif x == "p":
        client.publish("/car/reason", "police")
    elif x == "am":
        client.publish("/car/reason", "ambulance")
    elif x == "h":
        client.publish("/car/reason", "hospital")
    elif x == "n":
        client.publish("/car/reason", "None")
