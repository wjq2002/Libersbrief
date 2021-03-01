import random
import matplotlib.pyplot as plt

def C(a,b):
    ans = 1.0
    for x in range(b):
        ans*=(a-x)
    for x in range(1,b+1):
        ans/=x
    return ans

n = 1000
N = 100
group = [0,1,2,3,4,5]
number = [0,0,0,0,0,0]
fre = []
m=mark=0
num = []

for x in range(6):
    fre.append(C(50,x)*C(50,5-x)/C(100,5))

while m<=n:
    mark=0
    num = []
    num = list(range(1,N+1))
    for x in range(5):
        a = random.choice(num)
        #print(a)
        if a>=1 and a <= 50:
            mark+=1
        num.remove(a)
    number[mark]+=1
    m+=1

plt.figure(figsize=(10,8),dpi=80)
plt.bar(group,[x/1000 for x in number],label = 'Frequency histogram of X')
plt.plot(group,fre,'r.-',label = 'Theoretical frequency of X')
plt.legend()
plt.show()