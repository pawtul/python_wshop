import multiprocessing
import time
from random import randint


def producer(pipe):
    print 'producer startuje'
    for i in range(5):
        time.sleep(0.5)
        x = randint(1, 5)
        print 'producer wyprodukowal: {}'.format(x)
        pipe.send(x)
    print 'producer konczy'


def consumer(pipe):
    print 'consumer startuje'
    while pipe.poll(3):
        x = pipe.recv()
        time.sleep(1.3)
        print 'consumer przetworzyl {}'.format(x)
    print 'consumer konczy'


koniec1, koniec2 = multiprocessing.Pipe()
prod = multiprocessing.Process(target=producer, args=(koniec1,))
cons = multiprocessing.Process(target=consumer, args=(koniec2,))

prod.start()
time.sleep(0.5)
cons.start()

prod.join()
cons.join()
