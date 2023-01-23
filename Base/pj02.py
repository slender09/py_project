#!/bin/python3
# -*- coding : utf-8 -*-
import os, sys, time

#prime num

def cal_num(num):
    flag = 1
    if (num == 1):
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
if (__name__ == "__main__"):
    t1 = time.time()
    if (not os.path.exists("result")):
        os.mkdir("result")

    ###multiprocess invoke by os.fork()

    pid_0 = os.fork()
    pid_1 = os.fork()
    pid_2 = os.fork()

    if (pid_0 == 0):
        single_process(1, 100//4)
        os._exit(0)
    elif (pid_1 == 0):
        single_process(100//4, 100//2)
        os._exit(0)       
    elif (pid_2 == 0):
        single_process(100//2, 300//4)
        os._exit(0)
    else:
        single_process(300//4, 100)

    t2 = time.time()

    print("Run_time is %d" %(t2-t1))
    sys.exit(0)
