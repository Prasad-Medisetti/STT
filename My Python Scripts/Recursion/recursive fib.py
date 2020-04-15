# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:07:40 2019

@author: hp

topic : Dynamic Programming
"""

def rfib(n):
    if n==0 or n==1:
        return n
    else:
        return rfib(n-1)+rfib(n-2)

def btfib(n):
    d = {}
    d[0], d[1] = 0, 1
    for i in range(2,n+1):
        d[i] = d[i-1]+d[i-2]
    return d[n]
        
def tdfib(n):
    d = {}
    d[0], d[1] = 0, 1
    if d.get(n, -1)!=-1:
        return d[n]
    else:
        d[n] = tdfib(n-1)+tdfib(n-2)
        return d[n]
    
if __name__=='__main__':
    from timeit import default_timer
    n = int(input())
    s = default_timer()
    print(tdfib(n))
    e = default_timer()
    print('Time: %fs'%(e-s))