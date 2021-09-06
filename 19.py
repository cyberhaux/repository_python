def copyText(fileName1: str, fileName2: str):
    with open(fileName1) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    with open(fileName2, 'w') as ob:
        ob.writelines('\n'.join(mainText))
    return 'Copied the data to the given file {}'.format(fileName2)


print(copyText('sample.txt', 'demo.txt'))
