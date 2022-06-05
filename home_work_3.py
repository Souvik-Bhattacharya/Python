starting = int(input())
ending = int(input())
L = []
for i in range(starting,ending+1):
    L.append(i)
#print(L)
K = []
for i in range(2,ending):
    for j in range(2,ending):
        M = (i*j)
        K.append(M)
#print(K)
for i in L:
    if i in K:
        print(i)