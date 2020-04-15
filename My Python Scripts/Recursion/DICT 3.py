# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:21:03 2019

@author: hp

DICT3
Write a python code for a given list iterate it and count the occurrence of each element and create a dictionary to show the count of each element.
Sample Input:
11 45 8 11 23 45 23 45 89
Expected Output:

 Original list  [11, 45, 8, 11, 23, 45, 23, 45, 89]
 Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
Additional Sample TestCases
Sample Input and Output 1 :
11 22 33 44 55 66 11 22 55 33 44
Origigal list  [11, 22, 33, 44, 55, 66, 11, 22, 55, 33, 44]
Printing count of each item   {11: 2, 22: 2, 33: 2, 44: 2, 55: 2, 66: 1}
Sample Input and Output 2 :
1 1 1 1 2 2 2 2 2 2 3 3 3 3 3 3 3 3 4 4 4 5 5 5 5 5 5 5 6 6 6 6 6 6 4
Origigal list  [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 4]
Printing count of each item   {1: 4, 2: 6, 3: 8, 4: 4, 5: 7, 6: 6}
"""

l = [int(x) for x in input().split()]
d = {}
for i in l:
    d[i] = d.get(i,0)+1
print('Origigal list ',l)
print('Printing count of each item ',d)