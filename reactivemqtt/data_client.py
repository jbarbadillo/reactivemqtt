import paho.mqtt.client as mqtt

class DataClient():
    def __init__(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        self.client = client
        client.connect("iot.eclipse.org")
        client.loop_start()

    def on_connect(self, client, userdat, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe("message", qos=2)

    def on_message(self, client, userdata, msg):
        print("received")
        print(msg.topic + " " + str(msg.payload))

