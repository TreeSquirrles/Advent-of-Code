ranges = []
nums = []
with open("input.txt", "r") as input:
    t = input.read().strip().split("\n\n")
    r = t[0].split("\n")
    for i in range(len(r)):
        dloc = r[i].index("-")
        ranges.append(int(r[i][:dloc]))
        ranges.append(int(r[i][dloc + 1:]))

    nums = [i for i in map(int, t[1].split("\n"))]


def binary(n, l):
    low = 0
    high = len(l)

    while low < high:
        mid = (low + high) // 2
        if l[mid] <= n:
            low = mid + 1
        else:
            high = mid
    return low

#doesn't actually sort correctly. Ignore this.
sorted = [ranges[0], ranges[1]]
for i in range(2, len(ranges), 2):

    lowBound = binary(ranges[i], sorted)  # indexes
    highBound = binary(ranges[i + 1], sorted)

    if highBound == lowBound and highBound % 2 == 0:
        sorted.insert(lowBound, ranges[i + 1])
        sorted.insert(lowBound, ranges[i])
        continue

    if highBound % 2 == 0:
        sorted[highBound - 1] = ranges[i + 1]
        highBound -= 1
    if lowBound % 2 == 0:
        sorted[lowBound] = ranges[i]
    else:
        lowBound -= 1
    for j in range(highBound - lowBound - 1):
        sorted.pop(lowBound + 1)

count = 0
for num in nums:
    f = binary(num, sorted)
    if f % 2 == 1:
        count += 1

print(count)

