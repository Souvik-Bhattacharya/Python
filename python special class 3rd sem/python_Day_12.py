# Q> Printing a half pyramid

def drawStars(n):
    for i in range(1,n + 1):
        for j in range(i):
            print('*',end = '')
        print()
    print('\n')

def drawNumbers(n):
    for i in range(1,n + 1):
        for j in range(i):
            print(j + 1,end = '')
        print()
    print('\n')

def drawAlphabets(n):
    for i in range(1,n + 1):
        for j in range(i):
            print(chr(65 + j),end = '')
        print()
    print('\n')

def drawStarsReverse(n):
    for i in range(n,0,-1):
        for j in range(i):
            print('*',end = '')
        print()
    print('\n')

def drawNumbersReverse(n):
    for i in range(n,0,-1):
        for j in range(n,n-i,-1):
            print(j,end = '')
        print()
    print('\n')

# Q> Printing a full pyramid

def drawPyramid(n):
    for i in range(n):
        for k in range(n-i-1):
            print(' ',end = '')
        for j in range(2*i+1):
            print('*',end = '')
        print()
    print('\n')

n = int(input('Enter the row no:'))
drawStars(n)
drawNumbers(n)
drawAlphabets(n)
drawStarsReverse(n)
drawNumbersReverse(n)
drawPyramid(n)