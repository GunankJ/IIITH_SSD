import csv

def printdata(data):
    for row in data:
        print(row)

cleanedData = []
def q1(csvfile):
    cleanedData = []
    with open(csvfile, newline='') as file:
        fileReader = csv.reader(file, delimiter=',')
        for row in fileReader:
            cleanedData.append(row[:-6])
    return cleanedData

def q2(data):
    cleanedData = []
    cleanedData.append(data[0])
    data = data[1:]
    # count = 1
    # for row in data:
    #     if(float(row[6]) < -3.0):
    #         continue
    #     else:
    #         cleanedData.append(row)
    #         count += 1
    # print(count)
    filteredData = list(filter(lambda x: float(x[6]) >= -3.0, data))
    return cleanedData + filteredData

def q3(data):
    opencol = []
    for row in data[1:]:
        opencol.append(float(row[1].replace(',','')))

    highcol = []
    for row in data[1:]:
        highcol.append(float(row[2].replace(',','')))

    lowcol = []
    for row in data[1:]:
        lowcol.append(float(row[3].replace(',','')))

    return list(map(lambda x: sum(x) / len(x), [opencol, highcol, lowcol]))

def q4(char, data):
    toBeDisp = []
    for row in data[1:]:
        if(row[0].startswith(char)):
            toBeDisp.append(row)
    return toBeDisp

csvfile = './lab_11_data.csv'
data = q1(csvfile)
# print("------------------------------------------- Q1 -----------------------------------------")
# printdata(data)

data = q2(data)
# print("------------------------------------------- Q2 -----------------------------------------")
# printdata(data)
# print(len(data))

op, hi, lo = q3(data)
file = open("avg_output.txt", 'w')
file.write(f'{op}\n{hi}\n{lo}')
file.close()

char = input()
file = open("stock_output.txt", 'w')
data = q4(char, data)
for row in data:
    file.write(' '.join(row)+'\n')


# with open('./lab_11_data.csv', newline='') as file:
#     fileReader = csv.reader(file, delimiter=',')
#     fileReader = list(fileReader)
#     cleanedData.append(fileReader[0][:-6])
#     count = 1
#     for row in fileReader[1:]:
#         if(float(row[6]) < -3.0):
#             cleanedData.append(row[:-6])
#             count += 1

# for row in cleanedData:
#     print(row)
# print(count)