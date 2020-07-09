import json
import paho.mqtt.client as mqtt
import subprocess
import time


#starts local mqtt broker
brokerport = str(1882)
broker = subprocess.Popen("D:\Sciebo\STUDIUM\Bachelorarbeit\mosquitto\mosquitto -p "+brokerport, shell=False)
print("Broker on port "+brokerport+" started.")

data =[]
connected = 1

id ="1564654"
name="Michael"
location=[0,0]

def register():
    reg = {
        "driver_name": name,
        "location": location,
        "reasons": "None",
        "id": id
        }
    client_o.publish("/hshl/users/", json.dumps(reg))
    client_o.subscribe("/hshl/users/"+id+"/data",2)

def request(reasons):
    call = {
        "driver_name": name,
        "location": location,
        "reasons": reasons,
        "id": id
        }
    client_o.publish("/hshl/users/"+id, json.dumps(call))



#local client methods
def on_connect_local(client, userdata, flags, rc):
    print("Connected to localbroker with rc:"+str(rc))
    client_l.subscribe(("/car/temp", 2))
    client_l.subscribe(("/car/reason", 2))
    client_l.subscribe(("/car/gps", 2))

def on_message_local(client, userdata, msg):
    global location
    if str(msg.topic) == "/car/reason":

        request(msg.payload.decode())


    elif str(msg.topic) == "/car/gps":
        location = json.loads(msg.payload)

    else:
        print("new temperature"+msg.topic+" "+str(msg.payload))
        #store all incoming data FR A.1
        data.append(str(msg.payload))

#online client methods
def on_connect_online(client, userdata, flags, rc):
    global connected
    global id
    location
    print("Connected to onlinebroker with rc:"+str(rc))

    client_o.subscribe("/hshl/users/", 2)
    client_o.subscribe("/hshl/users/"+id,2)

    register()
    client_o.unsubcribe("/hshl/users/")

    #detect disconnections FRA
    if int(str(rc)) == 0:
        print("Connected to onlinebroker established")
        connected = 1
    else:
        print("connection to onlinebroker failed with rc:"+str(rc))
        connected = 0

def on_message_online(client, userdata, msg):
    if str(msg.topic) == "/hshl/users/"+id+"/data":
        js = json.loads(msg.payload)
        print("cardata from onlinebroker:")
        print(js)
        if js==data:
            data = []
    else:
        js = json.loads(msg.payload)
        print(js)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
        client.reconnect()



#initialise client for local broker
client_l = mqtt.Client()
client_l.on_connect = on_connect_local
client_l.on_message = on_message_local

#initialise client for online broker
client_o = mqtt.Client()
client_o.on_connect = on_connect_online
client_o.on_message = on_message_online
client_o.on_disconnect = on_disconnect
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
        #send collected data FR D
        client_o.publish("/hshl/users/"+id+"/data", json.dumps(data))
        time.sleep(8)
    else:
        print("no connection to onlinebroker")
        time.sleep(1)
