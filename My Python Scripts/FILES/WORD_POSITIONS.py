# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:56:30 2019

@author: hp
"""

def index(s,w):
    c = []
    s = s.split()
    for i in range(len(s)):
        if s[i]==w:
            c.append(i)
    return c
if __name__=='__main__':
    s = input()
    l = []
    for i in sorted(set(s.split())):
        l.append((i,index(s,i)))
    print(l)