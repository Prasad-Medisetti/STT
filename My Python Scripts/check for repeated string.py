# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:56:45 2019

@author: hp
"""

# to check repeated string and print the string repeated else -1

s = input()
r = (s+s).find(s,1,-1)
out = -1 if r==-1 else s[:r]
print(out)