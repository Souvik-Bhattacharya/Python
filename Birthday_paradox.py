import random
import datetime
l=[]
n=int(input())
for i in range(n+1):
    year=random.randint(1900,2022)
    print('Year is :',year)
    month=random.randint(1,12)
    print('Month is : ',month)
    if(year%4==0 and year%100!=0 or year%400==0):
        if(month==2):
            day=random.randint(1,29)
            print('Day is : ',day)
        else:
            if(month<=7):
                if(month%2!=0):
                    day=random.randint(1,31)
                    print('Day is : ',day)
                else:
                    day=random.randint(1,30)
                    print('Day is : ',day)
            elif(month>7):
                if(month%2==0):
                    day=random.randint(1,31)
                    print('Day is : ',day)
                else:
                    day=random.randint(1,30)
                    print('Day is : ',day)
    else:
        if(month==2):
            day=random.randint(1,28)
            print('Day is : ',day)
        else:
            if(month<=7):
                if(month%2!=0):
                    day=random.randint(1,31)
                    print('Day is : ',day)
                else:
                    day=random.randint(1,30)
                    print('Day is : ',day)
            elif(month>7):
                if(month%2==0):
                    day=random.randint(1,31)
                    print('Day is : ',day)
                else:
                    day=random.randint(1,30)
                    print('Day is : ',day)
    dd=datetime.date(year,month,day)
    dy=dd.timetuple().tm_yday
    print(dy)
    l.append(dy)
print(l)
            
    
    