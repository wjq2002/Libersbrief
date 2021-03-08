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
