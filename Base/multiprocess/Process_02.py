#!/bin/python3
# -*- coding:utf-8 -*-

###process communication

import os, sys, time, random
from multiprocessing import Process, Queue

def producer(q):
    print("Process (%d) to write" %(os.getpid()))
    for value in range(10):
        print("Put %d to queue..." %(value))
        q.put(value)
        time.sleep(random.random())

def consumer(q):
    print("Process (%d) to read" %(os.getpid()))
    while True:
        value = q.get(True)
        print("Get %d from queue" %(value))

if (__name__ == "__main__"):
    print("parent process (%d) start" %(os.getpid()))
    q = Queue()
    pd = Process(target=producer, args = (q,))
    pc = Process(target=consumer, args = (q,))
    pd.start()
    pc.start()
    pd.join()
    pc.terminate()
    sys.exit(0)
