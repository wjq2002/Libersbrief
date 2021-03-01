a = input('Please a string: ')
b = 1
for i in range(len(a)):
    if a[i] != a[len(a)-i-1]:
        print('This string is not a palindrome!')
        b = 0
        break
if b != 0:
    print('This string is a palindrome!')
"""
wrd = input("Please enter a word: ")
rvs = wrd[::‐1]             #生成回文序列
print(rvs)
if wrd == rvs:              #比较原序列和回文序列是否相同
print("This word is a palindrome.") #回文
else:
print("This word is not a palindrome.")

"""