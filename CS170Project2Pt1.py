import random

#random.random() # 0.0 to 1.0

def evaluation_function_dummy(Node):
    return random.random()

def toPercent(decimal):
    return decimal*100

def generate_accuracies(num):
    numList = []
    for i in range(num):
        numList.append(toPercent(evaluation_function_dummy(0)))
    return numList

def makeFeatureSet(numFeatures):
    mySet = []
    for i in range(numFeatures):
        mySet.append(i)
    return mySet

def generate_list_forward(nodeList, numFeatures):
    featureSet = makeFeatureSet(numFeatures)
    nodeSize = len(nodeList)
    numNodes = numFeatures - nodeSize
    aList = []
    unusedList = featureSet.difference(nodeList)
    for i in unusedList:
        aList.append(i)
        for j in range(nodeSize):
            aList[i].append(nodeList[j])
    return aList

def generate_list_backward(nodeList, numFeatures):
    nodeSize = len(nodeList)
    numNodes = numFeatures - nodeSize
    aList = []
    for i in range(len(nodeList)):
        aList.append(nodeList[:i] + nodeList[i + 1:])
    return aList

def listToString(aList):
    aString = ""
    for i in aList:
        aString = aString + i + ","
    return aString[:-1]

def forwardSelection(numFeatures):
    nodeSize = 1
    accuracy_i = 0
    accuracy_f = 0
    bestAccuracy = 0
    bestSubset = 0
    bestSubsetPercent = 0
    bestIndex = 0
    accList = []
    numList = []
    prevList = []
    while ((accuracy_i >= accuracy_f) and (len(prevList) < numFeatures)):
        accuracy_i = accuracy_f
        accList = generate_accuracies((numFeatures + 1 - nodeSize))
        accuracy_f = max(accList[:])
        numList = generate_list_forward(prevList, numFeatures)
        for i in range(len(accList)):
            print("Using feature(s) {" + listToString(numList[i]) + "} accuracy is " +  accList[i] + "%")
        #pick best feature subset to expand
        prevList = numList[accList.index(accuracy_f)]
    bestAccuracy = max(accuracy_f, accuracy[i])
    bestIndex = accList.index(bestAccuracy)
    bestSubset = numList[bestIndex]
    bestSubsetPercent = accuracy[bestIndex]

    return bestSubset, bestSubsetPercent

def backwardsElimination(numFeatures):
    nodeSize = numFeatures
    accuracy_i = 0
    accuracy_f = 0
    bestAccuracy = 0
    bestSubset = 0
    bestSubsetPercent = 0
    bestIndex = 0
    accList = []
    numList = []
    prevList = []
    while ((accuracy_i >= accuracy_f) and (nodeSize > 0)):
        accuracy_i = accuracy_f
        accList = generate_accuracies((numFeatures + 1 - nodeSize))
        accuracy_f = max(accList[:])
        numList = generate_list_backward(prevList, numFeatures) 
        for i in range(len(accList)):
            print("Using feature(s) {" + listToString(numList[i]) + "} accuracy is " +  accList[i] + "%")
        #pick best feature subset to expand
        prevList = numList[accList.index(accuracy_f)]
    bestAccuracy = max(accuracy_f, accuracy[i])
    bestIndex = accList.index(bestAccuracy)
    bestSubset = numList[bestIndex]
    bestSubsetPercent = accuracy[bestIndex]

    return bestSubset, bestSubsetPercent

def evaluation_program():
    print("Welcome to Scott Mesdjian's Feature Selection Algorithm.")
    userIn1 = 0
    while (int(userIn1) >= 1):
        input("Please enter total number of features: ")
    userIn2 = 0
    while (int(userIn2) > 0 and int(userIn2) < 2):
        print("Type the number of the algorithm you want to run.")
        print("\n1     Forward Selection \n2     Backward Elimination") #for extra credit: \n     Scott's Special Algorithm
        userIn2 = input("     ")
    accuracy = 0

    print("Using no features and \"random\" evaluation, I get an accuracy of " + accuracy)
    if (userIn2 == '1'):
        (bestSubset, bestSubsetPercent) = forwardSelection()
    elif(userIn2 == '2'):
        (bestSubset, bestSubsetPercent) = backwardElimination()
    #else: if we implement extra credit

    print("(Warning, accuracy has decreased!)")
    print("Finished search!! The best feature subset is {" + bestSubset + "}" + ", which has an accuracy of " + bestSubsetPercent + "%")
    
    return

def main():
    evaluation_program()

if __name__ == "__main__":
    main()

#todo: test
