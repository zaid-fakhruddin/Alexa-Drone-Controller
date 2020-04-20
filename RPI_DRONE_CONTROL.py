#!/usr/bin/env python3


import socket
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient



host = "insert host url here" # your host url should go here
rootCAPath = "insert your root CA path here" # insert your rootCA path here
certificatePath = "insert your certificate path here" # insert your certificate path here
privateKeyPath = "insert your private key path" # insert your private key path here
port = 8883
clientId = "sdk-java"
topic = "insert your topic here"



myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Bind to the local address and port
def droneconnect():
    global tello_address
    global sock
    tello_address = ('192.168.10.1', 8889)
    local_address = ('YOUR IP ADDRESS', 9000) # insert your ip address here
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(local_address)
    print("droneconnect()")



# Send the message to Tello and allow for a delay in seconds
def send(message, delay):
  # Try to send the message otherwise print the exception
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))
    exit()

  # Delay for a user-defined period of time
  time.sleep(delay)

# Receive the message from Tello




# Publish to the same topic in a loop forever
loopCount = 0
while True:
    def customCallback(client, userdata, message):
        v = message.payload
        v = str(v, 'utf-8')
        v = v[13:17]
        if v == "conn":
            droneconnect()
            send("command", 4)
        elif v == "laun":
            send("command", 2)
            send("takeoff", 2)
        elif v == "back":
            send("back 30", 3)
        elif v == "left":
            send("left 30", 3)
        elif v == "righ":
            send("right 30", 3)
        elif v == "upup":
            send("up 30", 3)
        elif v == "down":
            send("down 30", 4)
        elif v == "emer":
            send("command", 3)
            send("emergency", 3)
        elif v == "land":
            send("command", 2)
            send("land", 2)
        elif v == "forw":
            send("forward 70", 3)
        elif v == "flip":
            send("flip f", 3)
        elif v == "stop":
            sock.close()
            print("stopped")
        else:
            print("no command given")
    myAWSIoTMQTTClient.connect()
    myAWSIoTMQTTClient.subscribe("myTopic", 1, customCallback)



    time.sleep(1000000)