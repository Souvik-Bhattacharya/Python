# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:21:37 2022

@author: Souvik Bhattacharya
"""

import string

l = list(input())
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
d = {}
for i in range(len(s1)):
    d[s1[i]] = s2[i-2]
for i in range(len(s2)):
    if i <= 23:
        d[s2[i]] = s2[i+2]
    elif i == 24:
        d[s2[i]] = s2[0]
    elif i == 25:
        d[s2[i]] = s2[1]
num = '0123456789'
for i in range(len(num)):
    d[num[i]] = num[i-5]
for i in l:
    if i in d:
        print(d[i],end = '')
    elif i == ' ':
        print('#',end = '')
    else:
        print(i,end = '')