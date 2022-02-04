#Caesar
def caesar(str,shift):
    finalstring=''
    for i in str:
        if i.isupper():
            finalstring+=chr(65+(ord(i)-65+shift)%26)
        elif i.islower():
            finalstring+=chr(97+(ord(i)-97+shift)%26)
        else:
            finalstring+=chr(i)

    print(finalstring)

caesar("qnzWNZ",6)
