# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:09:39 2020

@author: hp
"""

'''

PROBLEM
HAPPY NUMBER
Happy Number
Write a program  to check the given number is a Happy number or not. 
A number is called happy if it leads to 1 after a sequence of steps where in each step number is replaced by sum of squares of its digit that is if we start with Happy Number and keep replacing it with digits square sum, we reach 1.
Examples :

 Input: n = 19
 Output:
 19 is a happy number
 1^2 + 9^2 = 82
 8^2 + 2^2 = 68
 6^2 + 8^2 = 100
 1^2 + 0^2 + 0^2 = 1
 As we reached to 1, 19 is a Happy Number.
 Another Example:
 Input: n = 20
 Output: 20 is not a happy number

Additional Sample TestCases
Sample Input and Output 1 :
13
13 is a happy number
Sample Input and Output 2 :
2005
2005 is not a happy number

'''

def happy(n):
    n = sum([int(d)**2 for d in str(n)])
    return n
        
if __name__=='__main__':
    n = int(input())
    hapy = n
    while n!=1 and n!=4:
        n=happy(n)
    if n==1:
        print(hapy,'is a happy number')
    else:
        print(hapy,'is not a happy number')