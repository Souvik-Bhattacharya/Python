# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 09:44:07 2022

@author: Souvik Bhattacharya
"""

a=10
b=20

c = a and b
print(c)

c = b and a
print(c)

d = False
c = a and d
print(c)

d = True
c = b and d
print(c)

d = False
e = 0
a = 10
c = d and e and a
print(c)

c = e and d and a
print(c)

c = a or b
print(c)

c = e or d
print(c)

c = not(a)
print(c)

c = not(False)
print(c)

s = 'Hi! I am souvik.'
c = 'souvik' in s
print(c)

c = 'hi' not in s
print(c)

x = '50'
y = 50
c = y is int(x)
print(c)
c = y is not x
print(c)
c = x is str(y)
print(c)