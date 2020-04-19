# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:41:05 2020

@author: hp
"""

'''
Telephone keyboard input recognition –I
On a standard telephone, the numbers 1-9 can be used to correspond to a set of letters:
1: space                2: ABC                   3: DEF              4: GHI                  5: JKL                   6: MNO            7: PQRS                 8: TUV                   9: WXYZ
Using the keypad, you can 'spell' words by entering the digits that correspond to each letter of the word. For example, ’CAT’ is spelled as 222 2 8 i.e., Frequency of each digit represents the character in the possible combination. In the above example, 2 pressed for 3 times that means we are entering C and the space followed by it specifies the other character in the string or else 22 can be interpreted in two ways AA or B.  Space delimiter is used to represent the next character in the input string.

Sample Test Case: Input:
22 2 8
Output:
BAT

For example:
Test	Input	    Result
1       22 2 8      BAT
2       333 2 66    FAN
3       9 8 7 6     WTPM

'''

def telkeypad(s):   
    d = { 1:' ', 2:'ABC', 3:'DEF',4:'GHI', 5:'JKL', 6:'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ' }
    chars = s.split()
    res = ''
    for i in chars:
        k = int(i[0])
        res += d[k][i.count(str(k))-1]
    return res

s = input()
print(telkeypad(s))