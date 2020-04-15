# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:54:57 2019

@author: hp
"""

def wellform(l,label):
    if type(l)==list and len(l)>=2 and l[0] in label:
        if type(l[1])==list:
            return wellform(l[1],label)
        elif type(l[1])==str:
            return True
        else:
            return False
    else:
        return False
if __name__=='__main__':
    l = eval(input())
    label = eval(input())
    print(wellform(l,label))