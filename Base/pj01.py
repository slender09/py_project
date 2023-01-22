#!/bin/python3
#-*- coding : utf-8 -*-

def even_num(x):
    if (x % 2 == 0):
        print("%d is a even number" %(x))
    else:
        print(x, "is a odd")

if (__name__ == "__main__"):
    for i in range(0, 101):
        even_num(i)
