#rot13
def rot13(str):
    finalstring=''
    for i in str:
        if i.isupper():
            finalstring+=chr(65 + (ord(i) -65 +13)%26)
        elif i.islower():
            finalstring+=chr(97 +(ord(i) -97 +13)%26)
        else:
            finalstring+=chr(i)
    print( finalstring)

rot13("jgsPGS")
        

    