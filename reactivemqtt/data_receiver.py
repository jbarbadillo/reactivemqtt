from rx import Observable

class DataReceiver:
    def __init__(self, sources):
        Observable.from_(sources) \
            .merge_all() \
            .filter(lambda s: s[0] == "event/status" ) \
            .subscribe(self._on_event)
        Observable.from_(sources) \
            .merge_all() \
            .filter(lambda s: s[0] == "data/object") \
            .subscribe(self._on_object)
        Observable.from_(sources) \
            .merge_all() \
            .filter(lambda s: s[0] == "data/position") \
            .subscribe(self._on_position)

    def _on_event(self, data):
        print("event: {}".format( data[1]))

    def _on_object(self, data):
        print("object: {}".format( data[1]))

    def _on_position(self, data):
        print("position: {}".format( data[1]))