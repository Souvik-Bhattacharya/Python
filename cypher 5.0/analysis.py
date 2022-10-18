N = int(input())
M = int(input())
l = []
for i in range(N):
    a = []
    a = [x for x in input().split()]
    l.append(a)
max = -1
s = ''
for i in range(N):
    if (int(l[i][1]) < M):
        if (int(l[i][1]) > max):
            max = int(l[i][1])
            s = l[i][0]
if s != '':
    print(s,max)
else:
    print(-1)
# A = [1,2,8,10,12,19]
# N = len(A)
# X = 11
# max = -1
# for i in A:
#     if i <= X:
#         if i > max:
#             max = i
# print(max)