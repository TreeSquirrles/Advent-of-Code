firstDestination = []
secondDestionation = []

with open("AdventOfCodeDay1.txt", "r") as text:
    t = text.read()
    splitT = t.split("\n")
    
    for i in range(len(splitT)):
        betterSplitT = splitT[i].split("   ")


        firstDestination.append(int(betterSplitT[0]))
        secondDestionation.append(int(betterSplitT[1]))
        
    firstDestination.sort()
    secondDestionation.sort()

    sum = 0

    for i, _ in enumerate(firstDestination):
        sum += firstDestination[i] * secondDestionation.count(firstDestination[i])
    
    print(sum)