def countArticles(fileName: str):
    count = [0, 0]
    with open(fileName) as ob:
        mainText = ob.read()
    mainText = mainText.split('\n')
    for i in mainText:
        for j in i.split(' '):
            print(j)
            if j.lower() == 'an':
                count[0] += 1
            elif j.lower() == 'the':
                count[1] += 1
            else:
                continue
    return count


print('The Number of "an" present in the file is {} and "the" present in the file is {}'
      .format(countArticles('sample.txt')[0], countArticles('sample.txt')[1]))
