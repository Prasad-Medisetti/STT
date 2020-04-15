# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:44:08 2019

@author: hp
"""
from functools import reduce
def isSeedSquare(input1,input2):
   l = [int(x)**2 for x in str(input1)]
   return input1 * reduce(lambda x,y : x*y ,[int(x) for x in l]) == input2
        

if __name__ == '__main__':
    input1 = int(input())
    input2 = int(input())
    result = isSeedSquare(input1,input2)
    print (result)