from math import copysign as cpys

with open("AoC2/AdventOfCodeDay2.txt", "r") as text:
    reports = text.read().split("\n")
    counter = 0
    for report in reports:
        numbers = report.split(" ")
        b = False
        sign = cpys(1, int(numbers[0]) - int(numbers[-1]))
        
        #for regulars
        for i in range(len(numbers)-1):
            diff = int(numbers[i]) - int(numbers[i+1])
            if cpys(1, diff) != sign or not (1 <= abs(diff) <= 3):
                break
            if i == len(numbers)- 2:
                counter += 1   
                b = True
            
        #now for the wee thing
        #0 1 100 3 4 : neg sign
        for i in range(len(numbers)):
            if b:
                break
            copy = numbers.copy()
            copy.pop(i)
            sign = cpys(1, int(copy[0]) - int(copy[-1]))
            for v in range(len(copy) - 1):
                diff = int(copy[v]) - int(copy[v+1])
                if cpys(1, diff) != sign or not (1 <= abs(diff) <= 3):
                    break
                if v == len(copy) - 2:
                    counter += 1
                    b = True

    print(counter)

    text.close()