import hashlib

##changing the str to bytes
def encoding(password):
    password=password.strip()##removing spaces if any.
    encodedMessage=password.encode("utf-8")
    return(encodedMessage)

##md5 hash encoding
def md5(encodedMessage):
    return(hashlib.md5(encodedMessage).hexdigest())

##s256 hash encoding
def s256(encodedMessage):
    return(hashlib.sha256(encodedMessage).hexdigest())

##s512 hash encoding
def s512(encodedMessage):
    return(hashlib.sha512(encodedMessage).hexdigest())

##s224 hash encoding
def s224(encodedMessage):
    return(hashlib.sha224(encodedMessage).hexdigest())

##s384 hash encoding
def s384(encodedMessage):
    return(hashlib.sha384(encodedMessage).hexdigest())

##s3_256 hash encoding
def s3_256(encodedMessage):
    return(hashlib.sha3_256(encodedMessage).hexdigest())

##s3_512 hash encoding
def s3_512(encodedMessage):
    return(hashlib.sha3_512(encodedMessage).hexdigest())

##welcome message
print("Welcome to hash cipher key.\n Enter M for md5 encoding, S256 for sha256 encoding, S512 for sha512 encoding, S224 for sha224 and S384 for sha384 encoding.\n Use S3_256 for sha-3-256 and S3_512 for sha-3-512.\n")
key=input("Please enter the code: ")
textPassword=input("Please input the string: ")

##checking the codes
if (key!="M"|key!="S256"|key!="S512"|key!="S224"|key!="S384"|key!="S3_256"|key!="S3_512"):
    print("Please only give the codes mentioned above.")


##outputs
if(key=="M"):
    passwordString=encoding(textPassword)
    output=md5(passwordString)
    print("MD5 encoding:",output)

elif(key=="S256"):
    passwordString=encoding(textPassword)
    output=s256(passwordString)
    print("SHA-256 encoding:",output)

elif(key=="S512"):
    passwordString=encoding(textPassword)
    output=s512(passwordString)
    print("SHA-512 encoding:",output)

elif(key=="S224"):
    passwordString=encoding(textPassword)
    output=s224(passwordString)
    print("SHA-224 encoding:",output)

elif(key=="S384"):
    passwordString=encoding(textPassword)
    output=s384(passwordString)
    print("SHA-384 encoding:",output)

elif(key=="S3_256"):
    passwordString=encoding(textPassword)
    output=s3_256(passwordString)
    print("SHA-3-256 encoding:",output)

elif(key=="S3_512"):
    passwordString=encoding(textPassword)
    output=s3_512(passwordString)
    print("SHA-3-512 encoding:",output)