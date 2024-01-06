
from typing import List
from math import sqrt

class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        # code here
        rs=0
        for i in range(a,b+1):
            x=int(sqrt(b))
            for j in range(2,x+1):
                while i % j== 0:
                    rs+=1
                    i=i // j
            if i>1:
                rs+=1
            
        return rs
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=int(input())
        b=int(input())
        
        obj = Solution()
        res = obj.sumOfPowers(a,b)
        
        print(res)
        

# } Driver Code Ends