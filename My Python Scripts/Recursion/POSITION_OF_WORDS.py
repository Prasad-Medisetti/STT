# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:44:28 2019

@author: hp

POSITION_OF_WORDS
Write a python function which accepts a string of words and a target word, and returns the list of the positions of the target word in the string of words. 

Sample input1:
we dont need no education we dont need no thought control no we dont
dont
output1:
[1,6,13]
 

Additional Sample TestCases
Sample Input and Output 1 :
we dont need no education we dont need no thought control no we dont
dont
[1, 6, 13]
Sample Input and Output 2 :
abc abc abc abc abc abc abc abc
bc
[]
"""

def posofwords(s,sub):
    sl = s.split()
    return [i for i in range(len(sl)) if sl[i]==sub]

if __name__=='__main__':
    s = input()
    sub = input()
    print(posofwords(s,sub))