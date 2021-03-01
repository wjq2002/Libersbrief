a = 0
while  a != 'q':
    a,b = input('Please enter your names and ages, or enter q to quit: ').split()
    if a != 'q':
        b = int(b)
        print(a, ',it is ' + str(100 - b + 2021) + ' when you are 100 years old.')
    else:
        print('Goodbye!')