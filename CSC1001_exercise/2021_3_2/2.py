def is_prime(number):
    for x in range(2,int(number/2)+1):
        if(number%x == 0):
            return False
    return True

def is_hui(number):
    a = number
    b = 0
    while(a>0):
        b = b*10 + a%10
        a //= 10
    if(b == number):
        return True
    else:
        return False
line = num = 0
mark = 2
while num<=100:
    if(is_prime(mark) and is_hui(mark)):
        print(mark,end = ' ')
        line += 1
        num+=1
        if(line %10 == 0 and line != 0):
            print()
    mark+=1
