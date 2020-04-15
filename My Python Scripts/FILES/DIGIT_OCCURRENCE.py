# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:55:43 2019

@author: hp
"""

def count2(n):
    c = 0
    for i in range(n+1):
        c += str(i).count('2')
    return c
if __name__=='__main__':
    n = int(input())
    print(count2(n))