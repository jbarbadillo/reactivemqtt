"""
A simple application that shows how different mqtt clients can subscribe on the same observer using rxpy
in order to receive data reactively.
"""
from time import sleep
from rx import Observable

from reactivemqtt.mqtt_client import MqttClient
from reactivemqtt.object_receiver import ObjectReceiver
from reactivemqtt.tracking_receiver import TrackingReceiver
from reactivemqtt.event_subscriber import EventSubscriber

def main():
    event_publisher = MqttClient()

    object_positions = Observable.create(ObjectReceiver).share()
    events = Observable.create(TrackingReceiver).share()

    EventSubscriber([object_positions, events])


    event_publisher.client.publish("tracking/status", payload="start_tracking", qos=2)
    event_publisher.client.publish("data/position",payload="[1, (2,2,34)", qos=2)
    event_publisher.client.publish("data/object",payload="[1, car]", qos=2)
    event_publisher.client.publish("data/position", payload="[1, (2,2,37)", qos=2)
    event_publisher.client.publish("data/object", payload="[1, car]", qos=2)
    event_publisher.client.publish("data/position", payload="[2, (0,0,2)", qos=2)
    event_publisher.client.publish("data/object", payload="[2, person]", qos=2)
    sleep(1)
    event_publisher.client.publish("tracking/status", payload="stop_tracking", qos=2)

    sleep(1)

if __name__ == '__main__':
    main()