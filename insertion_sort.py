# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:02:52 2021

@author: soumy_000
"""


def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1,n):
 
        min_index = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        for j in range(i-1,-2,-1):
            if arr[j]>min_index:
                arr[j+1]=arr[j]
            else:
                break
        arr[j+1]=min_index 
    return arr    
            
 
 
# Driver code to test above
if __name__=='__main__':
    n=int(input("What will be the length of array: "))
    arr=[]
    for i in range(n):
        x=int(input("Enter the values :"))
        arr.append(x)
    result=insertionSort(arr)
    for j in range(n):
        print ("The sorted array is  %d" % result[j])