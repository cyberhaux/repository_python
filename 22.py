def countCharacters(fileName: str, character: str):
    count = 0
    with open(fileName) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    for i in mainText:
        if i[len(i)-1].lower() == character:
            count += 1
        else:
            continue
    return count


print('The number of time the character is present at the end are {}'.format(countCharacters('sample.txt', 'a')))
