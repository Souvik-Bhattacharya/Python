# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 17:26:31 2022

@author: Souvik Bhattacharya
"""

def bubble(b):
    n = len(b)
    for i in range(n):
        for j in range(n-i-1):
            if(b[j]>b[j+1]):
                c = b[j]
                b[j] = b[j+1]
                b[j+1] = c

def linear_search(a,x):
    count = 1
    for i in a:
        if(i == x):
            print(x,'is found in the position of ',i)
            break
        count += 1
    print(count)

def binary_search(a,x):
    first_pos = 0
    last_pos = len(a)-1
    count = 0
    flag = 0
    while(first_pos <= last_pos and flag == 0):
        count += 1
        mid = (first_pos + last_pos)//2
        if(a[mid] == x):
            print('The number present at ',mid)
            print('The total number of iterations is ',count)
            flag = 0
            return
        else:
            if(a[mid]>x):
                last_pos = mid-1
            else:
                first_pos = mid+1
    print("The number is not present in the given list !")

a = []
for i in range(1,501):
    a.append(i)
b = [23,55,132,2,3,87,7,4,0,454,6]
bubble(b)
print(b)
linear_search(a,127)
binary_search(a,127)