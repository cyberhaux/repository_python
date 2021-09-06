def countFirstCharacter(fileName: str, alphabet: str):
    count = 0
    with open(fileName) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    for i in mainText:
        if i[0].lower() == alphabet.lower():
            count += 1
    return count


print('The number of first character E present in file are {}'
      .format(countFirstCharacter('sample.txt', 'E')))
