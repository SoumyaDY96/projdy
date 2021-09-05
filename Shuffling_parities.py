# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:58:07 2021

@author: soumy_000
"""


from itertools import permutations as pm

for _ in range(int(input())):
    
    N=int(input())
    A=[int(i) for i in input().split()]
    mx=0
    for i in pm(A):
        sm=0
        
        for j in range(len(list(i))):
            
            sm+=((list(i))[j]+(j+1))%2
        if sm>mx:
            mx=sm
        else:
            continue
    print(mx)