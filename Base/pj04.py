#!/bin/python3
# -*- coding:utf-8 -*-
import os, sys, time
import threading
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
    time1 = time.time()
    if (not os.path.exists("result")):
        os.mkdir("result")

    ###multithreading
    t1 = threading.Thread(target = single_process, args = (1, 100//4))
    t2 = threading.Thread(target = single_process, args = (100//4, 100//2))
    t3 = threading.Thread(target = single_process, args = (100//2, 300//4))
    t4 = threading.Thread(target = single_process, args = (300//4, 10))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    time2 = time.time()
    print("Run_time is %d" %(time2-time1))
    sys.exit(0)
