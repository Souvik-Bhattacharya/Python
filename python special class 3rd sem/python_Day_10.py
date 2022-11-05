# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:19:51 2022

@author: Souvik Bhattacharya
"""

# Q> calculate the factorial of a number

# iterative method:
    
# n = int(input('Enter the number:'))
n = 10

if n < 0:
    print('Invalid number given...')
elif n == 0:
    result = 1
elif n > 0:
    result = 1
    for i in range(1,n+1):
        result *= i
print('The factorial of',n,'is',result)

# recursive method:

def fact(n):
    if n == 0:
        return 1
    else:
        return(n * fact(n-1))

n = 10
result = fact(n)
print('The factorial of',n,'is',result)

# Q> Swap two numbers

# sum & subtraction method

x = 12
y = 20
x = x + y
y = x - y
x = x - y
print(x,y)

# product & division method

x = 12
y = 20
x = x * y
y = x // y
x = x // y
print(x,y)