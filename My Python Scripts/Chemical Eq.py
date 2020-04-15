# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:51:14 2020

@author: hp
"""

'''
You are given a chemical equation of the following format:

    (b1)Cx + (b2)Hy -----> (b3)CpHq

Your task is to calculate the balancing factor b1, b2, b3 


'''


def solve(x,y,p,q):
    # solved = False
    # r = range(1,100)
    # while solved!=True:
    #     for b1 in r:
    #         for b2 in r:
    #             for b3 in r:
    #                 if b1*x==b3*p and b2*y==b3*q and solved==False:
    #                     solved = True
    #                     print(b1,b2,b3)
    i = 1
    while True:
        if (i*p)%x==0 and (i*q)%y==0:
            b1 = (i*p)//x
            b2 = (i*q)//y
            b3 = i
            # print(i*p,i*q)
            break
        i += 1
    return (b1,b2,b3)
            
if __name__=='__main__':
    import timeit
    x, y, p, q = [int(val) for val in input().split()]
    s = timeit.default_timer()
    print(*solve(x,y,p,q))
    e = timeit.default_timer()
    print("%f"%(e-s))
