#!/bin/python3
# -*- coding:utf-8 -*-

import time, os, sys


def run_proc():
    while True:
        pass


if (__name__ == "__main__"):
    print("main process starting ......")
    
    i = 0
    while ( i < 4 ):
        pid = os.fork()
        if ( not pid ):
            break
        elif ( pid < 0 ):
            print("fork error")
        i += 1

    if ( i < 4 ):
        print(f"subprocess pid is {os.getpid()}, ppid is {os.getppid()}")
        run_proc()
    elif ( i == 4 ):
        print("parent process pid is %d" %(os.getpid()))
        os.wait()
        print("Done")
