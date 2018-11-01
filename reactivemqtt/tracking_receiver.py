import paho.mqtt.client as mqtt


class TrackingReceiver():
    """
        mqtt client that receives tracking status
    """
    def __init__(self, observer):
        self.observer = observer
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.message_callback_add("tracking/status", self.on_event)

        self.client = client
        client.connect("iot.eclipse.org")
        client.loop_start()

    def on_connect(self, client, userdat, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe("tracking/status", qos=2)


    def on_event(self, client, userdata, msg):
        self.observer.on_next([msg.topic, msg.payload.decode("utf-8")])

