from os import PathLike


class Sequence:
    def __init__(self): 
        self.x = 0
      
    def __next__(self): 
        self.x += 1
        #if self.x > 14:
        #raise StopIteration
        return self.x**self.x
    def __iter__(self):
        return self

s = Sequence()
n = 0
for e in s:
    print(e)
    n += 1 
    if n > 10:
        break


# r表示只读    
f = open('D:\python_work/CSC1001_study/2021_3_15/test.txt','r')
#read函数默认从最开始读取全部
f.read()
print(f.read(3))        #read(3)代表从光标位置往后读取3位
f.seek(0)               #seek(n)代表把光标移动到n的位置
print(f.readline())     #代表读取一行的内容
print(f.readlines())    #代表读取全部内容，并将每一行的内容存在列表中
f.close()

# w代表写入
f = open('D:\python_work/CSC1001_study/2021_3_15/test.txt','w')
f.write('one\n')
f.writelines(['two\n', 'three'])# writelines 可以将列表写入文件
f.close()
# 使用with函数进行调用open
with open('D:\python_work/CSC1001_study/2021_3_15/test.txt','r') as f:
    while True:
        line = f.readline()
        if not line:    #判断是否为空
            break
        else :
            print(line)
            
# 使用StopIteration输出3的倍数
n = (e for e in range(50000000) if not e % 3)
i = 0
for e in n:
    print(e)
    i += 1
    if i > 100:
        #raise StopIteration
        break

# 生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(10)
def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b             #! 使用yield函数能够减少内存使用，同时提高函数简洁度
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fib_g(6):
    print(n)

# 简单地讲，yield 的作用就是把一个函数变成一个 generator，
# 带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
# 调用 fib_g(5) 不会执行 fib_g 函数，而是返回一个 iterable 对象！
# 在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，
# 执行到 yield b 时，fab 函数就返回一个迭代值，
# 下次迭代时，代码从 yield b 的下一条语句继续执行，
# 而函数的本地变量看起来和上次中断执行前是完全一样的，
# 于是函数继续执行，直到再次遇到 yield。

#! 使用lambda 模块编写简易函数
# 变量名 = lambda   ：   冒号左侧申明变量，右侧申明表达式
add = lambda a, b : a + b
print(add(1,2))
fn = lambda x : x**2
print(fn(3))
print((lambda x : x**2)(3))
print((lambda x : [x*_ for _ in range(5)])(3))

#使用lambda模块对多元素列表的不同位置元素进行排序
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda x : x[0])
print(pairs)
pairs.sort(key = lambda x : x[1])
print(pairs)