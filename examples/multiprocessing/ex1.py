import multiprocessing
import time

def f():
    time.sleep(1)
    print "running function f"


proc = multiprocessing.Process(target=f)
proc.start()
proc.join()

