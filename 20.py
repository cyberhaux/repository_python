def displayWords(textFile: str):
    text = []
    with open(textFile) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    for i in mainText:
        for j in i.split(' '):
            if len(j) < 4:
                text.append(j)
            else:
                continue
    return text


print('The words that are less tha 4 characters are "{}"'
      .format(', '.join(displayWords('sample.txt'))))
