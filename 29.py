def operation(list, operation: str, element: int):
    if operation == 'insert':
        list.append(element)
    elif operation == 'delete':
        list.remove(element)


options = {
    1: 'Insert element into the unsorted array',
    2: 'Delete element from the unsorted array',
    3: 'Exit'
}
while True:
    oper = ''
    for i in options.keys():
        print('{}: {}'.format(i, options[i]))
    listChoice = eval(input('Enter the list '))
    userChoice = int(input('Please enter the choice '))
    if userChoice == 1:
        element = int(input('Please enter the element for the following operation '))
        oper = 'insert'
        operation(listChoice, oper, element)
    elif userChoice == 2:
        element = int(input('Please enter the element for the following operation '))
        oper = 'delete'
        operation(listChoice, oper, element)
    else:
        break
