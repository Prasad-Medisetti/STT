# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:49:05 2019

@author: hp
"""

"""
PRONIC NUMBER
Pronic number is a number which is the product of two consecutive integers, that is, a number n is a product of x and (x+1).
The task is to check and print Pronic Numbers in a range.
The first few Pronic numbers are:
0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420, 462 . . . . . .
Sample Testcases:

Input  : 6
Output : Pronic Number
Explanation: 6 = 2 * 3 i.e 6 is a product
of two consecutive integers 2 and 3.

Input :56
Output :Pronic Number
Explanation: 56 = 7 * 8 i.e 56 is a product 
of two consecutive integers 7 and 8. 

Input  : 8
Output : Not a Pronic Number
Explanation: 8 = 2 * 4 i.e 8 is a product of 
2 and 4 which are not consecutive integers.

"""
def pronic(n):
    f = False
    i = 0
    j = 1
    while i*j <= n:
        if i*j==n:
            f = True
            break
        i += 1
        j += 1
    if f==True:
        print('Pronic Number')
    else:
        print('Not a Pronic Number')
        
if __name__ == '__main__':
    pronic(int(input('Enter a Number: ')))