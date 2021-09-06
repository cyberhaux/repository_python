def findLastLine(fileName: str):
    with open(fileName) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    return mainText[len(mainText) - 1]


print('The last line of the file contains "{}"'.format(findLastLine('sample.txt')))
