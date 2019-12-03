def main():
    file = open('q3_input.txt')
    firstWire = file.readline().split(',')
    secondWire = file.readline().split(',')

    # calculate the coordinates crossed by these two wires

    firstCoordinates = getPathCoordinates(firstWire)
    secondCoordinates = getPathCoordinates(secondWire)

    # compare to find coordinates of cross

    listOfCross = list(set(firstCoordinates).intersection(secondCoordinates))
    distances = []

    for coordinate in listOfCross:
        distances.append(abs(coordinate[0]) + abs(coordinate[1]))

    print(min(distances))

    getMinimalSignalDelayPoint(firstCoordinates, secondCoordinates, listOfCross)
        
def getPathCoordinates(wire):

    currentX = 0
    currentY = 0
    pathCoordinates = []

    for step in wire:
        stepSize = int(step[1:])

        if step[0] == 'L':
            for i in range(stepSize):
                currentX -= 1
                pathCoordinates.append((currentX, currentY))

        elif step[0] == 'R':
            for i in range(stepSize):
                currentX += 1
                pathCoordinates.append((currentX, currentY))

        elif step[0] == 'U':
            for i in range(stepSize):
                currentY += 1
                pathCoordinates.append((currentX, currentY))

        elif step[0] == 'D':
            for i in range(stepSize):
                currentY -= 1
                pathCoordinates.append((currentX, currentY))

    return pathCoordinates

def getMinimalSignalDelayPoint(pathOne, pathTwo, intersects):

    minimalPoint = intersects[0]
    currentMinimaldelay = travelTime(pathOne, minimalPoint) + travelTime(pathTwo, minimalPoint)
    
    for point in intersects:
        totalDelay = travelTime(pathOne, point) + travelTime(pathTwo, point)
        if totalDelay < currentMinimaldelay:
            currentMinimaldelay = totalDelay
            minimalPoint = point

    print('The minimal point is (%s, %s), with a delay of %s' % (point[0], point[1], currentMinimaldelay))
    return None

def travelTime(path, point):
    step = 1
    while path[step-1] != point:
        step += 1
    return step

if __name__ == '__main__':
    main()

