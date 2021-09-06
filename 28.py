import bisect

def listOperation(list, operation: str, element: int):
    if operation == 'InsertAsc':
        bisect.insort(list, element)
    elif operation == 'InsertDesc':
        list.sort()
        bisect.insort(list, element)
        list.reverse()
    elif operation == 'DeleteDesc':
        list.remove(element)
    else:
        return 'Cannot proceed'
    return list

operations = {
    1: 'Insert element in the ascending order sorted list',
    2: 'Insert element in the descending order sorted list',
    3: 'Delete element from the list in descending order',
    4: 'Exit'
}

while True:
    oper = ''
    for i in operations.keys():
        print('{}: {}'.format(i, operations[i]))
    userList = eval(input('Please enter the list '))
    userChoice = int(input('Please enter your choice '))
    if userChoice == 1:
        oper = 'InsertAsc'
        element = int(input('Please enter the element for the operation '))
        listOperation(userList, oper, element)
        print(userList)
    elif userChoice == 2:
        oper = 'InsertDesc'
        element = int(input('Please enter the element for the operation '))
        listOperation(userList, oper, element)
        print(userList)
    elif userChoice == 3:
        oper = 'DeleteDesc'
        element = int(input('Please enter the element for the operation '))
        listOperation(userList, oper, element)
        print(userList)
    else:
        break
