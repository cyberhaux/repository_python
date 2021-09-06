import pickle


def createEmployeeData(fileName: str, code: int, name: str, salary: float, phone: int):
    data = [[code, name, salary, phone]]
    with open(fileName, 'wb') as ob:
        pickle.dump(data, ob)


def appendEmployeeData(fileName: str, code: int, name: str, salary: float, phone: int):
    data = [code, name, salary, phone]
    with open(fileName, 'wb+') as ob:
        mainData = pickle.load(ob)
        mainData.append(data)
        pickle.dump(mainData, ob)


def searchingData(fileName: str, code:int):
    with open(fileName, 'rb') as ob:
        mainData = pickle.load(ob)
    for i in mainData:
        if code == i[0]:
            return True
        else:
            continue


def checkIndex(mainData, code):
    for i in range(len(mainData)):
        for j in range(i):
            if mainData[i][0] == code:
                return i


def updatingData(fileName: str, code: int, name: str, salary: float, phone: int):
    data = [code, name, salary, phone]
    if searchingData(fileName, code):
        with open(fileName, 'wb+') as ob:
            mainData = pickle.load(ob)
            index = checkIndex(mainData, code)
            del mainData[index]
            mainData.insert(index, data)
            pickle.dump(mainData, ob)


def deletingData(fileName: str, code: int, name: str, salary: float, phone: int):
    data = [code, name, salary, phone]
    if searchingData(fileName, code):
        with open(fileName, 'wb+') as ob:
            mainData = pickle.load(ob)
            index = checkIndex(mainData, code)
            del mainData[index]
            pickle.dump(mainData, ob)


def readingData(fileName: str):
    with open(fileName, 'rb') as ob:
        mainData = pickle.load(ob)
        return mainData


