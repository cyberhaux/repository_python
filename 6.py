def countElements(tuple, element):
    return tuple.count(element)


userTuple = eval(input('Please enter a tuple with number elements '))
element = int(input('Please enter the element to be counted '))
print('The number of element {} occurred in {} tuple is {}'
      .format(element, userTuple, countElements(userTuple, element)))