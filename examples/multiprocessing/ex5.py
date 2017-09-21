import multiprocessing
import time
import Queue
from random import randint


def producer(queue):
    print 'producer startuje'
    for i in range(5):
        time.sleep(0.5)
        x = randint(1, 5)
        print 'producer wyprodukowal: {}'.format(x)
        queue.put(x)
        queue.join()
    print 'producer konczy'


def consumer(queue):
    print 'consumer startuje'
    while True:
        try:
            x = queue.get(timeout=2)
        except Queue.Empty:
            break
        time.sleep(1.3)
        queue.task_done()
        print 'consumer przetworzyl {}'.format(x)
    print 'consumer konczy'


queue = multiprocessing.JoinableQueue()
prod = multiprocessing.Process(target=producer, args=(queue,))
cons = multiprocessing.Process(target=consumer, args=(queue,))

prod.start()
time.sleep(0.5)
cons.start()

prod.join()
cons.join()
print 'koniec programu'

