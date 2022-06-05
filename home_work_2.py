s=input()
l=list(s)
n=int(l.count('#'))
a=[]
for i in range(len(l)):
    if(l[i]=='#'):
        a.append(i)
#print(a)
N=int(len(a))
I1=int(a[0])
b=[]
b.append(l[:I1])
if(n>1):
    for i in range(N-1):
        p=int(a[i])
        q=int(a[i+1])
        b.append(l[p+1:q])
        #print(b)
    #print(b)
    c=int(a[n-1])
    b.append(l[c+1:])
else:
    b.append(l[I1+1:])
#print(b)
b.sort()
#print(b)
b.reverse()
#print(b)
#print(b)
t=0    
for i in range(len(b)):
    g=b[i]
    for j in g:
        print(j,end='')
    if(t!=n):
        print('#',end='')
    t+=1