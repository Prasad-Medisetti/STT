# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:38:29 2019

@author: hp
"""    
def rmp(p,n):
    if n==0:
        return 0
    else:
        r = -999999
        for x in range(1,len(p)+1):
            if n>=x:
                r = max(r,p[x-1]+rmp(p,n-x))
    return r

d = {0:0}
def tmp(p,n):
    if d.get(n)!=None:
        return d[n]
    if n==0:
        return 0
    else:
        r = -999999
        for x in range(1,len(p)+1):
            if n>=x:
                r = max(r,p[x-1]+tmp(p,n-x))
                d[n] = r
    return r


d = {0:0}
def bump(p,n):
    for j in range(1,n+1):
        r = -999999
        for x in range(1,len(p)+1):
            if j>=x:
                r = max(r,p[x-1]+d[j-x])
                d[j] = r
    return d[n]


if __name__=='__main__':
    from timeit import default_timer
    n = int(input())
    p = [1,5,8,9,10,17,17,20,24,30] 
    s = default_timer()
    print(bump(p,n))
    e = default_timer()
    print('Time: %f'%(e-s))