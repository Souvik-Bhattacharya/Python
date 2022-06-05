# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:24:01 2022

@author: Souvik Bhattacharya
"""

a = list(i for i in input().split())
b = []
for i in a:
    b.append(''.join(i[::-1]))
b.sort()
d = []
for i in b:
    #c = list(i)
    d.append(''.join(i[::-1]))
print(d)

