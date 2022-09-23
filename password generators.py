import random
plength=int(input("how long the password you want"))
if plength==0:
    print("kindly re run the progtam as the password you want is of 0 length")
    exit(0)
schar=int(input(f"how many special character you want out of {plength}\n"))
if schar>plength:
    print("kindly re run a program as the special characters are exceeding the length")
    exit(0)
elif schar< plength:
    pnum=plength-schar
else:
    pnum=0
num=int(input(f"how many numbers you want{pnum} \n"))
if num>pnum:
    print("kindly re run a program as the exceeding are exceeding the length ")
    exit(0)
schar_list=['@','#','$','_','*','-','!']
character=[]
for i in range(97, 123):
    character.append(chr(i))
for i in range(65, 91):
    character.append(chr(i))
#print(character)
s=[]
for i in range(schar):
    s.append(schar_list[random.randint(0,6)])
print(s)
for  i in range(num):
    s.append(random.randint(0,9))
print(s)
rchar=plength-schar-num
for i in range(rchar):
    s.append(character[random.randint(0,51)])
print(s)
fl=list(map(str,s))
str=""
for i in range(len(fl)):
    pos=random.randint(0, len(fl) - 1)
    str=str+fl[pos]
    fl.pop(pos)
print(str)


