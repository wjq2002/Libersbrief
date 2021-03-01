from typing import SupportsComplex


a , b = (int(x) for x in input('Please enter your working hours and hourly rate:').split())
if a > 40:
    c = (a - 40)*1.5*b + 40*b
else:
    c = a*b

print('Your salary is: %.2f'%c)