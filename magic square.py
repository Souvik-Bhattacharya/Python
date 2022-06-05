def Magic_Square(n):
    
    magicsquare=[]
    for i in range(n):
        L=[]
        for j in range(n):
            L.append(0)
        magicsquare.append(L)
        
    i=n//2
    j=n-1
    num=n*n
    count=1
    
    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(magicsquare[i][j]!=0):
             j=j-2
             i=i+1
             continue
        else:
            magicsquare[i][j]=count
            count+=1
        i=i-1
        j=j+1
        
    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j],end=" ")
        print()
    print("THE VALUE OF THE SUM OF THE ROW/COLUMN/DIAGONAL = "+ str(n*(n**2+1)/2))

Magic_Square(3)
        
