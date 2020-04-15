#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:08:47 2019

@author: prasadm
"""

'''

Count_State_Box

There are N number of closed boxes in a room. there are N people standing outside the room in a queue. Now one person will enter the room and performs the following task.

if he is the ith person in the queue, then he will examine every ith box in the boxes and opens a box if it is closed otherwise closes it if it is open. All n persons in the queue have to enter the room in the order 1 ... N only.

Your task is to write a python script that shows the no of boxes open and no of boxes close state after all the N persons visited the room once..

Note: 0 -> Close
          1 -> Open state



Input:
First line contains number of boxes or number of persons in the queue i.e N

Output:
Print the 2 integers separated by spaces indicating open state box count and closed state box count
Note: 0 -> Close
          1 -> Open state

Sample Input1:
5
Sample Output1:
2 3

Sample Input2:
10

Sample Output2:
3 7

Additional Sample TestCases
Sample Input and Output 1 :

5
2 3 

Sample Input and Output 2 :

10
3 7 

Sample Input and Output 3 :

12
3 9 

'''

n = int(input())
b = [0]*n
for i in range(n):
    for j in range(i,n,i+1):
        if b[j] == 0:
            b[j] = 1
        else:
            b[j] = 0
print(b.count(1),b.count(0))
