def evenSort(list):
    evenList = []
    oddList = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            evenList.append(list[i])
    for i in range(len(list)):
        if list[i] % 2 != 0:
            oddList.append(list[i])
    mainList = evenList + oddList
    return mainList


userList = eval(input('Please enter your list '))
print('The even sorted list is : {}'.format(evenSort(userList)))
