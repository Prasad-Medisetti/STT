# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:59:16 2019

@author: hp
"""

def Max(l):
    n = len(l)
    if n==1:
        return l[0]
    return max(l[-1], Max(l[:-1]))

def Min(l):
    n = len(l)
    if n==1:
        return l[0]
    return min(l[-1], Min(l[:-1]))

def OddSum(n):
    if n<=1:
        return 1
    elif n%1!=0:
        return n+OddSum(n-1)
    else:
        return OddSum(n-2)
    
def EvenSum(n):
    if n<=0:
        return 0
    else:
        if n&1:
            return (n-1)+EvenSum(n-2)
        else:
            return n+EvenSum(n-2)
def fen(n):
    if n==1:
        return 1
    else:
        return fen(n-1)+2*n-1

def Count(l,k):
    if len(l)==1:
        if l[0]==k:
            return 1
        else:
            return 0
    else:
        if l[-1]==k:
            return 1+Count(l[:-1],k)
        else:
            return Count(l[:-1],k)
        
def Bin(n):
    if n==0 or n==1:
        return str(n)
    else:
        return Bin(n//2)+str(n%2)
    
    
def Flattenl(l):
    if l == []:
        return l
    elif type(l[0])==list:
        return Flattenl(l[0])+Flattenl(l[1:])
    else:   
        return [l[0]]+Flattenl(l[1:])
    
def flatten(l):
    nl = []
    for x in l:
        if type(x)!=list:
            nl.append(x)
        else:
            nl.extend(flatten(x))
    return nl

def rtowers(n,ft,tt,at):
    if n==1:
        print('move %d disk from %s to %s using %s as helper tower'%(n,ft,tt,at))
    else:
        rtowers(n-1,ft,at,tt)
        print('move %d disk from %s to %s using %s as helper tower'%(n,ft,tt,at))
        rtowers(n-1,at,tt,ft)


