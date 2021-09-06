def countAlphabetOccurrence(textFile: str, alphabet: str):
    c = 0
    with open(textFile) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    for i in mainText:
        for j in i:
            if j.lower() == alphabet.lower():
                c += 1
            else:
                continue
    return c


print(countAlphabetOccurrence('sample.txt', 'c'))
