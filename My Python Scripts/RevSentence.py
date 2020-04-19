# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:18:55 2020

@author: hp
"""

'''

Ramu, Sita, Issac were playing word game. When their turn comes they will tell the name of the film which is a sentence. Means it should be more than one word. Others has to reverse the words from the given sentence. Also they decided to make this game as application using computer.
Rules are as follows:
⦁ It should be a film name and the film name should be a sentence.
⦁ It should contain more than one word.
⦁ The line should contain letters and space.
⦁ There should be exactly one space between each pair of words.
Sample Input
No.of sentence :2
Alibaba and 40 thieves
Star Wars
Sample Output
Thieves 40 and Alibaba
Wars Star


For example:

Test	Input                      Result
1       2  
        Alibaba and 40 thieves     Thieves 40 and Alibaba
        Star Wars                  Wars Star

'''




def RevSentence(s):
    words = s.split()
    words[-1] = words[-1].capitalize()   
    return ' '.join(words[::-1])

for i in range(int(input())):
    s = input()
    print(RevSentence(s))