table=[[2.4,1.05,2.5,0.38],[3.0,1.12,2.5,0.35],[3.6,1.20,2.5,0.32]]
def basiccocomo():
    result=[]
    kloc=int(input("Enter the lines of code "))
    if kloc>2 and kloc<=50:
        model="organic"
        index=0

    elif kloc>50 and kloc<=500:
        model="semidetatached"
        index=1
    else:
        model="embeded"
        index=2
    result = calculate_parameters(kloc, index)
    result.append(model)
    return result

def calculate_parameters(kloc,index):
    list=[]
    effort=table[index][0]*(kloc**table[index][1])
    time=table[index][1]*(effort**table[index][3])
    personnesrequired=effort/time
    list.append(effort)
    list.append(time)
    list.append(personnesrequired)
    return list
result=[]
result=basiccocomo()
print(result[0],"Person-Month")
print(result[1] ,"Development time Required" )
print(int(result[2])," Avg staff  Required")
print(result[3],"Model")
