#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:08:05 2019

@author: prasadm
"""

'''

Check_Box_State

There are N number of closed boxes in a room. there are N people standing outside the room in a queue. Now one person will enter the room and performs the following task.

if he is the ith person in the queue, then he will examine every ith box in the boxes and opens a box if it is closed otherwise closes it if it is open. All n persons in the queue have to enter the room in the order 1 ... N only.

Your task is to write a python script that shows the state of each of the N boxes as given in the note.

Note: 0 -> Close
          1 -> Open state
Input:
First line contains number of boxes or number of persons in the queue i.e N

Output:
Print the N integers separated by spaces indicating the N number of Box states.


Sample Input1:
5
Sample Output1:
1 0 0 1 0

Sample Input2:
10

Sample Output2:
1 0 0 1 0 0 0 0 1 0
 

Additional Sample TestCases
Sample Input and Output 1 :

3
1 0 0 

Sample Input and Output 2 :

5
1 0 0 1 0 
'''

n = int(input())
b = [0]*n
for i in range(n):
    for j in range(i,n,i+1):
        if b[j] == 0:
            b[j] = 1
        elif b[j] == 1:
            b[j] = 0
print(*b)