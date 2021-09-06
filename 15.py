def countWordsCharacters(fileName: str):
    count = 0
    with open(fileName) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    for i in mainText:
        for j in i.split(' '):
            if len(j) > 5:
                count += 1
    return count


print('The number of words with more the 5 characters present in the file are {}'.format(countWordsCharacters('sample.txt')))