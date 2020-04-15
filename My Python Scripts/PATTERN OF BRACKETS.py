# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:18:07 2019

@author: hp
"""

'''
PATTERN OF BRACKETS
Write a python code which accepts a string containing a pattern of brackets and returns true if the pattern of brackets is correct. Otherwise it returns false.
The string of brackets is correct if it satisfies the following conditions:
1. Number of opening and closing brackets are equal.
2. Pattern should not start with closing bracket and end with opening bracket.
 
Sample Testcase 1:
Input:
      )()((()())
Output:
     False
Sample Testcase 2:
Input:
     ()((())())
Output:
    True
'''

s = input()
n = len(s)
st,e = 0,0
for i in range(len(s)):
    if s[0]==')':
        e -= 1
    elif s[n-1]=='(':
        st -= 1
    elif s[i] =='(':
        st += 1
    elif s[i]==')':
        e += 1
print(st==e)