import string
m = 'SPY CODER'

chr(ord('A')+2)

chr(65)

#Shift one letter,Uppercase only
def shift(letter, value):
    return shift3(letter, value)
    if letter.isupper():
        ch = chr(ord(letter)+value)
        if(ch>'Z'):
            ch = chr(ord(letter)+value-26)
        if(ch<'A'):
            ch = chr(ord(letter)+value+26)
        return ch
    return letter


def shift2(letter,value):
    
    if letter.isalpha():
        ch = chr(ord(letter.upper())+value)
        if(ch>'Z'):
            ch = chr(ord(letter)+value-26)
        elif(ch<'A'):
            ch = chr(ord(letter)+value+26)
        
        return ch if letter.isupper() else ch.lower()
    
    return letter

#Custom only, but in one case only
def shift3(letter, value, alpha = string.ascii_uppercase):
    if letter in alpha:
        idx = (alpha.find(letter) + value) % len(alpha)
        return alpha[idx]
    return letter

#Encode the message(m) using caesars cipher
def shift_cipher(m, value):
    secret = ''
    for c in m:
        secret += shift3(c, value, 'ABC')
    return secret

#m = 'S'
m = 'SPY CODER'
ans = shift_cipher(m,5)
print(ans)
original = shift_cipher(ans, -5)
print(original)