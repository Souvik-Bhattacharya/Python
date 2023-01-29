# importing the timeit function
import timeit
# defining function isKaprekar
def isKaprekar(number):
    # checking if the number is 1
    if number == 1:
        # returning true if the number is 1
        return True
    # making square of the given number
    sqr = number**2
    # making a copy of the squared number
    copy = sqr
    # initializing the count variable by 1
    count = 0
    # running a loop until the copy is having 0 for getting the length of the number
    while copy > 0:
        # truncating the LSB of the number
        copy = copy // 10
        # incrementing the count variable
        count += 1
    # here the point of partition in the squared value is traversing from left to right and checking the equality of the sum of both sides of that partition
    for i in range(1, count):
        # checking if the number is 10 or its multiple
        if number == 10 ** i:
            break
        # checking if the sum of the right section and the left section is equal to the number 
        if number == (sqr // 10**i + sqr % 10**i):
            return True
    # if equality is not found returning false
    return False

# taking the range of finding the kaprekar number
n = int(input('Give the range:'))
# iterating every number from 1 to the upper limit
for number in range(1, n + 1):
    # checking if the number is kaprekar or not
    if isKaprekar(number):
        # printing the number if it is kaprekar number
        print(number, end = ' ')
# printing the execution time by using timeit function
print('\nTime taken :',timeit.timeit())