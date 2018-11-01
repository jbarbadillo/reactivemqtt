from rx import Observable
from rx.concurrency import ThreadPoolScheduler
from threading import current_thread
import multiprocessing, time, random

def simulate_calculation(value):
    time.sleep(random.randint(5, 20)*0.1)
    return value

optimal_threads = multiprocessing.cpu_count() + 1
pool_scheduler = ThreadPoolScheduler(optimal_threads)

print("using {0} thread pool".format(optimal_threads))
# task 1, process multiple emissions at a time
Observable.from_(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]) \
    .flat_map(lambda s:
              Observable.just(s) \
              .subscribe_on(pool_scheduler) \
              .map(lambda s: simulate_calculation(s))
    ).subscribe(on_next=lambda s: print("thread {0}, value {1}".format(current_thread().name, s)),
               on_completed=lambda: print("finished task 1"))

input("Press key to quit\n")