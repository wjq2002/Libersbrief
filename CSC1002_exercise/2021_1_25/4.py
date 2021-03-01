a,b = input('Please enter a and b.').split()
a , b = int(a) , int(b)
if a % b == 0:
    print('Check divides evenly into num.')
else:
    print('Check does not divid into num.')