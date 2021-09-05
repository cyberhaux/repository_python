def calculateSlantHeight(radius: int, height: int):
    slantHeight = (radius ** 2 + height ** 2) ** (1/2)
    return slantHeight


def calculateVolume(radius: int, height: int):
    volume = (22/7) * (radius ** 2) * (height / 3)
    return volume


def curvedSurfaceArea(radius: int, height: int):
    area = (22/7) * radius * calculateSlantHeight(radius, height)
    return area


def totalSurfaceArea(radius: int, height: int):
    area = curvedSurfaceArea(radius, height) + (22/7) * (radius ** 2)
    return area


menuMain = {
    1: 'Calculate Slant Height(l) of the Cone',
    2: 'Calculate Volume of the Cone',
    3: 'Calculate Curved Surface Area (CSA) of Cone',
    4: 'Calculate Total Surface Area (TSA) of Cone'
}

while True:
    for i in menuMain.keys():
        print('{}: {}'.format(i, menuMain[i]))
    radius = int(input('Please enter the radius of the Cone '))
    height = int(input('Please enter the height of the Cone (Unit must be same as radius) '))
    unit = input('Please enter the unit of both the quantity ')
    mainChoice = int(input('Please enter your choice '))
    if mainChoice == 1:
        print('Slant Height of the Cone is: {} {}'.format(calculateSlantHeight(radius, height), unit))
    elif mainChoice == 2:
        print('Volume of the Cone is: {}'.format(calculateVolume(radius, height), unit))
    elif mainChoice == 3:
        print('CSA of the Cone is: {}'.format(curvedSurfaceArea(radius, height), unit))
    elif mainChoice == 4:
        print('TSA of the Cone is: {}'.format(totalSurfaceArea(radius, height), unit))
    userConfirmation = input('Do you want to continue (Y/N) ')
    if userConfirmation.lower == 'y':
        continue
    else:
        break
