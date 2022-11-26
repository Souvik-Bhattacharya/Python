def equilateral(n):
    for i in range(n):
        for j in range(n - i -1):
            print(' ', end = '')
        for k in range(i + 1):
            print('*', end = '')
            print(' ', end = '')
        print()
    print('\n')

def reverasedEquilateral(n):
    for i in range(n - 1, -1, -1):
        for j in range(n - i - 1):
            print(' ', end = '')
        for k in range(i + 1):
            print('*', end = '')
            print(' ', end = '')
        print()
    print('\n')

def rightpascal(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end = '')
        print()
    for k in range(n - 1, 0, -1):
        for l in range(k):
            print('*', end = '')
        print()
    print('\n')

def leftpascal(n):
    for i in range(n):
        for x in range(n - i - 1):
            print(' ', end = '')
        for j in range(i + 1):
            print('*', end = '')
        print()
    for k in range(n - 1, 0, -1):
        for y in range(n - k):
            print(' ', end = '')
        for l in range(k):
            print('*', end = '')
        print()
    print('\n')

def fullpascal(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end = '')
        for k in range(i + 1):
            print('*', end = '')
            print(' ', end = '')
        print()
    for l in range(n - 1, 0, -1):
        for x in range(n - l):
            print(' ', end = '')
        for y in range(l):
            print('*', end = '')
            print(' ', end = '')
        print()
    print('\n')

n = int(input('Enter the range:'))
equilateral(n)
reverasedEquilateral(n)
rightpascal(n)
leftpascal(n)
fullpascal(n)