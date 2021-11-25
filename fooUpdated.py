# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 10:23:51 2021

@author: Sudharsaan
"""

import os 
os.chdir("C:\\Users\\Sudharsaan\\OneDrive\\SIM\\Year 2\\ST2195 Programming for Data Science\\Practice Assignment\\Assignment 5\\Assignment 5")

def is_divisible_by_k(x,k):
    if x%k == 0: 
        y = True
    else: 
        #print(str(x) + " is not divisible by " + str(k) + " since remainder is not 0") 
        y = False
    return y

is_divisible_by_k(2,2)

integers_divisibe_by_2_or_5_or_7 = []

for i in range(1001):
    if (is_divisible_by_k(i,2) == True or is_divisible_by_k(i, 5) == True or is_divisible_by_k(i, 7) == True):
        integers_divisibe_by_2_or_5_or_7.append(i)
        
integers_divisibe_by_2_or_5_or_7

sum(integers_divisibe_by_2_or_5_or_7)

