def displayLines(fileName: str, character: str):
    count = 0
    with open(fileName) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    i = len(mainText) - 1
    while i > -1:
        print(mainText[i][0])
        if mainText[i][0].lower() == character:
            count += 1
            i -= 1
        elif i <= -1:
            i -= 1
            break
        else:
            i -= 1
            continue
    return count


print(displayLines('sample.txt', 'k'))
