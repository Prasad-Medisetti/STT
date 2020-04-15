# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:57:10 2019

@author: hp

LIST 4
Given a list of integers and a number. Write a python function to find and returnthe sum of the elements of the list. 
Note: Don't add the given number and also the numbers present before and after the given number in the list
sample input1:
1,2,3,4
2
output
4
sample input2:
1,2,2,3,5,4,2,2,1,2
2
output:
5
sample input3:
1,2,1,2
2
output
0
"""

def fun(l,n):
    ln = len(l)
    s = 0
    for i in range(ln):
        if i==0 and l[i+1]!=n and l[0]!=n:
            s += l[0]
        elif i==ln-1 and l[i-1]!=n and l[i]!=n:
            s += l[i]
        elif l[i]!=n and l[i-1]!=n and l[i+1]!=n:
            s += l[i]
    return s

if __name__=='__main__':
    l = [int(x) for x in input().split(',')]
    n = int(input())
    print(fun(l,n))
