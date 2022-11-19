# Q> Finding maximum no in a list

def getMax(l):
    i = l[0]
    for j in l:
        if j>i :
            i = j
    return i

l1 = [1,2,3,4,5,6,1,2,3,4,5,6]
r = getMax(l1)
print('Maximum no is:',r)

# Q> Rotate a list in left direction for n times

def rotate_left(l,n):
    n = n%len(l)
    if n == 0:
        return l
    else:
        temp = []
        i = 0
        while(i<n):
            temp.append(l[i])
            i+=1
        # j = 0
        # while(n<len(l)):
        #     l[j] = l[n]
        #     n += 1
        #     j += 1
        # return l[:j] + temp[:]
        return l[i:] + temp[:]

n = int(input('No of rotation:'))
l2 = [1,2,3,4,5,6,7,8]
newl = rotate_left(l2,n)
print('Rotated list is:',newl)