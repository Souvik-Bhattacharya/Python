# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 09:29:08 2022

@author: Souvik Bhattacharya
"""

# strings
'''
x = '123'
y = x + 1
print(y)

y = 1 + x
print(y)
'''
name = input("Enter:")
print(type(name))
print(name)

name = int(input("Enter:"))
print(type(name))
print(name)

fruit = 'mango'
print(fruit[0])
print(fruit[-1])
print(fruit[-2])

index = 0
while(index < len(fruit)):
    print(index, fruit[index])
    index += 1
    
for letter in fruit:
    print(letter, end = '')
print()
    
print(fruit[:])
print(fruit[2:])
print(fruit[:3])

a = 'fruit'
b = 'mango'
c = a + ': ' + b
print(c)

if 'o' in fruit:
    print('found')

if fruit == 'guava':
    print('matched')
else:
    print('not matched')

word = 'apple'
if(word < fruit):
    print('before')
elif(word > fruit):
    print('after')
else:
    print('same')

greet = 'HEllo'
print(greet.lower())
print(greet.upper())

#print(dir(greet))

print(greet.find('lo')) #return -1 if doesn't match

print(greet.replace('E','e'))
print(greet)

x = '   hello   '
print(x.lstrip())
print(x.rstrip())

y = 'hi 56'
print(y.startswith('hi'))

z = 'kkkkhi k'
print(z.lstrip('k'))
print(z.lstrip())
print(z)