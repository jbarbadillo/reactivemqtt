import paho.mqtt.client as mqtt


class SubscriberClient():
    def __init__(self, observer):
        self.observer = observer
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.message_callback_add("data/position", self.on_position)
        client.message_callback_add("data/object", self.on_object)

        self.client = client
        client.connect("iot.eclipse.org")
        client.loop_start()

    def on_connect(self, client, userdat, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe("data/position", qos=2)
        self.client.subscribe("data/object", qos=2)

    def on_position(self, client, userdata, msg):
        # print("position received")
        self.observer.on_next(msg.payload)
        # print(msg.topic + " " + str(msg.payload))

    def on_object(self, client, userdata, msg):
        # print("object received")
        self.observer.on_next(msg.payload)
        # print(msg.topic + " " + str(msg.payload))

