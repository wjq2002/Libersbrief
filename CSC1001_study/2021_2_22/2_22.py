#三种数据流
#indentation 缩进
#优先级 not > and > or

astr = 'Hello bob'
try:
    print('Bob')
    istr = int(astr)
    print('There')                  #仍然会输出Bob，但当遇到错误后则立刻执行except的语句
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)

######################################################
rawstr = input('Enter a positive number')
try:
    ival = int(rawstr)
except:
    ival = -1
    
if ival > 0:
    print('Good job')
else:
    print('Invalid number')
