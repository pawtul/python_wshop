import multiprocessing
import time
from random import randint


def producer(queue):
    print('producer startuje')
    for i in range(5):
        time.sleep(0.5)
        x = randint(1, 5)
        print('producer wyprodukowal: {}'.format(x))
        queue.put(x)
    print('producer konczy')


def consumer(queue):
    print('consumer startuje')
    while not queue.empty():
        x = queue.get()
        # time.sleep(1.3)
        time.sleep(0.3)
        print('consumer przetworzyl {}'.format(x))
    print('consumer konczy')


queue = multiprocessing.Queue()
prod = multiprocessing.Process(target=producer, args=(queue,))
cons = multiprocessing.Process(target=consumer, args=(queue,))

prod.start()
time.sleep(0.5)
cons.start()

prod.join()
cons.join()
print('koniec programu')
