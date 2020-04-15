# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:20:14 2019

@author: hp

LIST 2
Given an input list removes the element at index d and add it to the ith index position and also, at the end of the list
Input Format:
First line contains list of elements
Index of an element to delete
Index of an element to insert
Sample Input:
34 54 67 89 11 43 94
4
2
Sample Output:

 Origigal list  [34, 54, 67, 89, 11, 43, 94]
 List After removing element at index 4 [34, 54, 67, 89, 43, 94]
 List after Adding element at index 2 [34, 54, 11, 67, 89, 43, 94]
 List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
Additional Sample TestCases
Sample Input and Output 1 :
1 2 3 4 5 6
3
2
Origigal list  [1, 2, 3, 4, 5, 6]
List After removing element at index 3 [1, 2, 3, 5, 6]
List after Adding element at index 2 [1, 2, 4, 3, 5, 6]
List after Adding element at last  [1, 2, 4, 3, 5, 6, 4]
"""

l = [int(x) for x in input().split()]
d = int(input())
i = int(input())
print('Original list ',l)
e = l.pop(d)
print('List After removing element at index',d,l)
l = l[:i]+[e]+l[i:]+[e]
print('List after Adding element at index',i,l[:-1])
print('List after Adding element at last',l)