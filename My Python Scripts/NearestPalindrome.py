# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:31:50 2019

@author: hp
"""

'''Nearest Palindrome'''

n = input()
s = ''
if len(n)==1:
    s += n
elif len(n)%2==0:
    s = n[:len(n)//2+1]
    s += n[len(n)//2-1::-1]
elif len(n)%2==1:
    s = n[:len(n)//2+1]
    s += n[len(n)//2-1::-1]
print(s)