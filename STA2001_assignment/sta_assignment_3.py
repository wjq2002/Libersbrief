import matplotlib.pyplot as plt
import random
sum = 0
pay = []
l = range(1,10001)
for i in range(10000):
    x = random.randint(1,6)
    if x <= 3:
        sum += 1
    elif x <= 5:
        sum += 2
    else:
        sum += 3
    pay.append(float(sum/(i+1)))

plt.plot(l, pay)
plt.show()

"""
The average payment the man needs to pay is 5/3 dollars.
The man can make profit if the game is repeated a large
number of times.
"""