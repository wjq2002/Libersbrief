n = input('Please enter a positive integer:')
n = int(n)
a = []
change = 1
num = 1
for x in range(1, n+1):
    a.append(num)
    
    if str(x).find('7')!=-1 or x % 7 ==0:
        change = change + 1
    
    if change % 2 == 1:
        num = num + 1
    else:
        num = num - 1
        
print('The %dth element in ping-pong sequence is: %d'%(n, a[n-1]))