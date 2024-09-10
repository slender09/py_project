#!/usr/bin/python3
# -*- coding:utf-8 -*-

class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("name is %s, age is %d" %(self.name, self.age))

class student(people):
    def __init__(self, name, age, grand):
        people.__init__(self,name, age)
        self.grand = grand

    def say_hi(self):
        people.say_hi(self)
        print("grand is %d" %(self.grand))

s_0 = student("fxxk", 20, 3)
s_0.say_hi()
