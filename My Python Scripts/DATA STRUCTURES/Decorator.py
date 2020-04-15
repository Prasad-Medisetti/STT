#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:59:31 2020

@author: prasadm

DATA STRUCTURES - LINKED LIST 
"""

#DECORATORS
#def outer():
#    def inner():
#        print("This is inner")
#    return inner
#
#n = outer()
#n()

# =========================================================================

#def outer(func):
#    def inner():
#        print('%'*10)
#        func()
#        print('#'*10)
#    return inner
#def myfunc():
#    print("STT")
#n = outer(myfunc)
#n()

# =========================================================================

#def outer(func):
#    def inner():
#        print('%'*10)
#        func()
#        print('#'*10)
#    return inner
#def myfunc():
#    print("STT")
#myfunc = outer(myfunc)
#myfunc()

# =========================================================================

#def outer(func):
#    def inner():
#        print('%'*10)
#        func()
#        print('#'*10)
#    return inner
#@outer
#def myfunc():
#    print("STT")
#myfunc()

# =========================================================================

#def outer(func):
#    def inner(name):
#        print('%'*10)
#        func(name)
#        print('#'*10)
#    return inner
#@outer
#def myfunc(n):
#    print(n)
#myfunc("STT, AEC")

# =========================================================================

#def outer(func):
#    def inner(*a,**b):
#        print('%'*10)
#        func(*a,**b)
#        print('#'*10)
#    return inner
#@outer
#def myfunc(n):
#    print(n)
#myfunc("STT, AEC")

# =========================================================================

def dec(s,n):
    def outer(func):
        def inner(*a,**b):
            print(s*n)
            func(*a,**b)
            print(s*n)
        return inner
    return outer
@dec('-',20)
def myfunc(n):
    print(n)
myfunc("STT, AEC")
