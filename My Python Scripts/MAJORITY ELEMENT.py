# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:11:04 2020

@author: hp
"""

'''

PROBLEM
MAJORITY ELEMENT
Harsha is good at numbers and series. His teacher wants to test his ability. Harsha was given a task by his teacher. He gave n numbers to harsha and asked him to find whether a majority element is existing or not. If not present he has to say “No Such Element”. Help Harsha in solving the problem.
Note: A majority element is one that appears more than n/2 times.
Example:
Input:
3 3 4 2 4 4 2 4 4
Output:
4
 


Additional Sample TestCases
Sample Input and Output 1 :
3 3 4 2 4 4 2 4
No Such Element
Sample Input and Output 2 :
3 3 4 2 4 4 2 4 4
4

'''


def mjele(l):
    d = {}
    for i in l:
        d[i] = d.get(i,0)+1
    for i in d.items():
        if i[1]>len(l)//2:
            return i[0]
    
    
    
if __name__=='__main__':
    l = list(map(int,input().split()))
    print(mjele(l))