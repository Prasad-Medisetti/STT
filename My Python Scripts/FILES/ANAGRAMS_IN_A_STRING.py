# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:55:26 2019

@author: hp
"""

from itertools import combinations
def CS(s,w):
    return len(list(combinations(w,len(w)))[0])
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        s = input()
        w = input()
        print(CS(s,w))