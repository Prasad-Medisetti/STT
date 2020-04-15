# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:25:45 2019

@author: hp
"""

def fibonacci(n):
    l = [0,1]
    for i in range(n):
        l.append(l[i]+l[i+1])
    print(l[n-1])
        
if __name__=='__main__':
    import timeit
    s = timeit.default_timer()
    fibonacci(int(input()))
    e = timeit.default_timer()
    print(e-s)