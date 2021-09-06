def longestLine(fileName: str):
    with open(fileName) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    return max(mainText)


print(longestLine('sample.txt'))
