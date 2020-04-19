# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:35:09 2020

@author: hp
"""

'''

Program to convert a binary number to octal number.

Input:
11010

Output:

32

1. Valid Input:

a) Only number consisting of 0s and 1s will be given as input

2. Invalid inputs:

a) Decimal b) Fraction c) String

d) Negative number

3. You should generate output as follows:

a) For right output print just the actual Octal Value without any other text.

b) If any error: print 'ERROR' without any other text.

For example:

Test	Input	Result
1       101     5
2       11010   32  32

'''


def Bin2Oct(n):
    for i in n:
        if i in '10':
            continue
        else:
            return 'ERROR'
    s = int(n,2)
    return oct(s)[2:]

n = input()
print(Bin2Oct(n))