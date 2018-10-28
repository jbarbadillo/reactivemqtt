from rx import Observable

class Subscriber:
    def __init__(self, sources):
        Observable.from_(sources) \
            .merge_all() \
            .subscribe(lambda s: print(s))

