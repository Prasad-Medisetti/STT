# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:54:13 2019

@author: hp
"""

def fl(l):
    j = -1
    m = max(l)
    i = l.index(m)
    for v in range(len(l)-1,-1,-1):
        if l[v]==m:
            break
    return (i,v)
if __name__=='__main__':
    l = eval(input())
    print(fl(l))