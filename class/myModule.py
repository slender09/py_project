#!/usr/bin/python3
# -*- coding:utf-8 -*-

def isRoseNum(x):
    if (x == (x//1000)**4+(x%1000//100)**4+(x%1000%100//10)**4+(x%1000%100%10)**4):
        return True
    else:
        return False

def isSymNum(x):
    if ((x//1000)==(x%1000%100%10) and (x%1000//100)==(x%1000%100//10)):
        return True
    else:
        return False

