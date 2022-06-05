import numpy as nm
def closestSchool(x,y,L):
  l=nm.array([x,y])
  a=[]
  for i in range(n):
    t=L[i]
    s=nm.array(t)
    diff=nm.subtract(l,s)
    sqr=nm.square(diff)
    sum=sqr[0]+sqr[1]
    distance=sum**0.5
    a.append(distance)
  print(a)
  '''
  r=[]
  r.append(a)
  p=r[0]
  p.sort()
  t=p[0]
  print(t)
  test=[]
  for i in range(len(a)-1):
      if(a[i+1]<a[i]):
          test.append(a[i+1])
      else:
          test.append(a[i])
  test.sort()
  print(test)
  #g=len(test)-1
  '''
  g=sorted(a)
  print(g)
  t=g[0]        
  print(t)
  print(a)
  for j in range(len(a)):
    if(a[j]==t):
      print(L[j])
      
x,y = map(int, input().split())

n = int(input())
L = []
for i in range(n):
    l = list(map(int, input().split()))
    L.append(l)
closestSchool(x,y,L)