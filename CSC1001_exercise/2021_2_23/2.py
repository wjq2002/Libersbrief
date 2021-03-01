day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
x, y=(int(x) for x in input().split(','))
if x!=2:
    print(day[x])
else:
    if(y%4==0):
        if(y%400==0):
            print(29)
        else:
            print(28)
    else:
        print(28)