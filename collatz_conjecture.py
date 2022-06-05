def check_num(number):
    iterations = 1
    while(number!=1):
        if(number%2==0):
            number=number/2
            iterations+=1
        else:
            number=(number*3)+1
            iterations+=1
    print(number,iterations)
number=int(input())
check_num(number)