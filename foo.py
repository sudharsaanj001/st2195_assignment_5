# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:50:36 2021

@author: Sudharsaan
"""

import os
# Used to set the working directory. Include an additional "\" between folders for the code to work. # os.chdir("C:\Users\Sudharsaan\OneDrive\SIM\Year 2\ST2195 Programming for Data Science\Practice Assignment\Assignment 3\Harverd Dataverse") does not work
os.chdir("C:\\Users\\Sudharsaan\\OneDrive\\SIM\\Year 2\\ST2195 Programming for Data Science\\Practice Assignment\\Assignment 5\\Assignment 5")

def is_divisible_by_k(x, k):
 '''
 Checks whether x is divisible by k.
 '''
 assert x%k == 0
 
'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding 
doubles)
'''
x = ()
for i in range(1000):
 if (is_divisible_by_k(x, 2) & is_divisible_by_k(x, 3)) | is_divisible_by_k(x, 7):
     x.append(i)
 
'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding 
doubles)
'''
sum(x)

# First bug found was found by using Debug (Ctrl + F5) which returned IndentationError. 
# Solution: Perform indentation on x.append(i) 
# x.append(i)
# ^
# IndentationError: expected an indented block

# 2nd bug found was that when using Debug & placing a breakpoint (By clicking on the line which creates a red circle) at
# the line which defines the is_divisibe_by function, the function requires values x & k as its arguments. When stepping into
# said function, it moves to line where x=() which calls for x that is part of another function. Since both x's are used to 
# perform different tasks (One is used to check whether a number is divisibe by another & the other x is used to store all 
# integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 excluding doubles)
# Solution: Change the argument in the is_divisibe_by function from x to something else like y. 

# 3rd bug found was at the if(is_divisible_by_k(x, 2) & is_divisible_by_k(x, 3)) | is_divisible_by_k(x, 7): line which gives 
# the TypeError: unsupported operand type(s) for %: 'tuple' and 'int' 

# By understanding the objective of the program, we are required to sum all integers of said characteristics that are lower or
# equal to 1000. Through which we find the 4th bug which is that the range function's argument should be 1001 instead of 1000
# since range(1000) only includes integer values from 0 to 999. 

# By looking at the if statement, we also find that the statement only appends a value the within range 0 to 999 into vector
# x if it is divisibe by 2 & 3 or divisibe by 7. We need the integers that are divisible by 2 OR 5 OR 7. So the and operator 
# is not required. This is the 5th bug. The 6th bug is that the value 3 which should be changed to 5 instead. 