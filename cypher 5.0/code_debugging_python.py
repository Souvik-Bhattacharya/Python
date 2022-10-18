# -*- coding: utf-8 -*-
"""
Spyder Editor
author: souvik bhattacharya
code debugging python
This is a temporary script file.
"""

# Q NO 1

# with open('file.txt','r') as file:
#     print(file.read())
#     file.write('write...')
# file.close()

# Q NO 2

# l = [1,2,[4,5,['hi','there','rcc'],6,7],3]
# a = l[2:3][0][2:3][0][-1]
# print(a)

# Q NO 3

# l = [6,31,35,46,51,54,55,56,57,58,59,60]
# a = 5
# b = l[5:6]
# c = a + b
# print(c)


# # Q NO 4

# def isvowel(ch):
#     v = 'AEIOUaeiou'
#     if ch in v:
#         return True
    
#     else:
#         return False

# def replaceV(s):
    
#     n = len(s)
#     ans = ''
#     i=0
#     while(i<n-2):
#         if isvowel(s[i]) and isvowel(s[i+1]) and isvowel(s[i+2]):
#             ans = ans+'_'
#             i = i+3
            
#         else:
#             ans = ans+s[i]
#             i = i+1
            
#     return ans+s[i:]

# print(replaceV('aaaajaaayeAAAEEEIIIOOOUUU___'))


# # Q NO 5

# def squareT(T):
#     temp = list(T)
#     for i in T:
#         temp.append(i*i)
#     return tuple(temp)
# if __name__ == "__main__":
#     L = [1,2,3,4,5]
#     T = tuple(L)
#     ans = squareT(T)
#     if type(ans) == type(T):
#         print(ans)

# Q NO 6

# def spiral(row,column,arr):
#     rowstart=0;columnstart=0
#     while (rowstart<row and columnstart<column):
#         for i in range(rowstart,row):
#             print(arr[i][columnstart],end=" ")
#         columnstart=columnstart+1
#         for i in range(columnstart,column):
#             print(arr[row-1][i],end=" ")
#         row=row-1
#         if(rowstart<row):
#             for i in range(row-1,rowstart-1,-1):
#                 print(arr[i][column-1],end=" ")
#             column=column-1
#         if(columnstart<column):
#             for i in range(column-1,columnstart-1,-1):
#                 print(arr[rowstart][i],end=" ")
#             rowstart=rowstart+1
# matrix=[[1,2,3],
#         [5,6,7],
#         [9,10,11]]
# row=3
# column=3
# spiral(row,column,matrix)

# Q NO 7

# a = 56
# b = '56'
# c = str(a)
# if c is b:
#     print('True')
# else:
#     print('False')

# Q NO 8

# x = (56 and 58 and 59 and 60 and 6 and False and 0)
# y = (False or 0 or 31 or 35 or 46 or 55 or 54)
# z = x or y
# print(z)

# Q NO 9

# a = (1,2,3,4,5,6)
# for i in range(-1,-len(a),-1):
#     print(a[i], end = ' ')

# Q NO 10

# def recursive(L):
#     if(len(L) <= 6):
#         return L[-1]
#     return L[-1] * recursive(L[:-1])

# a = recursive([1,2,3,4,5,6,7,8,9,10])
# print(a)