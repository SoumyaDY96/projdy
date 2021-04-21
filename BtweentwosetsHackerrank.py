# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:12:11 2021

@author: soumy_000
"""


import math
import os
import functools


def getTotalX(a, b):
    alc=functools.reduce(lcm,a)
    bgc=functools.reduce(gdc,b)
    count=0        
    for k in range(alc,bgc+1):
        if bgc%k==0:
            count+=1
            k*=2
        else:
            pass
    return count                          
            
def lcm(x,y):
    return abs(x*y)//math.gcd(x,y)

def gdc(p,r):
    return math.gcd(p,r)
              

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + '\n')

    
