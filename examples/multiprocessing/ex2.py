import multiprocessing
import time

def f():
    time.sleep(1)
    open('daemon-log', 'w').close()
    print("running function f")


proc = multiprocessing.Process(target=f)
proc.daemon = True
proc.start()
# proc.join()  # dodanie join oczekuje na zakończenie daemona

