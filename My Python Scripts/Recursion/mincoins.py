# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:24:00 2019
@author: hp

minimum no.of coins
"""

from sys import maxsize
def rch(v,l):
    if v==0:
        return 0
    else:
        r = maxsize
        for x in l:
            if x<=v:
                r = min(r,1+rch(v-x,l))
    return r

d = {0:0}
def tch(v,l):
    if d.get(v,-1)!=-1:
        return d[v]
    if v==0:
        r = 0
    else:
        r = maxsize
        for x in l:
            if x<=v:
                r = min(r,1+rch(v-x,l))
    d[v] = r
    return r

bu = {0:0}
def buch(v,l):
    for i in range(1,v+1):
        bu[i] = maxsize
    for value in range(1,v+1):
        for x in l:
            if x<=value:
                s = bu[value-x]
                if s+1<bu[value]:
                    bu[value] = s+1
    return bu[v]
                

def mincoins(v,l):
    if v==0:
        return 0
    else:
        return min([1+mincoins(v-i,l) for i in l])
    
if __name__=='__main__':
    from timeit import default_timer
    v = int(input())
    l = eval(input())
    s = default_timer()
    print(tch(v,l))
    e = default_timer()
    print('Time: %fs'%(e-s))