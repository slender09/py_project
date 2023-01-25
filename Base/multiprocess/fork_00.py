#!/bin/python3
# -*- coding:utf-8 -*-

import time, os, sys

print("main process starting ......")

pid = os.fork()

if (pid == 0):
    print("I am child process %d, my parent is %d" %(os.getpid(), os.getppid()))
    os._exit(0)
else:
    print("I %d just creat a child process %d" %(os.getpid(), pid))
print("main process done")
sys.exit(0)

