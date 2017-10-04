import multiprocessing
import time

def daemon_child():
    time.sleep(1)
    open('daemon-child-log', 'w').close()


def daemon():
    child = multiprocessing.Process(target=daemon_child)
    child.daemon = True
    child.start()
    time.sleep(2)
    open('daemon-log', 'w').close()
    print("running function f")


proc = multiprocessing.Process(target=daemon)
proc.daemon = True
proc.start()
time.sleep(0.1)

