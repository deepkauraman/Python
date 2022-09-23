# findng the second largest in a nested list
# finding the second minimum in a list
import sys

if __name__ == '__main__':
    record = []
    for _ in range(int(input("Enter the number of record"))):
        lst = []
        name = input("enter name")
        score = float(input(" enter score"))
        lst.append(name)
        lst.append(score)
        record.append(lst)
    minscore = []
    min = sys.maxsize
    for element in record:
        if element[1] < min:
            minscore = element
            min = element[1]

    secmin = sys.maxsize
    for element in record:
        if element[1] > min and element[1] < secmin:
            secmin = element[1]
    fl = []
    for records in record:
        if secmin in records:
            fl.append(records)
    FL = sorted(fl)
    print(FL)
    for element in FL:
        print(element[0])

# import sys
#
#     record = []
# for _ in range(int(input(""))):
#     lst = []
#     name = input("")
#     score = float(input(""))
#     lst.append(name)
#     lst.append(score)
#     record.append(lst)
# # print(max(record))
# maxscore = []
# mx = -sys.maxsize - 1
# for element in record:
#     if element[1] > mx:
#         maxscore = element
#         mx = element[1]
# print(maxscore)
# ms = maxscore[1]
# print(ms)
# secmax = []
# secm = -sys.maxsize - 1
# for element in record:
#     if element[1] > secm and element[1] < ms:
#         secm = element[1]
# for x in record:
#     if secm in x:
#         secmax.append(x)
# # print(secmax)
# lst = sorted(secmax)
# for x in lst:
#     print(x[0])
# list_scores = []
# for i in range(len(record)):
#     list_scores.append(record[i][1])
# maximum = max(list_scores)
# secondmax = 0.0
# secondmaxlist = []
# for i in range(len(record)):
#     if secondmax < record[i][1] and record[i][1] < maximum:
#         secondmax = record[i][1]
# for i in range(len(record)):
#     if secondmax in record[i]:
#         secondmaxlist.append(record[i][0])
# return secondmaxlist