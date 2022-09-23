from nltk import ngrams
def generator(string,key):
    if len(string)==len(key):
        return key
    else:
        for i in range ( len(string)- len(key)):
              key= key+(key[i%len(key)])
        return ("".join(key))

def ciher(string,key):
    cpher=[]
    length=len(string)
    key_length=len(key)
    #print(length,key_length)
    for i in range(length):
       # print(string[i], ":", key[i], end="    ")
      #  print(string[i],key[i])
        x=(ord(string[i])+ord(key[i]))%26
        #print(x)
        x=x+ord('A')
        #print(x)
        cpher.append(chr(x))
    cpher="".join(cpher)
    return cpher


def decpher(ct,key):
    org=[]
    for i in range(len(ct)):
       # print(ct[i],":",key[i],end="    ")
        x=x = (ord(ct[i]) - ord(key[i] )+26) % 26
        # if ord(ct[i])>ord(key[i]):
        #    x = (ord(ct[i]) - ord(key[i] )) % 26
        # else:
        #     x = (ord(key[i]) - ord(ct[i])) % 26
        x=x+ord('A')
        org.append(chr(x))
    org="".join(org)
    return org





string=input("Enter a password")
key=input("Enter a key you want to use" )
key=generator(string,key)
string=string.upper()
key=key.upper()
#print(key)
ct=ciher(string,key)
n_grams = ngrams(ct.split(),3)
for grams in n_grams:
    print(grams)




#print(ct)
#print(decpher(ct,key))



