import json
import paho.mqtt.client as mqtt
import subprocess
import time


#starts local mqtt broker
brokerport = str(1882)
broker = subprocess.Popen("D:\Sciebo\STUDIUM\Bachelorarbeit\mosquitto\mosquitto -p "+brokerport, shell=False)
print("Broker auf port "+brokerport+" gestartet.")


connected =0

data =[]

#local client methods
def on_connect_local(client, userdata, flags, rc):
    print("Connected to localbroker with rc:"+str(rc))
    client_l.subscribe(("hshl/car/sensor", 2))

def on_message_local(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    data.append(str(msg.payload))

#online client methods
def on_connect_online(client, userdata, flags, rc):
    global connected
    client_o.subscribe(("hshl/car", 2))
    if int(str(rc)) == 0:
        print("Connected to onlinebroker established")
        connected = 1
    else:
        print("Connected to onlinebroker failed with rc:"+str(rc))
        connected = 0

def on_message_online(client, userdata, msg):
    js = json.loads(msg.payload)
    print(js)

#initialise client for local broker
client_l = mqtt.Client()
client_l.on_connect = on_connect_local
client_l.on_message = on_message_local

#initialise client for online broker
client_o = mqtt.Client()
client_o.on_connect = on_connect_online
client_o.on_message = on_message_online
client_o.username_pw_set("solace-cloud-client", "nbsse0pkvpkvhpeh3ll5j7rpha")

#connect to local brokers
client_l.connect("localhost", 1882, 60)
#connect to online broker
client_o.connect("mr2mbqbl71a4vf.messaging.solace.cloud", 20614, 60)
#start client loops
client_l.loop_start()
client_o.loop_start()
while True:
    if connected:
        client_o.publish("hshl/car", json.dumps(data))
        data = []
        time.sleep(8)
    else:
        print("no connection to onlinebroker")
        time.sleep(1)
