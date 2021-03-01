n = input('Please enter an integer n, n > 2:')
n = int(n)
a = range(0, n+1)
prime = []
a = list(a)
for x in range(2,int(n**0.5)):
    for y in range(2,int(n/x)+1):
        a[x*y] = -1
for x in range(1, n+1):
    if a[x] != -1:
        prime.append(x)
print('All the prime numbers smaller than %d are:'%n,prime)
#筛法
n = input('Please enter an integer n, n > 2:')
n = int(n)
prime = []
for x in range(1, n+1):
    mark = 1
    for y in range(2, int(x**0.5)+1):
        if x%y == 0:
            mark = 0
            break
    if mark == 1:
        prime.append(x)
print('All the prime numbers smaller than %d are:'%n,prime)
#枚举法
