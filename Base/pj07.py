#!/bin/python3
# -*- coding:utf-8 -*-

import time
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("call %s" %(func.__name__))
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print("%s executed in %0.2f s" %(func.__name__, t2 - t1))
        return f
    return wrapper

@decorator
def proc(n):
    for i in range(n):
        time.sleep(1)
        print(i)




