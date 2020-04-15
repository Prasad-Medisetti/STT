# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:56:22 2019
Topic: Closure and Decorator
@author: hp
"""

def outer(name):
    def inner(symbol):
        print(name.center(30,symbol))
    return inner


if __name__:
    fun = outer('Prasad')
    fun('*')