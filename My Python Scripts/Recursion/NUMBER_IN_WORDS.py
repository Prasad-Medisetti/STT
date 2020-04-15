# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:33:32 2019

@author: hp
NUMBER_IN_WORDS
Write a python function to identify and return the number name of a given number. 
The number should be in the range 1 to 1000. If the number is invalid, return -1.

Sample input 1:
1
output1:
one
sample input2:
112
output2:
one hundred and twelve
 

Additional Sample TestCases
Sample Input and Output 1 :
3997
-1
Sample Input and Output 2 :
345
three hundred and fortyfive
Sample Input and Output 3 :
814
eight hundred and fourteen

"""

def num2words(n):
    ns = str(n)
    nl = [int(x) for x in str(n)]
    d = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
    8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
    14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
    19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
    70:'seventy',80:'eighty',90:'ninety',100:'one hundred',200:'two hundred',
    300:'three hundred',400:'four hundred',500:'five hundred',600:'six hundred',
    700:'seven hundred',800:'eight hundred',900:'nine hundred',1000:'thousand'}
    if n>=1 and n<=1000:
        if d.get(n)!=None:
            return d[n]
        else:
            if n<100:
                return d[nl[0]*10]+d[nl[1]]
            else:
                return d[nl[0]*100]+' and '+num2words(int(ns[1:]))
    else:
        return -1

if __name__=='__main__':
    n = int(input())
    print(num2words(n))