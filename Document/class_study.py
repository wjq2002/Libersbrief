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