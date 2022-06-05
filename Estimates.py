import matplotlib.pyplot as plt
from statistics import mean
from scipy import stats
l=[3,7,8,26,38,49,25,50,37,38,29,57,60,48,30,17,30,25,17,45,18,19]
l.sort()
M=mean(l)
print('Mean is :',M)
m=stats.trim_mean(l,0.1)
print('Trim_Mean is :',m)
plt.plot(l,'bs')
plt.show()
y=[]
for i in range(len(l)):
    y.append(5)
plt.plot(l,y,'r--')
plt.plot([30.5],[5],'g^')
plt.show()
