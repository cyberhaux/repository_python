def replaceCharacter(fileName: str, replacedCharacter: str, newCharacter: str):
    replacedCHaracters = []
    with open(fileName) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    for i in mainText:
        replacedCHaracters.append(i.replace(replacedCharacter, newCharacter))
    returnText = '\n'.join(replacedCHaracters)
    return returnText


print(replaceCharacter('sample.txt', 'a', 'e'))
