from functools import reduce
nums = []
def prompnumbers():
    idx = 1
    while True:
        prompt = 'enter number' + str(idx) + ': '
        n = input(prompt)
        if n == 'x':
            break
        try:
            n = eval(n)
            if type(n) in (int, float):
                nums.append(n)
                idx += 1
        except:
            continue
        
# def compute(nlist,c = max):
#     ans = nlist[0]
#     for x in nlist:
#         ans = c(x,ans)
#     print(ans)

def compute(nlist,c = max):
    ans = reduce(c,nlist)
    print(ans)

def large(a,b):
    return a if a[1]>b[1] else b

def small(a,b):
    return a if a[1]<b[1] else b

# prompnumbers()
# compute(nums)
# compute(nums , min)

data = (('a',20),('b',18),('c',17),('d',14),('e',22))
compute(data,large)
compute(data,small)