import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
import datetime


def convert_to_number(arr):
    x = preprocessing.LabelEncoder()
    x.fit(arr)
    xx = x.transform(arr)
    return xx


file = open("train2.txt", "r")
file.readline()
training_data = []
while 1:
    line = file.readline()
    if not line: break
    y = line.split(",")
    x = y[-1][0:-1]
    y[-1] = x
    training_data.append(y)
file.close()

file = open("test2.txt", "r")
file.readline()
test_data = []
while 1:
    line = file.readline()
    if not line: break
    y = line.split(",")
    x = y[-1][0:-1]
    y[-1] = x
    test_data.append(y)
file.close()

diff_orders = []
diff_deliveries = []

sizesTrain = []
colorsTrain = []
salutTrain = []
stateTrain = []

sizesTest = []
colorsTest = []
salutTest = []
stateTest = []

for d in training_data:
    year1, month1, day1 = d[1].split("-")
    year2, month2, day2 = d[2].split("-")
    byear, bmonth, bday = d[10].split("-")
    cyear, cmonth, cday = d[12].split("-")

    sizesTrain.append(d[4])
    colorsTrain.append(d[5])
    salutTrain.append(d[9])
    stateTrain.append(d[11])

    orderDate = datetime.date(int(year1), int(month1), int(day1))
    deliveryDate = datetime.date(int(year2), int(month2), int(day2))
    birthDate = datetime.date(int(byear), int(bmonth), int(bday))
    creationDate = datetime.date(int(cyear), int(cmonth), int(cday))

    sampleDate = datetime.date(2010, 1, 1)
    sampleDate2 = datetime.date(1900, 1, 1)

    d[1] = str((orderDate - sampleDate).days)
    d[2] = str((deliveryDate - sampleDate).days)
    d[10] = str((birthDate - sampleDate2).days)
    d[12] = str((creationDate - sampleDate).days)

diff_orders2 = []
diff_deliveries2 = []
for d in test_data:
    year1, month1, day1 = d[1].split("-")
    year2, month2, day2 = d[2].split("-")
    byear, bmonth, bday = d[10].split("-")
    cyear, cmonth, cday = d[12].split("-")

    sizesTest.append(d[4])
    colorsTest.append(d[5])
    salutTest.append(d[9])
    stateTest.append(d[11])

    orderDate = datetime.date(int(year1), int(month1), int(day1))
    deliveryDate = datetime.date(int(year2), int(month2), int(day2))
    birthDate = datetime.date(int(byear), int(bmonth), int(bday))
    creationDate = datetime.date(int(cyear), int(cmonth), int(cday))

    sampleDate = datetime.date(2010, 1, 1)
    sampleDate2 = datetime.date(1900, 1, 1)

    d[1] = str((orderDate - sampleDate).days)
    d[2] = str((deliveryDate - sampleDate).days)
    d[10] = str((birthDate - sampleDate2).days)
    d[12] = str((creationDate - sampleDate).days)

sizesTrain = convert_to_number(sizesTrain)
colorsTrain = convert_to_number(colorsTrain)
salutTrain = convert_to_number(salutTrain)
stateTrain = convert_to_number(stateTrain)

sizesTest = convert_to_number(sizesTest)
colorsTest = convert_to_number(colorsTest)
salutTest = convert_to_number(salutTest)
stateTest = convert_to_number(stateTest)

for i in range(len(training_data)):
    training_data[i][4] = sizesTrain[i]
    training_data[i][5] = colorsTrain[i]
    training_data[i][9] = salutTrain[i]
    training_data[i][11] = stateTrain[i]

for i in range(len(test_data)):
    test_data[i][4] = sizesTest[i]
    test_data[i][5] = colorsTest[i]
    test_data[i][9] = salutTest[i]
    test_data[i][11] = stateTest[i]

train_dataset = [(int(column[3]),
                  column[5],
                  column[11],
                  column[4],
                  column[9],
                  int(column[1]),
                  int(column[2]),
                  int(column[10]),
                  int(column[12]),
                  float(column[7]),
                  int(column[6]),
                  int(column[8])) for column in training_data]
test_dataset = [(int(column[3]),
                 column[5],
                 column[11],
                 column[4],
                 column[9],
                 int(column[1]),
                 int(column[2]),
                 int(column[10]),
                 int(column[12]),
                 float(column[7]),
                 int(column[6]),
                 int(column[8])) for column in test_data]

return_shipment = [column[-1] for column in training_data]


shaped_train_dataset = np.reshape(train_dataset, (-1, 8))
shaped_test_dataset = np.reshape(test_dataset, (-1, 8))
target_dataset = return_shipment

scaler = StandardScaler()

scaler.fit(shaped_train_dataset)
shaped_train_dataset = scaler.transform(shaped_train_dataset)
shaped_test_dataset = scaler.transform(shaped_test_dataset)

mlp = MLPClassifier(hidden_layer_sizes=(100, 100, 100))

mlp.fit(shaped_train_dataset, target_dataset)

predictions = mlp.predict(shaped_test_dataset)

print(predictions)

fff = open("predictbest.txt", "w")

for x in predictions:
    fff.write("{}\n".format(x))

