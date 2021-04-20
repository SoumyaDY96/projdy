# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:36:33 2021

@author: soumy_000
"""


import math

def minsum(n,k):
    sn=sorted(n)
    print(sn)
    while k>0:
        last=sn[-1]
        b=math.ceil(last/2)
        sn.remove(last)
        sn.append(b)
        print(sn)
        sn.sort()
        k-=1
        
    return sum(sn)    
    
    
    
    
    
    
    
if __name__=='__main__':
    print("Enter the length of array")
    ln=int(input())
    n=[]
    for i in range(ln):
        print("Enter the values")
        a=int(input())
        n.append(a)
    print(n)    
    print("Enter the number of operations")
    k=int(input())
    result=minsum(n,k)
    print(str(result)+"\n")