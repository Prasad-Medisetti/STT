# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 05:57:44 2019

@author: hp

JET AND MAT
Given a string, write a python code to print True if the strings "mat" and "jet" appear the same number of times in the given string, else return False.
Note: Perform case insensitive string comparison wherever necessary.

Sample Input	Expected Output
Jet on the Mat but mat is too long	False
mat jet Jet Mat	True
Additional Sample TestCases
Sample Input and Output 1 :
Jet on the Mat but mat is too long
False
Sample Input and Output 2 :
mat jet Jet Mat
True
"""

s = input().split()
jet,mat = 0,0
for i in s:
    if i=='jet':
        jet += 1
    elif i=='mat':
        mat += 1
print(jet==mat)