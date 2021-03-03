m = 'SPY CODER'

chr(ord('A')+2)

chr(65)

#Shift one letter
def shift(letter, value):
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
    
#Encode the message(m) using caesars cipher
def shift_cipher(m, value):
    secret = ''
    for c in m:
        secret += shift2(c, value)
    return secret
    
#m = 'S'
m = 'Spy Coder'
ans = shift_cipher(m,5)
print(ans)
original = shift_cipher(ans, -5)
print(original)