from math import copysign as cpys

counter = 0
with open("AoC2/AdventOfCodeDay2.txt", "r") as text:
    
    reports = text.read().split("\n")

    counter = len(reports)

    for report in reports:
        numbers = report.split(" ")

        sign = cpys(1, int(numbers[0]) - int(numbers[-1]))
        
        for i in range(len(numbers) - 1):

            diff = int(numbers[i]) - int(numbers[i+1])
            
            if cpys(1, diff) != sign:
                counter -= 1
                break

            if abs(diff) < 1 or abs(diff) > 3: 
                counter -= 1
                break


        


    print(counter)

    text.close()