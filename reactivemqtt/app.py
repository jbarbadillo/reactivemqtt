from time import sleep

from reactivemqtt.data_client import DataClient
from reactivemqtt.subscriber_client import SubscriberClient

def main():
    data = DataClient()
    subs = SubscriberClient()

    data.client.publish("data/position",payload="[1, (2,2,34)", qos=2)
    data.client.publish("data/object",payload="[1, car]", qos=2)
    data.client.publish("data/position", payload="[1, (2,2,37)", qos=2)
    data.client.publish("data/object", payload="[1, car]", qos=2)
    data.client.publish("data/position", payload="[2, (0,0,2)", qos=2)
    data.client.publish("data/object", payload="[2, person]", qos=2)
    sleep(2)



if __name__ == '__main__':
    main()