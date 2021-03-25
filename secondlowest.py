# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:10:52 2021

@author: soumy_000
"""


if __name__ == '__main__':
    mark=[]
    sheet={}
    names=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())    
        mark.append(score) 
        sheet[name]=score
            
    nextmin=min([i for i in mark if i!=min(mark)])  
    for k,v in sheet.items():
        if v==nextmin:
            names.append(k)
        else:
            continue 
    print('\n'.join([i for i in sorted(names)])) 