# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:26:17 2019

@author: hp
"""

'''HIGHEST_POPULATION
Highest_Population
Suppose you are given a data structure which is a list of dictionaries as follows:
[
{'Name':'Vancouver','State':'WA','Population':161791},
{'Name':'Salem','State':'OR','Population':154637},
{'Name':'Seattle','State':'WA','Population':608660},
{'Name':'Spokane','State':'WA','Population':208916},
{'Name':'Aeattle','State':'WA','Population':608660}
]
write a python function that takes the list and a state as parameters and returns the city (as a dictionary) with the highest population in a given state.
If the population is a tie then return the city that comes first alphabetically.

Sample input1:
[
{'Name':'Vancouver','State':'WA','Population':161791},
{'Name':'Salem','State':'OR','Population':154637},
{'Name':'Seattle','State':'WA','Population':608660},
{'Name':'Spokane','State':'WA','Population':208916}
]
WA

ouput1:

{'Name':'Seattle','State':'WA','Population':608660}
 

 '''
 
def highestpopulation(ld,state):
    ls = [i for i in ld if i['State']==state]
    m = max(ls,key=lambda k:k['Population'])['Population']
    return sorted([i for i in ls if i['Population']==m],key=lambda k:k['Name'])[0]

if __name__=='__main__':
    ld = eval(input())
    state = input()
    print(highestpopulation(ld,state))