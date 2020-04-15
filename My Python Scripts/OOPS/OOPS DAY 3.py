#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:42:43 2020

@author: prasadm
"""

#class Temp:
#    def __init__(self,a,b):
#        self.a = a
#        self.b = b
#    def show(self):
#        print(self.a,self.b)
#    @classmethod #decorator
#    def con(cls,a,b=23):
#        return Temp(a,b) #cls(a,b)
##    def con(cls,a,b=23):
##        return Temp(a,b)
##    con = classmethod(con)
#    @staticmethod
#    def m():
#        print('I am m()')


#class Temp:
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#    def show(self):
#        print(self.name,self.age)
#    @staticmethod
#    def m(age):
#        return age>=18
#    def canvote(self):
#        return self.m(self.age)

class classA:
    __p = 200
    def __init__(self):
        self.__p = 100
        def 