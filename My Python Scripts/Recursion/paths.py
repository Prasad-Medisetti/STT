# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:08:00 2019

@author: hp
"""

def rpaths(i,j):
    if i==0 and i==0:
        return 1
    elif i==0:
        return rpaths(0, j-1)
    elif j==0:
        return rpaths(i-1 ,0)
    elif i==4 and j==4:
        return 0
    else:
        return rpaths(i-1, j)+rpaths(i, j-1)
    
def btrpaths(i,j):
    d = {}
    d[(0,0)] = 1
    for c in range(1, j+1):
        d[(0, c)] = 1
    for r in range(1, j+1):
        d[(r, 0)] = 1
    for r in range(1, i+1):
        for c in range(1, j+1):
            d[(r, c)] = d[(r-1, c)]+d[(r, c-1)]
    return d[(i, j)]

d = {}
d[(0,0)] = 1
def tdrpaths(i,j):
    if d.get((i,j),-1)!=-1:
        return d[(i,j)]
    elif i==0:
        return rpaths(0, j-1)
    elif j==0:
        return rpaths(i-1 ,0)
    else:
        d[(i,j)]=tdrpaths(i-1,j)+tdrpaths(i,j-1)
        return d[(i,j)]
    
    