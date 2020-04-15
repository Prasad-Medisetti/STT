# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 05:53:09 2019
@author: hp
STRING_PATTERN1
Write a python script that reads in a string and prints the following output.
String: abcd
d
cd
bcd
abcd

input 1:
grapes

ouput 1:

s
es
pes
apes
rapes
grapes
"""

s = input()
for i in range(-1,-len(s)-1,-1):
    print(s[i:])