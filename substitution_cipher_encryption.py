#substitution cipher

#encryption
def encrypt(text,key):
    encrypted=""
    
    for i in text:
        n=ord(i)
        if n==32:
            encrypted+=" "
            continue
        char=n+key
        if 90<char<97:
            ciphered=(chr(char-26))
        elif(char>122):
            ciphered=(chr(char-58))

        else:
            ciphered=chr(char)
        
        encrypted+=encrypted.join(ciphered)
    return encrypted


#input
plainTxt=input("Please enter the text to be encrypted: ")
key=int(input("Please provide a key: "))


#output
print(encrypt(plainTxt,key))