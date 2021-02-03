# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:29:28 2021

@author: soumy_000
"""


a=[1,2,3,4,5,6,7,8,9,10,11,12,100,99]
d=4

def leftshift(x,y):
    r=[]
    for i in range(len(y)):
        r.append(y[i])
    for j in range(len(y)):
        y[j-x]=r[j]
    print(y) 
    
def rightshift(m,n):
    r=[]
    c=len(n)
    for i in range(c):
        r.append(n[i])
    for j in range(c):
        n[j-(c-m)]=r[j]
    print(n)    
    
        
leftshift(d,a) 
rightshift(d,a)