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


