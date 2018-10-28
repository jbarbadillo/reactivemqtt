from rx import Observable

source1 = Observable.interval(1000).map(lambda s: "Source 1: {0}".format(s))
source2 = Observable.interval(500).map(lambda s: "Source 2: {0}".format(s))
source3 = Observable.interval(2000).map(lambda s: "Source 3: {0}".format(s))

Observable.merge(source1, source2, source3) \
    .subscribe(lambda s: print(s))

input("Press key to quit\nq")