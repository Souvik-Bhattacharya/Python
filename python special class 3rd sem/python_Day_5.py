# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 09:10:37 2022

@author: Souvik Bhattacharya
"""

l1 = ['apple','mango',56]
print(l1[-3])

l2 = ['apple',[56,['mango','yes']]]
print(l2[1][1][0])
print(l2[-1][-1][-2])
print(l2[1:2][0][1:2][0][0:1][0])

l3 = l2[1:2]
print(l3)

l4 = []
n = int(input('Enter length: '))
for i in range(n):
    element = int(input('Enter elements: '))
    l4.append(element)

for i in l4:
    print(i, end = ' ')
print()

print(l4[::2])

print(l3, l4)
print(l3 + l4)

print(type(l4[0]))
print(type(l4[0:1]))