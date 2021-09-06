def countWords(fileName: str, word: str):
    count = 0
    with open(fileName) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    for i in mainText:
        for j in i.split(' '):
            if j == word:
                count += 1
    return count


print('The number of words present in the file are {}'.format(countWords('sample.txt', 'are')))
