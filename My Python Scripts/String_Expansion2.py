#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:32:19 2019

@author: prasadm
"""

'''
String_Expansion2

Write a Python code to read the string contains every alphabet followed by a digit. Now your task is to display the string as each digit in the given string is converted to an alphabet by add this digit to the previous alphabet in the given string.
Sample Input1:
a4k3b2
Sample Output:
aeknbd
Sample Input2:
A1C1E1
Sample Output2:
ABCDEF

Additional Sample TestCases
Sample Input and Output 1 :

A4B2C4D2
AEBDCGDF

Sample Input and Output 2 :

a4k3b2
aeknbd

Sample Input and Output 3 :

a4r3s5
aerusx
'''

from string import ascii_letters, digits
s = input()
n = len(s)
ns = ''
case = s[0].isupper()
i = 0
c = 0
while i < n:
    # if s[i] in digits and s[i+1] in digits:
    if s[i] in digits:    
        if case == True:
            ns += ascii_letters[i].upper()
            c+=1
        else:
            ns += ascii_letters[i]
    if s[i] in ascii_letters:
        ns += s[i]
    i += 1
print(ns)