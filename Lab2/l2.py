#FIRST PART FUNCTION---------------
def myMin(targetList):
    a=targetList[0]
    for item in targetList:
        if item<a:
            a=item
    return a

def myMax(targetList):
    a=targetList[0]
    for item in targetList:
        if item>a:
            a=item
    return a

def mySum(targetList):
    s=0
    for item in targetList:
        s=item+s
    return s

def myAvge(targetList):
    return sum(targetList)/len(targetList)
#END---------------

#SECOND PART FUNCTION---------------
def findPosition(myArray):
    retVal = []
    for i in range(len(myArray)):
        for j in range(len(myArray[i])):
            if(myArray[i][j]==-2):
                retVal.append([i,j])
    return retVal

def findExits(myArray):
    retVal = []
    for i in range(len(myArray)):
        for j in range(len(myArray[i])):
           if i == 0 or j==0 or i==len(myArray)-1 or j == len(myArray)-1:
               if(myArray[i][j]==0):
                   retVal.append([i,j])
    return retVal

def getDistance(pointOne,pointTwo):
    x=abs(pointOne[0]-pointTwo[0])
    y=abs(pointOne[1]-pointTwo[1])
    return x+y

def readFromFile(filePath):
    with open(filePath, 'r') as f:
        l = [[int(num) for num in line.split(' ')] for line in f]
    print(l)

#END---------------

#THIRD PART FUNCTIONS-----------------------------
def isCoordValid(coord,matrix):
    width = len(matrix[0])
    height = len(matrix)
    if coord[0]>=width or coord[0]<0 or coord[1]>=height or coord[1]<0 or matrix[coord[0]][coord[1]]!=0:
        return False
    return True

def printMatrix(targetMatrix):
    for item in targetMatrix:
        print(item)
def lee(matrix,startCoord,endCoord):
    listToBeSearched =[]
    listToBeSearched.append(startCoord)
    matrix[startCoord[0]][startCoord[1]]=1
    while len(listToBeSearched)!=0 and not endCoord in listToBeSearched:
       # print("A2 "+str(listToBeSearched))
       # printMatrix(matrix)
        targetCoord = listToBeSearched.pop(0)
        
        upCoord = [targetCoord[0],targetCoord[1]+1]
        rightCoord =[targetCoord[0]+1,targetCoord[1]]
        downCoord = [targetCoord[0],targetCoord[1]-1]
        lefCoord = [targetCoord[0]-1,targetCoord[1]]

        if isCoordValid(upCoord,matrix):
            matrix[upCoord[0]][upCoord[1]] = matrix[targetCoord[0]][targetCoord[1]]+1
            listToBeSearched.append(upCoord)
        if isCoordValid(rightCoord,matrix):
            matrix[rightCoord[0]][rightCoord[1]] =matrix[targetCoord[0]][targetCoord[1]]+1
            listToBeSearched.append(rightCoord)
        if isCoordValid(downCoord,matrix):
            matrix[downCoord[0]][downCoord[1]] =matrix[targetCoord[0]][targetCoord[1]]+1
            listToBeSearched.append(downCoord)
        if isCoordValid(lefCoord,matrix):
            matrix[lefCoord[0]][lefCoord[1]] =matrix[targetCoord[0]][targetCoord[1]]+1
            listToBeSearched.append(lefCoord)
    matrix[endCoord[0]][endCoord[1]]=15       
    return matrix

def traceBack(matrix, endPoint,startPoint):
    steps = []
    steps.append(endPoint)
    currentCoord = endPoint
    while currentCoord!=startPoint:
        currentCoord=getLowestNeighboor(matrix,currentCoord)
        steps.append(currentCoord)
    return steps

def getLowestNeighboor(matrix, targetCoord):

    minValue = matrix[targetCoord[0]][targetCoord[1]]

    upCoord = [targetCoord[0],targetCoord[1]+1]
    rightCoord =[targetCoord[0]+1,targetCoord[1]]
    downCoord = [targetCoord[0],targetCoord[1]-1]
    lefCoord = [targetCoord[0]-1,targetCoord[1]]

    upValue = matrix[upCoord[0]][upCoord[1]]
    rightValue = matrix[rightCoord[0]][rightCoord[1]]
    downValue = matrix[downCoord[0]][downCoord[1]]
    leftValue = matrix[lefCoord[0]][lefCoord[1]]
    if upValue<minValue and upValue!=0 and upValue!=-1:
        return upCoord
    if rightValue<minValue and rightValue!=0 and rightValue!=-1:
        return rightCoord
    if downValue<minValue and downValue!=0 and downValue!=-1:
        return downCoord
    if leftValue<minValue and leftValue!=0 and leftValue!=-1:
        return lefCoord

#END---------------------

print("-------------PART 1-------------")
myList = [14,80,75,85,90,96]
print("Target list:" + str(myList))
print("Max:" + str(myMax(myList)))
print("Min:" + str(myMin(myList)))
print("Average:" + str(myAvge(myList)))
print("Sum:" + str(mySum(myList)))
print("")
print("-------------PART 2-------------")
myMatrix = [[1, 0, -1, 0, -1, 0, 0, -1],[-1, -2, -1, 0, -1, 0, 0, -1],[-1, 0, -1, 0, -1, -1, 0, -1],[-1, 0, 0, 0, 0, 0, 0, -1],[-1, 0, -1, -1, -1, 0, 0, -1],[-1, 0, 0, 0, 0, 0, 0, -1],[-1, 0, -1, 0, -1, 0, -2, -1],[-1, 0, -1, 0, -1, -1, 0, -1]]
endPoints = findPosition(myMatrix)
print("Target matrix:" + str(myMatrix))
print("Position of -2 are:" + str(endPoints))
print("Distance of -2 is:" + str(getDistance(endPoints[0],endPoints[1])))
print("Exit points:"+str(findExits(myMatrix)))
print("Data from file:")
#readFromFile('input.txt')

print("-------------PART 3-------------")
matrix = lee(myMatrix,endPoints[0],endPoints[1])
for item in matrix:
    print(item)
print("Drum de la tinta catre punctul de plecare: ")

print(traceBack(matrix,endPoints[1],endPoints[0]) )