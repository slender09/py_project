#!/usr/bin/python3
# -*- coding:utf-8 -*-

from functools import reduce

listCh = ["12", "78", "-69", "108", "-2", "36", "5", "3", "-90", "8"]

listNum = list(map(int, listCh))

print("listNum is: ", listNum)

listCon23 = list(filter(lambda x: (x%2==0)and(x%3==0), listNum))

print("listCon23 is: ", listCon23)

list_sum = reduce(lambda x, y: x+y, listNum)

print("listNum sum is ", list_sum)

sorted_list = sorted(listNum, key=lambda x: abs(x))

print("After sorted: ", sorted_list)


