#!/bin/python3
# -*- coding:utf-8 -*-

###multithread

import os, sys, time
import threading

def loop():
    print("thread %s is running..." %(threading.current_thread().name))
    n = 0
    while (n < 5):
        print("thread %s >>> %d" %(threading.current_thread().name, n))
        n += 1
        time.sleep(1)
    print("thread %s is ended" %(threading.current_thread().name))

if __name__ == '__main__':
    print("Thread %s is running..." %(threading.current_thread().name))
    t = threading.Thread(target = loop, name = 'LoopThread')
    t.start()
    t.join()
    print("thread %s ended..." %(threading.current_thread().name))
    sys.exit(0)
