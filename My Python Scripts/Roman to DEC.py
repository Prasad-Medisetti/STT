# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:09:32 2020

@author: hp
"""

'''

Converting Roman Numerals to Decimal lying between 1 to 3999
Roman numerals are based on below symbols.

SYMBOL       VALUE
I             1
V             5
X             10
L             50
C             100
D             500
M             1000    
Input: XL

Output: 40

Input: MCMIV
Output: 1904
M is a thousand, CM is nine hundred
and IV is four


For example:

Test	Input	Result
1       MCMIV   1904
2       XL      40
3       XVIV    19


'''
def dec(s):
    r = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    l = [r[i] for i in s]
    if len(s)%2==0:
        n = []
        for i in range(0,len(l),2):
            if l[i]<l[i+1]:
                n.append(l[i+1]-l[i])
            else:
                n.append(l[i]+l[i+1])
        return sum(n)
    else:
        n = [l[0]]
        for i in range(1,len(l)-1):
            if l[i]<l[i+1]:
                n.append(l[i+1]-l[i])
        return sum(n)
s = input()
print(dec(s))