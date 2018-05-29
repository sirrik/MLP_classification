file = open("dataset/train.txt", "r")

file.readline()
id_color = []
colors = []

while 1:
    line = file.readline()
    if not line: break
    y = line.split(",")
    id = y[3]
    color = y[5]
    if color != "?":
        id_color.append((id, color))
        colors.append(color)
file.close()

print(max(colors))

ids = []
ids_and_maxcolors = []

for i in id_color:
    x = i[0]
    if not x in ids:
        ids.append(x)

kkk = 0

for i in ids:
    c = []
    for j in id_color:
        if j[0] == i:
            c.append(j[1])

    ids_and_maxcolors.append((i, max(c)))
    kkk += 1
    print(kkk)

file2 = open("ids_and_maxcolors.txt", "w")

for i in ids_and_maxcolors:
    file2.write("{},{}\n".format(i[0], i[1]))

print()
print(len(ids))
print(len(ids_and_maxcolors))