# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:11:52 2019

@author: hp
"""
def ifact(n):
    fact = 1
    for i in range(n,1,-1):
        fact *= i
    return fact

def rfact(n):
    if n==0:
        return 1
    else:
        return n*rfact(n-1)
    
if __name__=='__main__':
    import timeit
    n = int(input())
    start = timeit.default_timer()
    ifact(n)
    end = timeit.default_timer()    
    print('Time Tsken in Seconds :', end-start)
    start1 = timeit.default_timer()
    rfact(n)
    end1 = timeit.default_timer()
    print('Time Tsken in Seconds :', end1-start1)