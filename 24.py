def remove_lowercase(fileName1: str, fileName2: str):
    upperCase = []
    with open(fileName1) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    for i in mainText:
        if i[0].isupper():
            upperCase.append(i)
        else:
            continue
    with open(fileName2, 'w') as ob:
        ob.writelines('\n'.join(upperCase))
    return 'The lines have been copied'


remove_lowercase('sample.txt', 'demo.txt')
