def Enqueue(userList):
    element = input("Enter the element:")
    userList.append(element)
    print(element, "is added to the Queue!")


def dequeue(userList):
    if not userList:
        print("Queue is Empty!!!")
    else:
        e = userList.pop(0)
        print("element removed!!:", e)


def peek(userList):
    print(userList[0])


def display(userList):
    print(userList)


options = {
    1: 'Insert element into the Queue',
    2: 'Remove element from the Queue',
    3: 'Peek element from the Queue',
    4: 'Display the element in the Queue',
    5: 'Exit'
}


while True:
    for i in options.keys():
        print('{}: {}'.format(i, options[i]))
    choice = int(input())
    userList = eval(input('Please enter the list for implementing the Queue '))
    if choice == 1:
        Enqueue(userList)
    elif choice == 2:
        dequeue(userList)
    elif choice == 3:
        peek(userList)
    elif choice == 4:
        display(userList)
    elif choice == 5:
        break
    else:
        print('Invalid Option')
