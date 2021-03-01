a, b, c = (int(x) for x in input().split())

d = b**2 - 4*a*c
if d<0:
    print('No')
elif d==0:
    print('x= %.2f'%((-b)/(2*a)))
else:
    print('x1=%.2f,x2=%.2f'%((-b+(b**2-4*a*c)**0.5)/(2*a),(-b-(b**2-4*a*c)**0.5)/(2*a)))