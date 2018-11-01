from rx import Observable

class DataReceiver:
    def __init__(self, sources):
        Observable.from_(sources) \
            .merge_all() \
            .filter(lambda s: s[0] == "event/status" ) \
            .subscribe(self._on_event)
        object_source = Observable.from_(sources) \
            .merge_all() \
            .filter(lambda s: s[0] == "data/object") \
            .map(lambda s: s[1])
        position_source = Observable.from_(sources) \
            .merge_all() \
            .filter(lambda s: s[0] == "data/position") \
            .map(lambda s: s[1])

        Observable.zip_array(object_source, position_source) \
            .subscribe(self._on_position)

    def _on_event(self, data):
        print("event: {}".format( data[1]))


    def _on_position(self, data):
        print("position: {}".format( data))