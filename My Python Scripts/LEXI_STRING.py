# -*- coding: utf-8 -*-
"""
LEXI_STRING
Lexi String

Problem Description
Little Jill jumbled up the order of the letters in our dictionary. Now, Jack uses this list to find the smallest lexicographical string that can be made out of this new order. Can you help him?
You are given a string P that denotes the new order of letters in the English dictionary. You need to print the smallest lexicographic string made from the given string S.
Constraints
1 <= T <= 1000
Length (P) = 26
1 <= length (S) <= 100
All characters in the string S, P are in lowercase
Input Format
The first line contains number of test cases T
The second line has the string P
The third line has the string S
Output
Print a single string in a new line for every test case giving the result
Test Case
Example 1
Input
2
polikujmnhytgbvfredcxswqaz
abcd
qwryupcsfoghjkldezxvbintma
ativedoc
Output
bdca
codevita
Explanation
The transformed smallest lexicographical strings are in order they would be if order of letters are changed to string P.
 

Additional Sample TestCases
Sample Input and Output 1 :
1
polikujmnhytgbvfredcxswqaz
abcd
bdca
Sample Input and Output 2 :
1
abcdsuvwxtmnoptmndefghijk
tts
stt
"""

#n = int(input())
#s = []
#for i in range(0,2*n,2):
#    out = ''
#    pl = input()
#    sl = input()
#    for c in pl:
#        if c in sl:
#            out += c
#    s.append(out)
#print(*s,sep='\n')


s1 = input()
s2 = input()
print(''.join(sorted(s2,key=lambda x:s1.index(x))))