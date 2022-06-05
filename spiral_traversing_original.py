import turtle
import random
turtle.bgcolor("black")
cr=turtle.Turtle()
height=(7)
width=(5)
dot_distance=(25)
cr.penup()
cr.setpos(-250,250)
list=['white','blue','green','red','yellow','orange','pink']
col=random.randint(0,6)
cr.color(list[col])
def spiral_traversing(m,n):
    k=0
    l=0
    f=0
    #cr.color("white")
    '''
    k is starting row 
    l is starting coloumn..
    '''
    while(k<m and l<n):
        if(f==1):
            cr.right(90)
            
        for i in range(l,n):
            cr.dot()
            cr.forward(dot_distance)
            #print(a[k][i],end=" ")
        f=1
        k+=1
        cr.right(90)
        col=random.randint(0,6)
        cr.color(list[col])
        for i in range(k,m):
            cr.dot()
            cr.forward(dot_distance)
            #print(a[i][n-1],end=" ")
        
        n-=1
        cr.right(90)
        col=random.randint(0,6)
        cr.color(list[col])
        for i in range(n-1,l-1,-1):
            cr.dot()
            cr.forward(dot_distance)
            #print(a[m-1][i],end=" ")
        m-=1
        cr.right(90)
        col=random.randint(0,6)
        cr.color(list[col])
        for i in range(m-1,k-1,-1):
            cr.dot()
            cr.forward(dot_distance)
            #print(a[i][l],end=" ")
        l+=1
        
m=int(input())
n=int(input())
'''
matrix=[]
c=1
for i in range(m):
    x=[]
    for j in range(n):
        x.append(c)
        c+=1
    matrix.append(x)
'''
spiral_traversing(m,n)
turtle.done()
