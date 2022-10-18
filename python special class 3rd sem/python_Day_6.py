# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 09:16:07 2022

@author: Souvik Bhattacharya
"""

l = [1,2,3,4,5,6,7]
print(l.pop())
print(l)
l.remove(4)
print(l)
del l[len(l)-1]
print(l)
# del l
l.reverse()
print(l)
# l.sort()
# print(l)
nl = sorted(l)
print(l)
print(nl)
print(nl.index(3))
# reversing a list
i = 0
j = 0
for i in range(len(l)):
    for j in range(len(l)-1-i):
        tmp = nl[j]
        nl[j] = nl[j+1]
        nl[j+1] = tmp
print(nl)
# reversing a string
s = "hi there"
ns = ""
print(ns.join(reversed(s)))
#print(ns)
print(s[::-1])
# pallindrome checking
def rev(y):
    c = 0
    n = ''
    for i in range(len(y)):
        n += y[len(y)-1-i]
    for i in range(len(y)):
        if y[i] != n[i]:
            c = 1
            break
    if c == 1:
        return False
    else:
        return True

x = 'malayalam'
ans = rev(x)
print(ans)