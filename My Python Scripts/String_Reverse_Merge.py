#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:31:23 2019

@author: prasadm
"""

'''

String_Reverse_Merge

Given two lists, both having String elements, write a python program using python lists to create a new string as per the rule given below:
The first element in list1 should be merged with last element in list2, second element in list1 should be merged with second last element in list2 and so on.

If an element in list1/list2 is None, then the corresponding element in the other list should be kept as it is in the merged list. 

Input:
take 2 strings as an input
Output:
a string contains the all the words of the two input strings concatenated as per the above rules.

Sample Input:
A app a d ke th doc awa
y tor e eps ay None le n
Sample Output:
An apple a day keeps the doctor away

 

Additional Sample TestCases
Sample Input and Output 1 :

A app a d ke th doc awa
y tor e eps ay None le n
An apple a day keeps the doctor away 

Sample Input and Output 2 :

In wil wi world None i 20
23 n cup None n l dia
India will win world cup in 2023 

'''


l1 = input().split()
l2 = input().split()
l3 = []
n = len(l1) if len(l1) > len(l2) else len(l2)
n-=1
for i in range(n+1):
    s = l1[i]+l2[n-i]
    if 'None' in s:
        j = s.find('None')
        if j == 0:
            s=s[4:]
        else:
            s = s[:j]
    l3.append(s)
    
print(*l3)