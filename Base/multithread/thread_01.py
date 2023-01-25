#!/bin/python3
# -*- coding:utf-8 -*-

###no thread lock, threading share the same variable, can write at the same time, unexpect result

import threading, os, sys, time

balance = 0

def change_it(n):
    global balance
    #first in, last out
    balance += n
    balance -= n

def run_thread(n):
    for i in range(2000000):
        change_it(n)

if __name__ == "__main__":
    time1 = time.time()
    print("process %d start" %(os.getpid()))
    t1 = threading.Thread(target = run_thread, args = (5,))
    t2 = threading.Thread(target = run_thread, args = (9,))
    t1.start()
    print("thread %s start" %(threading.current_thread().name))
    t2.start()
    print("thread %s start" %(threading.current_thread().name))
    t1.join()
    t2.join()
    print(balance)
    print("process %d done" %(os.getpid()))
    time2 = time.time()
    print("run time %d" %(time2 - time1))
    sys.exit(0)
