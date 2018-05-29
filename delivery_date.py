import datetime
import numpy as np

file = open("dataset/train.txt", "r")

file.readline()
ord_delv_date = []

while 1:
    line = file.readline()
    if not line: break
    y = line.split(",")
    order = y[1]
    delivery = y[2]
    if delivery != "?":
        ord_delv_date.append((order, delivery))
file.close()
#
# year1, month1, day1 = ord_delv_date[0][0].split("-")
# year2, month2, day2 = ord_delv_date[0][1].split("-")
#
#
# day1 = datetime.date(int(year1), int(month1), int(day1))
# day2 = datetime.date(int(year2), int(month2), int(day2))
# diff = day2 - day1
# print(diff.days)

diffs = []
for d in ord_delv_date:
    year1, month1, day1 = d[0].split("-")
    year2, month2, day2 = d[1].split("-")

    day1 = datetime.date(int(year1), int(month1), int(day1))
    day2 = datetime.date(int(year2), int(month2), int(day2))
    diff = day2 - day1

    if diff.days >= 0:
        diffs.append(diff.days)

print(np.mean(diffs)) # 11 days