import paho.mqtt.client as mqtt
from random import *
import time
import sys
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(("/car/airbag", 2))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1882, 60)

client.loop_start()
while True:
    x = input("Something happend?\nha = heart attack\na = accident\naf = accident_fire\nao = accident_oil\nla = light_accident\nhard = hard_accident\np = police\nam = ambulance\nh = hospital\nn = None\n")
    #time.sleep(3)
    #if randint(0, 100) >50:
    #    client.publish("/car/airbag", "accident")
    if x == "ha":
        client.publish("/car/airbag", "heart_attack")
    elif x == "a":
        client.publish("/car/airbag", "accident")
    elif x == "af":
        client.publish("/car/airbag", "accident_fire")
    elif x == "ao":
        client.publish("/car/airbag", "accident_oil")
    elif x == "la":
        client.publish("/car/airbag", "light_accident")
    elif x == "hard":
        client.publish("/car/airbag", "hard_accident")
    elif x == "p":
        client.publish("/car/airbag", "police")
    elif x == "am":
        client.publish("/car/airbag", "ambulance")
    elif x == "h":
        client.publish("/car/airbag", "hospital")
    elif x == "n":
        client.publish("/car/airbag", "None")
