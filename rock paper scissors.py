import random
rock='''
*****()
*****()
****()
'''
paper='''
 ********
 ********
 ********
 ********'''

scissors='''
      /()
()===/
()===\
      \()
'''
print(rock, "\t",paper, "\t",scissors)

print("")

list=[rock,paper,scissors]

status=True
while status:
    choice = random.randint(0, 2)
    userch=int(input("enter your choice 0 for rock,1 for paper, 2 scissors"))
    print(f"computer chose{choice}")
    if userch==choice:
        status = False
        print("It is draw")
    if userch==0 and choice==1:
            status =False
            print("paper wins",paper)
    elif userch==0 and choice==2:
            status=False
            print("Rock wins", rock)
    elif userch==1 and choice==2:
            status=False
            print("scissors wins", scissors)













# def multiplyBy(n):
#     print(n)
#     return lambda x: x * n
#
#
# double = multiplyBy(2)
# times10 = multiplyBy(10)
# print(double(3))