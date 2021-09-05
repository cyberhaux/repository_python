def countOccurrence(string: str):
    occurrence = [0, 0, 0, 0]
    for i in string:
        if i.isalpha():
            if i.isupper():
                occurrence[0] += 1
            else:
                occurrence[1] += 1
        elif i.isdigit():
            occurrence[2] += 1
        else:
            occurrence[3] += 1
    return occurrence

userString = input('Please enter a string ')
print('The number of times Uppercase letters occurred are {}, lowercase letters occurred are {}, digits occurred are {} and special character occurred are {}'
      .format(countOccurrence(userString)[0], countOccurrence(userString)[1], countOccurrence(userString)[2], countOccurrence(userString)[3]))
