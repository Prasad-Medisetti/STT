# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:54:35 2019

@author: hp
"""

def delsubstr(s,substr):
    while substr in s:
        i = s.index(substr)
        s = s[:i]+s[i+len(substr):]
    if s=='':
        return True
    else:
        return False
if __name__=='__main__':
    s = input()
    substr = input()
    print(delsubstr(s,substr))