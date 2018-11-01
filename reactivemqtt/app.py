from time import sleep
from rx import Observable

from reactivemqtt.mqtt_client import MqttClient
from reactivemqtt.object_receiver import ObjectReceiver
from reactivemqtt.event_receiver import EventReceiver
from reactivemqtt.data_receiver import DataReceiver

def main():
    data_publisher = MqttClient()

    object_positions = Observable.create(ObjectReceiver).share()
    events = Observable.create(EventReceiver).share()

    DataReceiver([object_positions, events])


    data_publisher.client.publish("event/status", payload="start_tracking", qos=2)
    data_publisher.client.publish("data/position",payload="[1, (2,2,34)", qos=2)
    data_publisher.client.publish("data/object",payload="[1, car]", qos=2)
    data_publisher.client.publish("data/position", payload="[1, (2,2,37)", qos=2)
    data_publisher.client.publish("data/object", payload="[1, car]", qos=2)
    data_publisher.client.publish("data/position", payload="[2, (0,0,2)", qos=2)
    data_publisher.client.publish("data/object", payload="[2, person]", qos=2)
    sleep(1)
    data_publisher.client.publish("event/status", payload="stop_tracking", qos=2)

    sleep(1)

if __name__ == '__main__':
    main()