m = int(input())
for x in range(1,m+1):
    print(' '*(m-x),end='')
    n=x
    while n>=1:
        print(n,end='')
        n-=1
    n+=2
    while n<=x:
        print(n,end='')
        n+=1
    print()