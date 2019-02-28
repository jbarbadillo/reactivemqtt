from rx.subjects import Subject
from rx import Observable

class Reader(Subject):
    def __init__(self, filename):
        super().__init__()
        self.disposable = None
        self.filename = filename
        self.source = Observable.from_(file) \
            .map(lambda s: Observable.from_(s.split())) \
            .merge_all()
       
    def emit(self, word):
        self.on_next(word)
        
    def start(self):
        fp = open(filename, 'r')
        if not self.disposable:
            self.disposable =  Observable.interval(1000) \
                .map(lambda s: self.source) \
                .subscribe(on_next=self.emit)                
    
    def stop(self):
        if self.disposable:
            self.disposable.dispose()
            self.disposable = None
