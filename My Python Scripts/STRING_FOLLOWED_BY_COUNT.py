# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 05:48:07 2019

@author: hp

STRING_FOLLOWED_BY_COUNT
Write a python script to read in a string containg only letters [a-z] and generate another string which is the original string followed by characters and their correspomding counts in the original string with characters from z-a

Input1:
bananas
output1:
bananass1n2b1a3

input2:
ababaadityasai
output2:
ababaadityasaiy1t1s1i2d1b2a6

input 3:
finalandprefinalexams
output3:
finalandprefinalexamsx1s1r1p1n3m1l2i2f2e2d1a4
 

Additional Sample TestCases
Sample Input and Output 1 :
bananas
bananass1n2b1a3
Sample Input and Output 2 :
finalandprefinalexams
finalandprefinalexamsx1s1r1p1n3m1l2i2f2e2d1a4

"""

s = input()
ns = s[:]
for c in sorted(set(s),reverse=True):
    ns += c+str(s.count(c))
print(ns)