import numpy as np

file = open("dataset/train.txt", "r")

file.readline()
date_of_birth = []

while 1:
    line = file.readline()
    if not line: break
    y = line.split(",")
    d = y[10]
    if d != "?":
        date_of_birth.append(d)
file.close()


# mean = (np.array(date_of_birth, dtype='datetime64[s]')
#         .view('i8')
#         .mean()
#         .astype('datetime64[s]'))
#
# print(mean)
