from rx import Observable

source1 = Observable.from_(["tocho", "siberet", "mierder", "lingel"])
source2 = Observable.from_(["Miguel", "Rober", "Pietro", "Beltza Mari", "Moguer Pabler"])

Observable.merge(source1, source2) \
    .subscribe(lambda s: print(s))