import paho.mqtt.client as mqtt

class MqttClient():
    """An mqtt event client that connects to a broker"""
    def __init__(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        self.client = client
        client.connect("iot.eclipse.org")
        client.loop_start()

    def on_connect(self, client, userdat, flags, rc):
        print("Connected with result code " + str(rc))
