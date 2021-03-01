x = int(input())
y = 2
while x!= 1 :
    if x%y==0:
        print(y,'\n')
        x = int(x / y)
        continue
    y=y+1