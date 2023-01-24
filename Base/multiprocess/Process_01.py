#!/bin/python3
# -*- coding : utf-8 -*-

import os, sys, time, random
from multiprocessing import Pool

def long_time_task(name):
    print("Run task %s (%d), it parent process %d" %(name, os.getpid(), os.getppid()))
    t1 = time.time()
    time.sleep(random.random() * 3)
    t2 = time.time()
    print("Task %s runs %0.2f seconds" %(name, (t2-t1)))

if (__name__ == '__main__'):
    print("Parent process (%d) start" %(os.getpid()))
    p = Pool(3)
    for i in range(9):
        p.apply_async(long_time_task, args = (i,))
    print("Waiting for all subprocesses done.....")
    p.close()
    p.join()
    print("All subprocesses done")
    sys.exit(0)
    

