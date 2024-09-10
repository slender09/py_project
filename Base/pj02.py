#!/bin/python3
# -*- coding:utf-8 -*-
import os, sys, time

#prime num
def cal_num(num):
    flag = 1
    if ((num == 1) or (num == 0)):
        flag = 0
    elif (num ==2):
        flag = 1
    else:
        for i in range(2, num):
            if (num % i == 0):
                flag = 0
                break
            else:
                flag = 1
    if (flag):
        return "%d is prime num" %(num)
    else:
        return "%d is not prime num" %(num)

def save_res(f_name, res):
    with open(f_name, "w") as f:
        f.write(res)

def single_process(x, y):
    for i in range(x, y):
        res = cal_num(i)
        f_name = os.path.join("result", "is_prime_num_"+str(i))
        save_res(f_name, res)
        time.sleep(0.5)

if ( __name__ == "__main__" ):
    t1 = time.time()
    print("start main process pid is %d, ppid is %d" %(os.getpid(), os.getppid()))
    if (not os.path.exists("result")):
        os.mkdir("result")
    #creat 4 subprocess
    i = 0
    while ( i < 4 ):
        pid = os.fork()
        if ( pid == 0 ):
            break
        elif ( pid < 0 ):
            print("fork error")
        i += 1

    for n in range(4):
        if ( i == n ):
            print(f"allot task {n} to subprocess({i}), pid is {os.getpid()}, parent pid is {os.getppid()}")
            single_process(i*25, (i+1)*25)
            break
    if (i == 4):
        print(f"main process {os.getpid()} is over")
        os.wait()
        t2 = time.time()
        print("Run_time is %d" %(t2-t1))
        sys.exit(0)
