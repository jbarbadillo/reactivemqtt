from time import sleep
from rx import Observable

from reactivemqtt.data_client import DataClient
from reactivemqtt.object_pos_client import ObjectPosClient
from reactivemqtt.event_client import EventClient
from reactivemqtt.data_manager import DataManager

def main():
    data = DataClient()

    object_positions = Observable.create(ObjectPosClient).share()
    events = Observable.create(EventClient).share()

    DataManager([object_positions, events])


    data.client.publish("event/status", payload="start_tracking", qos=2)
    data.client.publish("data/position",payload="[1, (2,2,34)", qos=2)
    data.client.publish("data/object",payload="[1, car]", qos=2)
    data.client.publish("data/position", payload="[1, (2,2,37)", qos=2)
    data.client.publish("data/object", payload="[1, car]", qos=2)
    data.client.publish("data/position", payload="[2, (0,0,2)", qos=2)
    data.client.publish("data/object", payload="[2, person]", qos=2)
    sleep(1)
    data.client.publish("event/status", payload="stop_tracking", qos=2)

    sleep(1)

if __name__ == '__main__':
    main()