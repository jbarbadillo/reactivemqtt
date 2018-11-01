from rx import Observable
from rx.concurrency import ThreadPoolScheduler
from threading import current_thread
import multiprocessing, time, random

def simulate_calculation(value):
    time.sleep(random.randint(5, 20)*0.1)
    return value

# task 1
Observable.from_(["one", "two", "three", "four", "five"]) \
    .map(lambda s: simulate_calculation(s)) \
    .subscribe(on_next=lambda s: print("thread {0}, value {1}".format(current_thread().name, s)),
               on_completed=lambda: print("finished task 1"))
# task 2
Observable.range(1,5) \
    .map(lambda s: simulate_calculation(s)) \
    .subscribe(on_next=lambda s: print("thread {0}, value {1}".format(current_thread().name, s)),
               on_completed=lambda: print("finished task 2"))

input("Press key to quit\nq")