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

