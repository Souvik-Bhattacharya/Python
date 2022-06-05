# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:44:40 2022

@author: Souvik Bhattacharya
"""
import string
s=input()
l=[]
for i in s:
    l.append(i)
#l=list(s)
#print(l)
s1=string.ascii_lowercase
l1=list(s1)
#print(l1)
s2=string.ascii_uppercase
l2=list(s2)
#print(l2)
for i in l:
  if(i in l1):
    n1=l1.index(i)
    #print(n1)
    x=l2[n1]
    print(x,end='')
  elif(i in l2):
    n2=l2.index(i)
    #print(n2)
    y=l1[n2]
    print(y,end='')
  else:
    print(i,end='')