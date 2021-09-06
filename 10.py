def countVowels(fileName: str):
    count = [0, 0]
    with open(fileName) as ob:
        mainText = ob.read()
    vowels = 'aeiou'
    mainText = mainText.split('\n')
    for i in mainText:
        for j in i:
            if j.lower() in vowels:
                count[0] += 1
            else:
                count[1] += 1
    return count


print('The number of vowels present in the file are {} and the number of consonant present are {}'
      .format(countVowels('sample.txt')[0], countVowels('sample.txt')[1]))
