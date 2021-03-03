def reverse(number):
    global b
    b = number[::-1]
    return isPalindrome(number)
def isPalindrome(number):
    if b == number:
        return True
    else:
        return False


n = input('Please enter a integer number.')

print(reverse(n))

"""
def reverse(number):
    reversenumber = 0
    while number!=0:
        ```
    return reversenumber
def 
"""