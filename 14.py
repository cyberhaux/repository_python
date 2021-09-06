def countWords(fileName: str):
    count = 0
    with open(fileName) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    for i in mainText:
        for j in i.split(' '):
            count += 1
    return count


print(countWords('sample.txt'))