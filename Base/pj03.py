#!/bin/python3
# -*- coding:utf-8 -*-

import os
import time, sys

def my_print(string):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)

if (__name__ == "__main__"):
    print("Beginning...")

    time.sleep(5)

    pid_0 = os.fork()

    if (pid_0 == 0):
        my_print("sounds\n")
        time.sleep(1)
        my_print("test\n")
        os._exit(0)
    else:
        my_print("video\n")
    
    print("Done")
    sys.exit(0)    


