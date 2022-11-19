from copy import deepcopy

mainPuzzle = [[1, 2, 3],
              [7, 4, 8],
              [6, 0, 5],
              ["", 0, 0]]

explored = []
queue = []

def moveUp(puzzle, position):
    return {"from": [position["r"], position["c"]], "to": [position["r"] - 1, position["c"]]} if position["r"] > 0 else False

def moveDown(puzzle, position):
    return {"from": [position["r"], position["c"]], "to": [position["r"] + 1, position["c"]]} if position["r"] < len(puzzle) - 2 else False

def moveRight(puzzle, position):
    return {"from": [position["r"], position["c"]], "to": [position["r"], position["c"] + 1]} if position["c"] < len(puzzle[position["c"]]) - 1 else False

def moveLeft(puzzle, position):
    return {"from": [position["r"], position["c"]], "to": [position["r"], position["c"] - 1]} if position["c"] > 0 else False

def findZiro(puzzle):
    for row in puzzle:
        for num in row:
            if num == 0:
                return {"r": puzzle.index(row), "c": row.index(num)}

def checkTarget(puzzle):
    target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    if puzzle[0] == target[0]:
        if puzzle[1] == target[1]:
            if puzzle[2] == target[2]:
                return True
            return False
        return False
    return False

def makeMovements(puzzle, position):
    movements = []
    movements.append([moveUp(puzzle, position), 'u'])
    movements.append([moveDown(puzzle, position), 'd'])
    movements.append([moveRight(puzzle, position), 'r'])
    movements.append([moveLeft(puzzle, position), 'l'])
    return filter(lambda x: x[0], movements)

def move(puzzle, movements):
    state = []
    for movement in movements:
        copy = deepcopy(puzzle)
        positions = movement[0]
        lastValue = copy[positions["to"][0]][positions["to"][1]]
        copy[positions["to"][0]][positions["to"][1]] = 0
        copy[positions["from"][0]][positions["from"][1]] = lastValue
        copy[3][0] += movement[1]
        copy[3][1] += 1
        state.append(copy)
    return state

def printPuzzle(puzzle):
    for i in puzzle:
        print(i)

def checkExist(puzzle, searchable):
    for item in searchable:
        if item == puzzle.pop():
            return True
        else:
            return False

def solvePuzzle(puzzle):
    position = findZiro(puzzle)
    movements = makeMovements(puzzle, position)
    state = move(puzzle, movements)
    for item in state:
        queue.append(item)
    while True:
        currentItem = queue[0]
        print(currentItem)
        if checkTarget(currentItem):
            print('The puzzle was solved!')
            break
        else:
            position = findZiro(currentItem)
            movements = makeMovements(currentItem, position)
            state = move(currentItem, movements)
            queue.remove(currentItem)
            explored.append(currentItem)
            for newItem in state:
                queue.append(newItem)
    printPuzzle(currentItem)


solvePuzzle(mainPuzzle)