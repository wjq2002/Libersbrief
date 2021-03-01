import matplotlib.pyplot as plt
import random
num , num_a , num_b , num_c , num_d = ([] for i in range(5))
a = b = c = d = 0
l = range(1,100001)
for i in list(l):
    x = random.randint(1 , 18)  
    if x <= 8:
        d +=1
        if x <= 2:
            a += 1
        elif x <= 3:
            b += 1
        elif x <= 8:
            c += 1
    if d == 0 :
        num_a.append(0)
        num_b.append(0)
        num_c.append(0)
    else: 
        num_a.append(a/d*1.0)
        num_b.append(b/d*1.0)
        num_c.append(c/d*1.0)
    num_d.append(d/i*1.0)

plt.plot(l , num_d , label = 'P(R)', color = 'purple')
plt.plot(l , num_a , label = 'P(B1|R)', color = 'red')
plt.plot(l , num_b , label = 'P(B2|R)', color = 'green')
plt.plot(l , num_c , label = 'P(B3|R)', color = 'blue')
plt.legend()
plt.show()