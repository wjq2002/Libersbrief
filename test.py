import matplotlib.pyplot as plt
import random

num = []
sum = []
P_up = []
for i in range(1, 5001):
	x = random.randint(1, 6)
	num.append(x)
sum_up = 0
for i in range(1, 5001):
	x = num[i-1]
	if x < 3:
		sum_up += 1
	P_up.append(sum_up/i*1.0)
	sum.append(i)
plt.plot(sum, P_up)
plt.show()
