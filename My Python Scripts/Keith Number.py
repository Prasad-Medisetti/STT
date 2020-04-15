# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:39:41 2019

@author: hp
"""
'''
KEITH NUMBER
Keith numbers are rare numbers with a Fibonacci like property. An n-digit number with value N is a Keith number if N is part of the Keith series generated. This series starts with the n digits of the number N. Then the subsequent numbers in the series are found by calculating the sum of preceding n numbers. If the number N appears in the series, it is called a Keith number. Keith numbers are also known as repfigit (repetitive Fibonacci-like digit) numbers.

Keith numbers are very rare and computationally difficult to find. No optimized algorithm is known for finding Keith numbers. Only option is to do an exhaustive search.

For example consider the 3 digit number 742. Using the above rule, the first three numbers are 7, 4, 2. The next one is 7+4+2 (adding 3 previous numbers) = 13. The next one in series is 4+2+13 = 19. By applying this rule, following are numbers in the sequence,
7, 4, 2, 13, 19, 34, 66, 119, 219, 404, 742, 1365. The original number appears as the 11th item in the series. Hence the number 742 is a 3 digit Keith number.
Now Program to find the given number is Keith Number or not
Sample Input1:
742
Sample Output1:
742 is a Keith Number
Sample Input2:
194
Sample Output2:
194 is not a Keith Number
 
'''
s = input()
n = int(s)
l=[]
for i in range(0,len(s)):
    l.append(int(s[i]))
i = 0
while n not in l and l[i] < n:
    l.append(sum(l[i:]))
    i += 1
if n in l:
    print(n,'is a Keith Number')
else:
    print(n,'is not a Keith Number')