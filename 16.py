def countLines(fileName: str):
    count = 0
    with open(fileName) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    for i in mainText:
        count += 1
    return count


print('The number of lines present in the file are {}'.format(countLines('sample.txt')))
