num , num_a , num_b , num_c , num_d = ([] for i in range(5))
                                #在一行初始化多个列表

a=9.99909999                    #保留小数位数的几种方法
print(format(a,'.5f'))
print('%.5f'%a)                 #这两种会四舍五入
print(int(a*100000)/100000)     #不会四舍五入，直接截断
                                
a , b = (5555 ,6666)
print('%8d%8d'%(a, b))           #输出空格直到末尾达到八位后输出a，再输出空格直到末尾达到八位后输出b
print('%-8d%-8d'%(a, b))        #输出a后直到头达到8位后输出b,再隔8位
                                #数字代表两个输出头与头之间的距离

a = 1.23
print('%f'%a)                   #默认输出六位小数

print('\'')
print('\"')                     #输出单引号与双引号


print(4 * 'test')               #输出一个字符串多次可以直接使用乘号


print('\x55')                   #是 16 进制的意思，后边跟两位，则表示单字节编码(ASCII)
print('\u0100')                 #其后跟 4 个 16 进制数 , 表示 unicode 码


s = '\temp\spam'                #字符中含有\t
print(s)
#输出         emp\spam
s = r'\temp\spam'               #忽视字符中的 \ 字符
print(s)
#输出 \temp\spa


x = 1
y = 2.2
print("The length of %s is %d" % (x,y))
                                #使用百分号指名数据类型，并在逗号后指名具体变量
"""
%d 申明整数变量
%f 申明浮点数变量
$s 申明字符串或数字变量，要用type()函数查询数据类型
"""


a = [5, 10, 15, 20, 25, 30, 35, 40]
print(a[1:2:1])                 #a[b,c,d] 三元组表示：从第b位开始，第c位结束，步长为d
#输出 [10]                      #不会输出 c 处的元素
print(a[4:1:-1])                #若 d < 0 ，则形成倒序输出, 要求 b > c ,
#输出 [25, 20, 15]              #不会输出 c 处的元素


for i in range(1,12,2): print(('p'*i).center(11))
"""
     p                          #输出一棵圣诞树
    ppp
   ppppp
  ppppppp
 ppppppppp
ppppppppppp                     #print().center(a)表示输出时以 a/2 (向下取整)为中心

for i in range(1,12,2): print(('p'*i).center(5))

  p                             #输出时以 2 为中心
 ppp
ppppp
ppppppp
ppppppppp
ppppppppppp
"""
s = '12345'
result = s.isdigit()            #判断 s 是不是数字，并返回布尔值
print(result)                   #输出True


s = "This is not spam"
print(s.endswith('spam'))       #判断字符串是否以某个字符串结尾，并返回布尔值
                                #输出True

print('‐'.join('new spam'))     #将'-'字符添加到字符串或列表中
print('‐'.join(['apple','orange','grape']))
                                #输出 n‐e‐w‐ ‐s‐p‐a‐m
                                #     apple‐orange‐grape   


print('apple'.rjust(10,'‐'))    #用'-'字符使字符串右对齐到10的位置
#输出 
# -----apple


print('apple'.find('app'))
print('apple'.find('le'))
print('apple'.find('c'))        #寻找字符串在字符串的位置。若找不到，则返回 -1
"""
输出：
0
3
-1
"""


print('apple‐orange‐grape'.split('‐'))
                                #删去所有的'-'字符并返回列表
#输出 ['apple', 'orange', 'grape']
print('apple‐orange‐grape'.partition('‐'))
                                #找到第一个'-'字符并保留，将字符串分为三部分，并返回一个三元的元组
#输出 ('apple', '‐', 'orange‐grape')


s3 = 'one two three'
print(s3.rstrip('e'))
print(s3.rstrip('er'))
print(s3.rstrip('erh'))
print(s3.rstrip('erht'))
print(s3.rstrip('erhto'))
print(s3.rstrip('erht o'))      #删除末尾的字符
"""
输出
one two thr
one two th
one two t
one two
one two
one tw
"""

s3 = 'one two three one'
print(s3.replace('one','ten'))  #替换字符串中的元素
#输出 ten two three


#使用format函数将字符串中的{}替换为变量
print("{} {}".format("hello", "world")) # 不设置指定位置，按默认顺序
#输出   'hello world'

print("{0} {1}".format("hello", "world"))      # 设置指定位置
#输出   'hello world'

print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
#输出   'world hello world'

l = [1,2,3]
print(l)
l.insert(0,[9])                         #insert(a,b)在a位置插入b元素
print(l)
l.insert(0,9)
print(l)
"""
[1, 2, 3]
[[9], 1, 2, 3]                          #相当于在列表中嵌套了一个[9]列表
[9, [9], 1, 2, 3]
"""


a = 'a'
try:
  int(a)
except:
  print('It is not an integer.')        #尝试执行一段代码，并替换输出错误信息

S = 'spam'
print([c*2 for c in S])
#输出 ['ss', 'pp', 'aa', 'mm']  列表

num = [ int(x) for x in num ]           #将列表字符转为数字

print(ord('A'))                         #查看ASCII码
print(chr(65))                          #将ASCII码转为字符


