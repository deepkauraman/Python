def  encrypt(string,key):
    ciher=[]
    for i in range(len(string)):
        if ord(string[i])==32 or ord(string[i])==44:
            ciher.append(string[i])
            continue
        else:
            ch=ord(string[i])-ord('A')
            cchar= (ch+key)%26+65
            ciher.append(chr(cchar))
    ciher="".join(ciher);
    return ciher
def decrypt(cipher,key):
    pt=[]
    for i in range(len(cipher)):
        if ord(string[i]) == 32 or ord(string[i]) == 44:
            pt.append(string[i])
            continue
        else:
             ch = ord(cipher[i]) - ord('A')
             cchar = (ch - key) % 26 + 65
             pt.append(chr(cchar))
    pt = "".join(pt);
    return pt


string=input("enter data you want to encrypt")
string=string.upper();
key=int(input("enter key"))
print(ord(","))
ciphertext=encrypt(string,key)
print(ciphertext)
pt=decrypt(ciphertext,key)
print(pt)


