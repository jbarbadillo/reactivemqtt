from rx.subjects import Subject
from rx import Observable
import re

class Reader(Subject):
    def __init__(self, filename):
        super().__init__()
        self.disposable = None
        self.filename = filename
        file = open(filename, 'r')
        self.source = Observable.from_(file) \
            .map(lambda s: Observable.from_(s.split())) \
            .concat_all() \
            .map(lambda w: re.sub(r'[^\w\s]','', w)) \
            .map(lambda s: s.lower())
       
    def emit(self, word):
        self.on_next(word)
        
    def start(self):
        
        if not self.disposable:
            self.disposable =  self.source \
                .subscribe(on_next=self.emit)                
    
    def stop(self):
        if self.disposable:
            self.disposable.dispose()
            self.disposable = None

def printword(word):
    print(word)
    
def example():
    """
    Example output
    ojete
    calor
    muy
    rico
    no
    se
    ...
    
    """
    reader = Reader("samples/data/some_text.txt")
    reader.subscribe(on_next=printword)
    reader.start()

if __name__ == "__main__":
    example()
