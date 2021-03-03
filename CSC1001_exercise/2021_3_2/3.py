def C(a,b):
    if b == 0:
        return 1
    ans =1
    for x in range (a-b+1,a+1):
        ans*=x
    for x in range(1,b+1):
        ans/=x
    return int(ans)

n = int(input('Enter n:'))
for x in range(1,n+1):
    print(' '*(n-x+1),sep = '',end = '')
    for y in range(1,x+1):
        print(C(x-1,y-1),' ',sep = '',end = '')
    print() 