a ,b, c = ( int(x) for x in input().split())
#输入的字符以空格隔开，形成一个列表，可以使用多个变量来储存列表的元素

mystr = 'today'
mylist = list(mystr)
print(mylist)

x = range(1,8)
x = list(x)
print(x)
#list 函数将字符串转为列表,但是不能将数字转为列表,只能将range转为列表

mylist = [1, 2, 3]
dir(mylist)
#使用dir函数查看变量的操作

help(mylist.remove)
#使用help函数查看帮助

mylist = [7, 34, 1, 25, 13]
mylist.sort() 
#正序排序
mylist.sort(reverse = True)
#反序排序

S = [x**2 for x in range(1,13)]
print(S)
#使用for语句快速定义列表

N = [x for x in S if x % 2 ==0]
print(N)
#for和if语句的配合使用                                  
#当定义一个列表，即只有一个变量时，应该使用中括号，
#而想要把一个列表的元素赋给多个变量时，要使用小括号
#a, b, c = (x for x in range(1,4))
#print(a,b,c)

X = []
for x in range(1,13):
  X.append(x**2)
print(X)
#使用append函数构造列表

print('a','b',sep = '*',end = '!')

#sep = '*' 表示元素间用*字符隔开，end = '!' 表示输出结束后用'!'结尾，否则默认以空格为sep隔开，以回车为end结尾

exec ('print("Hello World")')
exec ('def xx():print("hahaha")')
exec ('xx()')
#exec 执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。

from functools import reduce
def add(x, y) :            # 两数相加
    return x + y
sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
print(sum1)
print(sum2)
#reduce函数对给定的函数和数据进行迭代计算

a = [1,2,3,4]
v =''.join([str(x) for x in a])
print (v)
#join函数将列表的字符元素转为字符串

#*
#!
#?
#TODO
#@param value    不同颜色注释

# ctrl+alt+z     自动对齐

import random
num = list(range(1,101))
random.choice(num)
#从列表中随机取一个元素

#!删除列表元素的几个方法
num.remove(10)
#可以将列表中的第一个num移出列表，若要移出多个，需要循环

str = [0,1,2,3,4,5,6]
a = str.pop(1)
str2=['abc','bcd','dce']
str2.pop(2)
#删除列表指定位置的元素，并返回这个元素的值，可以用变量储存这个元素的值

str=[1,2,3,4,5,2,6]
del str[1]
del str[2:4] #删除从第2个元素开始，到第4个为止的元素(但是不包括尾部元素)
del str      #del 也可以删除整个数据对象(列表、集合等)

#!删除元素的变相方法
s1=(1,2,3,4,5,6)
s2=(2,3,5)
s3=[]
for i in s1:
    if i not in s2:
        s3.append(i)
print (s3)
#输出 s1-s2 的结果

str = '12312414'
str.find('12', 0, 5)
#find函数用于寻找字符串中的元素
#第一个参数表示检索的字符串，第二个参数表示从第几位开始检索，第三个参数表示到第几位停止检索(对应下标，从0开始)
S = 'abc123abc'
S.find('ab')        #输出0
S.find('ad')        #输出-1（不存在）
S.rfind('ab')       #从右向左寻找元素，输出6
S[S.rfind('a')]     #套娃，输出a

a = '12312314 12313'
a.split()           #将字符串隔开，形成列表
list(a)             #将字符串的每一位都加入列表元素

''.join(S)          #将S的每个元素组合形成字符串
'-'.join(S)         #将S的每个元素组合形成字符串，并用'-'隔开

S = 'I aM herE'
S.upper()           #将字符串的每个字母都变成大写字母
S.lower()           #将字符串的每个字母都变成小写字母
S.capitalize()      #将字符串的首字母大写，其余权威全为小写
S.title()           #将字符串的每个单词首字母大写，其余小写

S='''
fuck       
'''
print(S)            #输出三行内容

name = 'Xiaoming'
institute = 'CUHK(SZ)'
example = f'{name} is a from {institute}'
print(example)
#使用f''+{}将字符串中的内容替换为别的字符串

for i in range(5):
    if i == 3:
        pass            #占位符，什么都不做
    print(i)

print('tab')            #输出制表符
print('spaces')         #输出4个空格


def fun():
    print('hello')
    return
def fun_():
    print('hello')
def fun__():
    print('hello')
    return 3
print(fun())
print(fun_())
print(fun__())
#只有指定return非0数时，才会得到非none的值


from math import sin

fun = 'sin'
x = int(input())
exec(f'y = {fun}(x)')
print(y)
#使用exec函数和f'{}'技巧，使得不需要if，就能直接将函数名用于语句中

ord('S')
chr(65)
#ASCII 码与字符转换

handle = open('D:\python_work/Document/test.txt','r')
# alltext = handle.read()
# print(len(alltext))
# print(alltext[:20])

# for line in handle:
#     print(line,end = '')
for line in handle:
    if line.startswith('2'):                    #判断行开头是不是'2'
        print(line,end = '') 
handle.close()

handle = open('D:\python_work/Document/test.txt','w')
handle.write('233\n666 666\n999 999 999')       #write的内容只能是string

