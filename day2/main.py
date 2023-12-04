
MAX_RED=12
MAX_BLUE=14
MAX_GREEN=13

def getGameId(data: str):
    return int(data.split(' ')[1].rstrip(':'))

def getSetOne(data: str):
    return data.split(':')[1].split(';')[0]

def getSetTwo(data: str):
    return data.split(':')[1].split(';')[1]

def getSetThree(data: str):
    return data.split(':')[1].split(';')[2]


def getSetOneRed(data: str):
    setOne = getSetOne(data)
    setOneSplit = setOne.split(',')
    for i in setOneSplit:
        if 'red' in i:
            return int(i.split(' ')[1])
    return -1

def getSetOneBlue(data: str):
    setOne = getSetOne(data)
    setOneSplit = setOne.split(',')
    for i in setOneSplit:
        if 'blue' in i:
            return int(i.split(' ')[1])
    return -1


def getSetOneGreen(data: str):
    setOne = getSetOne(data)
    setOneSplit = setOne.split(',')
    for i in setOneSplit:
        if 'green' in i:
            return int(i.split(' ')[1])
    return -1


def getSetTwoRed(data: str):
    setTwo = getSetTwo(data)
    setTwoSplit = setTwo.split(',')
    for i in setTwoSplit:
        if 'red' in i:
            return int(i.split(' ')[1])
    return -1


def getSetTwoBlue(data: str):
    setTwo = getSetTwo(data)
    setTwoSplit = setTwo.split(',')
    for i in setTwoSplit:
        if 'blue' in i:
            return int(i.split(' ')[1])
    return -1


def getSetTwoGreen(data: str):
    setTwo = getSetTwo(data)
    setTwoSplit = setTwo.split(',')
    for i in setTwoSplit:
        if 'green' in i:
            return int(i.split(' ')[1])
    return -1


def getSetThreeRed(data: str):
    setThree = getSetThree(data)
    setThreeSplit = setThree.split(',')
    for i in setThreeSplit:
        if 'red' in i:
            return int(i.split(' ')[1])
    return -1


def getSetThreeBlue(data: str):
    setThree = getSetThree(data)
    setThreeSplit = setThree.split(',')
    for i in setThreeSplit:
        if 'blue' in i:
            return int(i.split(' ')[1])
    return -1


def getSetThreeGreen(data: str):
    setThree = getSetThree(data)
    setThreeSplit = setThree.split(',')
    for i in setThreeSplit:
        if 'green' in i:
            return int(i.split(' ')[1])
    return -1


with open('input.txt', 'r') as file:
    data = file.read().split('\n')


gameIdSum = 0
for i in data:
    gameId = getGameId(i)
    print('Game ID: ' + str(gameId))

    valid = True
    redHighest = 0
    blueHighest = 0
    greenHighest = 0
    allSets = i.split(':')[1].split(';')
    for game in allSets:

        gameSplit = game.split(',')

        for color in gameSplit:
            if 'red' in color:
                if int(color.split(' ')[1]) > redHighest:
                    redHighest = int(color.split(' ')[1])
                # if int(color.split(' ')[1]) > MAX_RED:
                #     valid = False
                #     print('Invalid game data > red')
                #     print('-----------------------------------')
                #     print('\n')
                #     break
            if 'blue' in color:
                if int(color.split(' ')[1]) > blueHighest:
                    blueHighest = int(color.split(' ')[1])
                # if int(color.split(' ')[1]) > MAX_BLUE:
                #     valid = False
                #     print('Invalid game data > blue')
                #     print('-----------------------------------')
                #     print('\n')
                #     break
            if 'green' in color:
                if int(color.split(' ')[1]) > greenHighest:
                    greenHighest = int(color.split(' ')[1])
                # if int(color.split(' ')[1]) > MAX_GREEN:
                #     valid = False
                #     print('Invalid game data > green')
                #     print('-----------------------------------')
                #     print('\n')
                #     break

    power = redHighest * blueHighest * greenHighest


    gameIdSum += power

    # if getSetOneRed(i) > MAX_RED or getSetOneBlue(i) > MAX_BLUE or getSetOneGreen(i) > MAX_GREEN:
    #     print('Invalid game data > set one')
    #     print('-----------------------------------')
    #     print('\n')
    #     continue
    # if getSetTwoRed(i) > MAX_RED or getSetTwoBlue(i) > MAX_BLUE or getSetTwoGreen(i) > MAX_GREEN:
    #     print('Invalid game data > set two')
    #     print('-----------------------------------')
    #     print('\n')
    #     continue
    # if getSetThreeRed(i) > MAX_RED or getSetThreeBlue(i) > MAX_BLUE or getSetThreeGreen(i) > MAX_GREEN:
    #     print('Invalid game data > set three')
    #     print('-----------------------------------')
    #     print('\n')
    #     continue

    # gameIdSum += int(getGameId(i))
    # print(getGameId(i) + ':' + getSetOne(i) + ':' + getSetTwo(i) + ':' + getSetThree(i))
    # print(getSetOneRed(i))
    # print(getSetOneBlue(i))
    # print(getSetOneGreen(i))
    # print(getSetTwoRed(i))
    # print(getSetTwoBlue(i))
    # print(getSetTwoGreen(i))
    # print(getSetThreeRed(i))
    # print(getSetThreeBlue(i))
    # print(getSetThreeGreen(i))
    # print('\n')

print('Game ID Sum: ' + str(gameIdSum))