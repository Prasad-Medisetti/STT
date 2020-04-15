# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:40:05 2019

@author: hp
"""
def rrev(s):
    l = len(s)
    if l==1:
        return s[0]
    else:
        return s[-1]+rrev(s[:-1])
    
def irev(s):
    r = ''
    for i in  range(-1,-len(s)-1,-1):
        r += s[i]
    return r

def Len(s):
    if s=='':
        return 0
    else:
        return 1+Len(s[1:])
    
#
#def rrev(s):
#    if len(s)==0:
#        return s
#    else:
#        return rrev(s[1:])+s[0]
        
if __name__=='__main__':
    ip = input()
    import timeit
    s = timeit.default_timer()
    print(irev(ip))
    e = timeit.default_timer()
    print(e-s)
    s = timeit.default_timer()
    print(rrev(ip))
    e = timeit.default_timer()
    print(e-s)