#!/bin/python3
# -*- coding : utf-8 -*-

import os, sys
from multiprocessing import Process

def run_proc(name):
    print("Run child process %s (%d), his parent is %d" %(name, os.getpid(), os.getppid()))

if (__name__ == '__main__'):
    print("Parent process %d" %(os.getpid()))

    p = Process(target = run_proc, args = ('test',))

    print("Child process will start")

    p.start()

    p.join()

    print("Child process end")

    print("Parent process end")

    sys.exit(0)
