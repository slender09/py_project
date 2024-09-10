#!/usr/bin/python3
# -*- coding:utf-8 -*-

from myModule import *


if (__name__=="__main__"):
    while True:
        num=eval(input("please enter a four bit num:"))
        if (num>=1000 and num<=9999):
            break
    if (isRoseNum(num) and not(isSymNum(num))):
        print("%d isRoseNum" %(num))
    elif (not(isRoseNum(num)) and isSymNum(num)):
        print("%d isSymNum" %(num))
    elif (isRoseNum(num) and isSymNum(num)):
        print("%d isSymNum and RoseNum" %(num))
    else:
        print("%d is not SymNum and RoseNum" %(num))

