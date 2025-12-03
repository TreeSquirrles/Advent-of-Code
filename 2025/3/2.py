lines = []
with open("input.txt", "r") as input:
    for line in input:
        lines.append(line.strip())

two = 0

def find(s):
    p = [int(a) for a in s]
    np = sorted(p, reverse=True)
    return np[0], s.find(str(np[0])) 

for line in lines:
    trimmedLine = line
    num = 0
    indexFound = 0
    for i in range(12):
        actual = trimmedLine[:-11 + i]
        if i == 11:
            actual = trimmedLine # list[:0] deletes the entire list... took me a bit to figure that one out
        largestDigit, indexFound = find(actual)
        trimmedLine = trimmedLine[indexFound + 1:] 
        num += largestDigit * 10 ** (11-i)
    two += num

print(two)
