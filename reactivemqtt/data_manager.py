from rx import Observable

class DataManager:
    def __init__(self, sources):
        Observable.from_(sources) \
            .merge_all() \
            .subscribe(self._process_data)

    def _process_data(self, data):
        print("{}: {}".format(__name__, data))