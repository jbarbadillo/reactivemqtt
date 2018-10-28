from time import sleep
from rx import Observable

from reactivemqtt.data_client import DataClient
from reactivemqtt.object_pos_client import ObjectPosClient

def main():
    data = DataClient()
    observer = Observable.create(ObjectPosClient).share()
    observer.subscribe(lambda s: print(s))

    data.client.publish("data/position",payload="[1, (2,2,34)", qos=2)
    data.client.publish("data/object",payload="[1, car]", qos=2)
    data.client.publish("data/position", payload="[1, (2,2,37)", qos=2)
    data.client.publish("data/object", payload="[1, car]", qos=2)
    data.client.publish("data/position", payload="[2, (0,0,2)", qos=2)
    data.client.publish("data/object", payload="[2, person]", qos=2)
    sleep(2)



if __name__ == '__main__':
    main()