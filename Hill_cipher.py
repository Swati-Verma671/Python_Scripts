##hill cipher
keyMatrice=[[0]*3 for i in range(3)]

vector=[[0] for i in range(3)]

ansMatrice=[[0] for i in range(3)]

#encryptes the key
def encryptkeymatrix(key):
    k=0
    for i in range(3):
        for j in range(3):
            keyMatrice[i][j]=ord(key[k])%65
            k+=1

#encryptes the message
def encryptVector(vector):
    for i in range(3):
        for j in range(1):
            ansMatrice[i][j]=0
            for p in range(3):
                ansMatrice[i][j]+=(keyMatrice[i][p]*vector[p][j])
                ansMatrice[i][j]=ansMatrice[i][j]%26

#functioning
def encrypt(message,key):
    encryptkeymatrix(key)
    for i in range(3):#creating the message
        vector[i][0]=ord(message[i])%65

    encryptVector(vector)

    string=[]#generating the text from encryption
    for i in range(3):
        string.append(chr(ansMatrice[i][0]+ 65))

    return("".join(string))

##input
message=input("Input message: ")
key=input("Input key: ")

print("Output:",encrypt(message,key))