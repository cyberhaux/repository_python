def emptyStack(s):
    if s.isempty():
        return True
    else:
        return False


def topElement(s):
    global top
    top = len(s) - 1


def pushElement(s, element):
    global top
    s.append(element)
    top = topElement(s)


def popElement(s):
    if emptyStack(s):
        return 'Stack is empty'
    else:
        global top
        num = s[top]
        s.pop()
        top = len(s) - 1
    return num


def peek(s):
    global top
    if emptyStack(s):
        return 'Stack is empty'
    else:
        top = len(s) - 1
        return top


def displayElements(s):
    global top
    if emptyStack(s):
        return 'Stack is empty'
    else:
        top = len(s) - 1
        for i in range(top, -1, -1):
            print(s[i])


displayText = {
    1: 'Insert the element into the list',
    2: 'Delete a element from the list',
    3: 'Display peek of the element',
    4: 'Display all the elements from the list',
    5: 'Exit'
}


while True:
    for i in displayText.keys():
        print('{}: {}'.format(i, displayText[i]))

    userInput = int(input('Please enter the choice '))
    userList = eval(input('Please enter the list'))
    if userInput == 1:
        element = int(input('Enter the element to be inserted '))
        pushElement(userList, element)
    elif userInput == 2:
        popElement(userList)
    elif userInput == 3:
        peek(userList)
    elif userInput == 4:
        displayElements(userList)
    elif userInput == 5:
        break
    else:
        userConf = input('Do you want to continue using the program (Y/N) ')
        if userConf.lower() == 'y':
            continue
        else:
            break
