import paho.mqtt.client as mqtt

class DataClient():
    def __init__(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        self.client = client
        client.connect("test.mosquitto.org", 1883, 60)
        client.loop_start()
        return client

    def on_connect(self, client, userdat, flags, rc):
        print("Connected with result code " + str(rc))

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

