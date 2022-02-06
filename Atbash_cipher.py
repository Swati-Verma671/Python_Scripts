##Atbash Cipher Encryption or Decryption
def encrypt(text):
    ans=''
    for char in text:
        
        if char.isalpha():
            if char.islower():
                n=ord('z')+ ord('a') 
                ans+=ans.join([chr(n-ord(char))])
            else:
                N= ord('Z')+ord('A')
                ans+=ans.join([chr(N-ord(char))])

        elif char.isdigit():
            ans+=(char)
       
        
    return ans



##welcome
print("Welcome to Atbash cipher.\n ")
text=input("Please input the text.\n")

##output
print(encrypt(text))

    
    





