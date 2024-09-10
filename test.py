#! /bin/python3
# -*- coding:utf-8 -*-

import os

i = 0

print(f"I'm start parent, pid is {os.getpid()}, ppid is {os.getppid()}")

while ( i<6 ):
    pid = os.fork()
    if (pid == 0):
        break
    elif (pid < 0):
        print("fork error")
    i +=1
    print(i)
if (i<6):
    print("subprocess pid is %d, parent pid is %d" %(os.getpid(), os.getppid()))

if (i == 6):
    print(f"I'm parent process, pid is {os.getpid()}, ppid is {os.getppid()}")

