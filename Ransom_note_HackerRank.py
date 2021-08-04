# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:48:13 2021

@author: soumy_000
"""


import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    try:
        for j in note:
            magazine.remove(j)
        print("Yes")
    except:
        print("No")
        return
        
            
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)