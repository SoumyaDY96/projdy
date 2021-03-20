# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:06:35 2021

@author: soumy_000
"""


class Deque:
    
    def __init__(self):
        self.items=[]
        
    def add_front(self,item):
        return self.items.insert(0,item)
        
    def add_rear(self,item):
        return self.items.append(item)
        
    def del_front(self):
        return self.items.pop(0)
        
    def del_rear(self):
        return self.items.pop()
        
    def is_empty(self):
        return self.items==[] 
    
    def size(self):
        return len(self.items)
    
def check_palindrome(input_string):     
    myd = Deque()
   
    
    for char in input_string:
        myd.add_rear(char)   
        
    while myd.size()>=2:
        frontitem=myd.del_front()
        rearitem=myd.del_rear()
      
        
        if frontitem != rearitem:
            return False
    return True 
    
if __name__=='__main__':
    a=input("please provide the name: ")
    print(check_palindrome(a))        
         