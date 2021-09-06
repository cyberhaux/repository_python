def countCharacters(fileName: str):
    counts = [0, 0, 0, 0]
    with open(fileName) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    for i in mainText:
        for j in i:
            if j.isalpha():
                if j.isupper():
                    counts[1] += 1
                else:
                    counts[2] += 1
            elif j == ' ':
                counts[0] += 1
            elif j.isdigit():
                counts[3] += 1
            else:
                continue
    return counts


countedChars = countCharacters('sample.txt')
print('The number of spaces are {}, uppercase are {}, lowercase are {}, digits are {} '
      .format(countedChars[0], countedChars[1], countedChars[2], countedChars[3]))

