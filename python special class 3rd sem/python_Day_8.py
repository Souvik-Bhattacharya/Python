# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 09:24:09 2022

@author: Souvik Bhattacharya
"""
from collections import OrderedDict
import numpy as np

d0 = {'y':1,'x':2,'z':3}
for i in d0:
    print(d0[i],end = ' ')
print()

d1 = dict()
d1['x'] = 1
print(d1)
d1['x'] = 2
print(d1)

d1.clear()
print(d1)

d1 = d0.copy()  # shallow copy
print(d1)

print(d1.get('y','default'))
print(d1.get('w','default'))

print(d1.items())
print(d1.keys())
print(d1.values())

# SORTING A DICTIONARY W.R.T KEYS

d2 = OrderedDict(sorted(d1.items()))
print(d2)

# SORTING A DICTIONARY W.R.T VALUES

d3 = {'a':2,'b':1,'c':3,'d':1}
print(d3)

# SIR'S APPROACH
# sorted_index = np.argsort(d3.values())
# keys = []
# for i in d3.keys():
#     keys.append(i)
# sorted_dict = {keys[i]:sorted(d3.values())[i] for i in range(len(keys))}
# print(sorted_dict)

# MY APPROACH
keys = [i for i in d3.keys()]
values_list = [i for i in d3.values()]
sorted_d3 = {}
values_list.sort()
values = set(values_list)
for j in values:
    for k in d3:
        if d3[k] == j:
            sorted_d3[k] = d3[k]
print(sorted_d3)