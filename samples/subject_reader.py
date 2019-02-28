from rx.subjects import Subject
from rx import Observable

class Reader(Subject):
    def __init__(self, filename):
        super().__init__()
        self.disposable = None
        self.filename = filename
        file = open(filename, 'r')
        self.source = Observable.from_(file) \
            .map(lambda s: Observable.from_(s.split())) \
            .merge_all()
       
    def emit(self, word):
        self.on_next(word)
        
    def start(self):
        
        if not self.disposable:
            self.disposable =  Observable.create \
                .map(lambda s: self.source) \
                .subscribe(on_next=self.emit)                
    
    def stop(self):
        if self.disposable:
            self.disposable.dispose()
            self.disposable = None

def printword(word):
    print(word)
    
def example():
    reader = Reader("path/to/some/file.txt")
    reader.subscribe(on_next=printword)
    reader.start()
