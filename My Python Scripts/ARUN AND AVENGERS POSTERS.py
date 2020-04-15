# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:13:43 2020

@author: hp
"""

'''

PROBLEM
ARUN AND AVENGERS POSTERS
Arun is a huge fan of Avengers. He needs to hang n Avengers posters on his wall. Standing on the ground he can reach upto a height of h. Each poster is to be bolted at a certain height above the ground level, described by the array wallpoints . Each poster also has some length, defined by the array lengths. To hang a poster properly, Arun needs to hold atleast 50% of the length of the poster and poster is to be bolted at a point which is 25% from its top. 
Arun wants to know what is the minimum height of the ladder he should buy, in order to hang all the wall posters. The ladder is only available in integral heights. Arun can reach any height upto the maximum possible height.

Input Format

The first line of the input contains two space separated integers, n and h.
The next line contains n space separated integers, denoting the elements of the array wallpoints.
The last line contains n space separated integers, denoting the elements of the array lengths.


Constraints:
1<=h<=109
1<=n<=105
1<=wallpointsi<=109 (0<=i<n)
1<=lengthsi<=105 (0<=i<n)
Output Format

Output an integer, the minimum height of the ladder required. If no ladder is required, output 0

Sample Input:
3 5
15 11 7
5 1 2
Sample Output:
12
Explanation 0

Arun’s height is 5
To hang the first poster, Arun need to reach a height of 13.75, so he needs a ladder of height 9.
To hang the second poster, Arun need to reach a height of 10.75, so he needs a ladder of height 6.
To hang the third poster, Arun need to reach a height of 16.50, so he needs a ladder of height 12.

So, the height of the ladder required is 12.


Additional Sample TestCases
Sample Input and Output 1 :
3 5
15 11 17
5 1 2
12
Sample Input and Output 2 :
2 5
5 5
4 4
0

'''


