a = b = c = d = e = 0
x = 1
while x!= 0 :
    x=int(input())
    if x>0:
        a = a + 1
    if x<0:
        b = b + 1
    c=c+x
    d=d+1
e=c/(d-1)
print(a,b,c,e)