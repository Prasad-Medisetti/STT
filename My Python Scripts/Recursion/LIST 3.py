# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:21:51 2019

@author: hp

LIST 3
Mr. Jagadeesh and Mr. Srinu are bored and wanted to play a game. Mr. Jagadeesh will give 10 names to Mr. Srinu. Now the task for Mr. Srinu is to delete the character from the current name depending upon its position in the given set of names. For Example If jagadeesh is the third name then the third indexed character in jagadeesh to be deleted. So jagadeesh will become jagdeesh.
After doing so the names obtained are needed to be shown to Mr. Jagadeesh.
Note: if the length of the name is less than the position then there is no need to delete the character from the name.

Sample Input:

abc defg hijklm

Sample Output:

bc
dfg
hiklm

Additional Sample TestCases
Sample Input and Output 1 :
abc defg hijklm
bc
dfg
hiklm
Sample Input and Output 2 :
abhi ramesh anand gajapathi narayanarao
bhi
rmesh
annd
gajpathi
naraanarao
"""

l = input().split()
for i in range(len(l)):
    if len(l[i])<i:
        print(l[i])
    else:
        print(l[i][:i]+l[i][i+1:])