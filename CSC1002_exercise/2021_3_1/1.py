diary = '''
at 10:30 am, Kinley sent me a pdf about String via &nbsp    kinley@cuhk.edu.cn.
at 12:15 pm, &nbsp    Xiaoming treated me a superb lunch as &nbsp    promised! 
at 2:15 pm, Kinley asked me to give a &nbsp    quiz on my tutorial.
at 4:00 pm, &nbsp    Xiaoming sent the quiz questions via xiaoming@cuhk.edu.cn.
at 6:00 pm, a student told &nbsp    me he was &nbsp    desprate for a hard quiz!
'''
a = []
diary = diary.replace('at ','At ')
diary = diary.replace('&nbsp','')

a = diary.split()

for x in range(len(a)):
    print(a[x],end = ' ')
    if(x <= len(a)-2 and a[x+1] == 'At'):
        print()