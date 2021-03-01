x= int(input())
num = 0
while x!=0 :
    num = num + x % 10
    x = int(x/10)
print(num)