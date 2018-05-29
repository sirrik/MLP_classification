import datetime

file = open("ids_and_maxcolors.txt", "r")

ids = []
colors = []

while 1:
    line = file.readline()
    if not line: break
    y = line.split(",")
    id = y[0]
    color = y[1][0:-1]
    ids.append(id)
    colors.append(color)
file.close()

average_birth = "1964-04-11"
average_difference = 11
max_color = "yellow"

file2 = open("dataset/test.txt", "r")
header = file2.readline()

file3 = open("test2.txt", "w")
file3.write(header)

while 1:
    line = file2.readline()
    if not line: break
    y = line.split(",")
    year, month, day = y[1].split("-")  # order date
    dateOrder = datetime.date(int(year), int(month), int(day))
    if y[5] == "?":
        if y[3] in ids:
            index = ids.index(y[3])
            y[5] = colors[index]
        else:
            y[5] = max_color
    if y[10] == "?":
        y[10] = average_birth
    if y[2] == "?":
        dateDelivery = str(dateOrder + datetime.timedelta(average_difference))
        y[2] = dateDelivery
    if y[2] != "?":
        year2, month2, day2 = y[2].split("-")
        date2 = datetime.date(int(year2), int(month2), int(day2))
        if (date2 - dateOrder).days < 0:
            dateDelivery = str(dateOrder + datetime.timedelta(average_difference))
            y[2] = dateDelivery

    for i in range(len(y) - 1):
        file3.write("{},".format(y[i]))
    file3.write("{}".format(y[-1]))





file3.close()
file2.close()