a = '1234'
#a[1] = '3'                  #! str不能改变元素的值
a = list(a)
a[1] = '3'
b = ''.join(a)               #join只能用于字符，不能用于数字和列表
print(b)                     #先将字符串转成列表，再修改列表值，再join为字符串


def print_inf(a, *b):       # *加上变量代表传递给变量的值是一个元组
    print(a,end=' ')
    for x in b:
        print(x,end = ' ')
    print(b)
    print()
print_inf(1)                #r若没有给元组赋值，则会存在一个空元祖
print_inf(1,2,3,4,5)


def print_map(**map_):      #**加上变量代表传递给变量的值是一个字典
    print(map_)
print_map(john=10, jill=12, david=15)


def foo():
    a = 1
    b = 2
    return a, b             #一个函数可以返回多个值，这些值会被打包在一个元组中
print(foo())

a = 'Hello, man'
a = a.replace('man', 'boy')
print(a)                    #替换字符串的片段，输出hello，boy


a= {'Alice':18,'Csg':3}
print(a['Csg'])
print(a.get('Csg','fuck'))
print(a.get('Wjq','good'))
#get函数从字典中找到键的值。如果找到了，则返回键对应的值，否则返回逗号后的内容

name="Csg"
def change_name(name):
    name="Wjq"              #局部变量
    print (name)            #这打印的是局部变量
change_name(name)           #这里函数调用的是局部变量的name
print (name)                #这里是是调用的函数外面的全局变量

#! 未加申明时，出现赋值语句则代表申明了变量，如函数中申明的name就是函数中的局部变量
#! 如果要使用全局变量，需要使用 global 语句对变量进行申明

name = 'Csg'
def change_name_():
    global name
    name = 'Wjq'
    print(name)
change_name_()
print(name)                  #此时name的值发生了变化


if not l:
        # 如果l不为空的话,就执行if内语句，为空就不执行
        l = []

        
def bad_foo(item, my_list=[]):
    print(id(my_list))
    my_list.append(item)
    return my_list
print (bad_foo('a'))
print (bad_foo('b'))
print (bad_foo('c'))
#! 参数默认值潜在的危害,会造成列表缓存
"""
按我们常规的理解，上面的输出结果应该是[‘a’]，[‘b’]和[‘c’]，
而不是[‘a’]，[‘a’, ‘b’]和[‘a’, ‘b’, ‘c’]。
这是由于函数参数的初值只会在函数定义的时间里计算一次。
所以，在第二次调用函数时，my_list=[]不会再被执行，
此时my_list已经不在等于[]，而是等于[‘a’]，以此类推。
"""
print (bad_foo('a',[]))
print (bad_foo('b',[]))
print (bad_foo('c',[]))
#! 因此最好在传递给函数空列表是，也注明初始变量
#! 或者如下修改函数
def bad_foo(item, my_list = None):
    if my_list == None:
        my_list = []
    print(id(my_list))
    my_list.append(item)
    return my_list
print (bad_foo('a'))
print (bad_foo('b'))
print (bad_foo('c'))


#! 与向函数传递列表有关的问题
def add(l1,l2):
    print(id(l1))
    l1=l1+l2
    print(id(l1))

def add_(l1,l2):
    print(id(l1))
    l1.append(l2)
    print(id(l1))

l1 = [1,2,3,4]

add(l1,[2])
print(l1)
# 当涉及列表整体运算或赋值时，函数会申明局部变量（发现l1的id发生变化）
add_(l1,2)
print(l1)
# 当仅仅对列表进行单项赋值或添加元素时，不会申明局部变量，而是共用同一个id

a = {'a':1, 'b':2, 'c':3}
# 通过keys，values，items函数返回字典的键，值，键值对，其中键值对是以元组的形式返回
print(a.keys())
print(list(a.keys()))
print(a.values())
print(list(a.values()))
print(a.items())
print(list(a.items()))

# 使用双变量输出键，值
for x,y in a.items():
    print(x,y)
    
# reverse函数将列表反序
a = [1,2,3,4,5]
print(a[::-1])
a.reverse()
print(a)

# 比较元组的大小，按位比较
print((0,1,2)<(0,1,100))
print(('a','b')<('b','a'))

# sorted 和 sort函数
a = [2,4,1,1,2,3]
b = sorted(a)
print(a, b, sep = '\n')
a.sort()
print(a)

# 将字典排序
a = {'b':1, 'a':2, 'c':3}
b = sorted(list(a.items()))
print(a, b, sep = '\n')

# 将字典备份同时排序
d = {'a':10, 'b':1, 'c':'22'}
tmp = []
for x,y in d.items():
    e = (x,y)
    tmp.append(e)
print(tmp)
tmp.sort()
print(tmp)

# 统计一个文件中出现次数前十的字符
a = open('D:\python_work/CSC1001_study/2021_3_15/test.txt')
b = {}
for line in a:
    words = line.split()
    for word in words:
        b[word] = b.get(word, 0) + 1
lst = []
for x,y in b.items():
    lst.append((y,x))
lst.sort(reverse=True)
for x,y in lst[:10]:
    print(x,y)

