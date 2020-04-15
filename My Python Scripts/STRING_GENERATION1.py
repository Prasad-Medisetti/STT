# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 05:46:54 2019

@author: hp

STRING_GENERATION1
Write a python function to generate and return the list of all possible sentences created from the given lists of Subject, Verb and Object.
Note: The sentence should contain only one subject, verb and object each.

Input:

I You

Love Play

Hockey Football

Output:

I Play Hockey
I Play Football
I Love Hockey
I Love Football
You Play Hockey
You Play Football
You Love Hockey
You Love Football

Additional Sample TestCases
Sample Input and Output 1 :
I You
Love Play
Hockey Football
Hockey Football
I Love Hockey
I Love Football
I Play Hockey
I Play Football
You Love Hockey
You Love Football
You Play Hockey
You Play Football
"""

sub = input().split()
verb = input().split()
obj = input().split()
for i in sub:
    for j in verb:
        for k in obj:
            print(i,j,k)