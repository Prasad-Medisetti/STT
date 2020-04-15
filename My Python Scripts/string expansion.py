#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:13:44 2019

@author: prasadm
"""

'''

String Expansion

Write a Python code to read the string contains every alphabet followed by a digit.
Now your task is to display the string as each alphabet in the given string repeated by followed digit in the given string.
Sample Input1:
A4B2C2
Sample Output1:
AAAABBCC
Sample Input2:
A1L2O1W1
Sample Output2:
ALLOW
 
Additional Sample TestCases
Sample Input and Output 1 :

A1L2O1W1
ALLOW

Sample Input and Output 2 :

E1N1G1I1N1E2R1I1N1G1
ENGINEERING

'''

from string import digits
s = input()
ns = '' 
for i in range(len(s)):
    if s[i] in digits:
        ns += s[i-1]*(int(s[i]))
print(ns)