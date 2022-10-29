# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 09:16:55 2022

@author: Souvik Bhattacharya
"""

# Q1> list down all numbers and there property within a given range

import math

# limit = int(input("Enter the range:"))
limit = 10

if(limit > 1):
    for i in range(1,limit+1):
        if(i > 1):
            j = 0
            for j in range(2,int(math.sqrt(i)+1)):
                if(i%j == 0):
                    print(i,'is a composite no.')
                    break
            else:
                print(i,'is a prime no.')
        else:
            print(i,'is neither a prime nor a composite no.')
else:
    print('Invalid range!')
    
# Q2> determine the nth fibonacci number

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# n = int(input("Enter the no:"))
n = 15
result = fib(n)
print(str(n)+'th fibonacci no is',result)

# Q3> determine if a no is a fibpnacci no or not within a given range

def square(n):
    x = int(math.sqrt(n))
    if x**2 == n:
        return True
    else:
        return False

# r = int(input('Enter the range:'))
r = 16

for num in range(2,r):
    result = square((5*num**2)+4) or square((5*num**2)-4)
    if result:
        print(num,'is a fibonacci no.')
    else:
        print(num,'is not a fibonacci no.')