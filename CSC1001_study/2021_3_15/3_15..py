a = {'a':1, 'b':2, 'c':3}

print(a.keys())
print(list(a.keys()))
print(a.values())
print(list(a.values()))
print(a.items())
print(list(a.items()))

for x,y in a.items():
    print(x,y)
    
a = [1,2,3,4,5]
a.reverse()
print(a)

print((0,1,2)<(0,1,100))
print(('a','b')<('b','a'))

a = [2,4,1,1,2,3]
b = sorted(a)
print(a, b, sep = '\n')
a.sort()
print(a)

a = {'b':1, 'a':2, 'c':3}
b = sorted(list(a.items()))
print(a, b, sep = '\n')

d = {'a':10, 'b':1, 'c':'22'}
tmp = []
for x,y in d.items():
    e = (x,y)
    tmp.append(e)
print(tmp)
tmp.sort()
print(tmp)

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