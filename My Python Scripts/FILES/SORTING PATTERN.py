# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:56:53 2019
@author: hp

SORTING PATTERN
Write a python function that performs a sort(ascending order) of the elements of a list by successively comparing pairs of adjacent elements, exchanging them if they are out of order, and alternately passing through the list from the beginning to the end and then from the end to the beginning until no exchanges are needed.The function should print the list after each iteration and finally print the total number of comparisions. (if the list is already sorted only 0 shold be the output)

Sample input1:
[3,5,1,4,6,2]

Output1:
[3, 1, 4, 5, 2, 6]
[1, 3, 2, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
7

Sample input2:
[1,2,3,4]

Output2:
0

 

Additional Sample TestCases
Sample Input and Output 1 :
[1,2,3,4]
0
Sample Input and Output 2 :
[3,5,1,4,6,2]
[3, 1, 4, 5, 2, 6]
[1, 3, 2, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
7
"""

def sort(l):
    for i in range((len(l)//2)+1):
        if l[i]>l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
    return l