#!/bin/python3
# -*- coding:utf-8 -*-

###threadlocal solve thread parameter/arguments transmit

import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print("hello, %s (in %s)" %(std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target = process_thread, args = ("zhangsan",), name = "thread_a")
t2 = threading.Thread(target = process_thread, args = ("lisi",), name = "thread_b")
t1.start()
t2.start()
t1.join()
t2.join()


