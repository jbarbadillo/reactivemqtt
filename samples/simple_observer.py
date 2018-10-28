from rx import Observable, Observer

letters = Observable.from_(["tocho", "tochez", "tochisimo", "tochine"])

class MySubscriber(Observer):
    def on_next(self, value):
        print(value)

    def on_completed(self):
        print("done")

    def on_error(self, error):
        print(error)


letters.subscribe(MySubscriber())

# The same for
letters.subscribe(on_next=lambda s: print(s),
  		          on_completed=lambda: print("done"),
                  on_error=lambda e: print(e))