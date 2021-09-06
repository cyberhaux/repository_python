import csv


def writeCSV(fileName: str, roll: int, name: str, marks: float):
    headerData = ['roll', 'name', 'marks']
    with open(fileName, 'w') as csvFile:
        csvWriter = csv.writer(csvFile)
        data = [roll, name, marks]
        csvWriter.writerow(headerData)
        csvWriter.writerow(data)


def searchData(fileName: str, roll: int):
    with open(fileName) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for i in csvReader:
            if i[0] == roll:
                return 'The student with roll number {} with name {} have scored {} marks'.format(i[0], i[1], i[2])
            else:
                continue


def showData(fileName: str, roll: int):
    with open(fileName) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for i in csvReader:
            print('The student with roll number {} wit name {} have score {} marks'.format(i[0], i[1], i[2]))


