with open("/Users/herky/Desktop/AoC/AoC10/AdventOfCodeDay10.txt", "r") as text:
    lines = [[int(c) for c in line.strip()] for line in text]

w, h = len(lines[0]), len(lines)

def yas(x, y, counter):
    if counter == 9: # same thing from part 1 except we don't keep track of unique peaks
        return 1
    return sum(
        yas(xx, yy, lines[yy][xx])
        for xx, yy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        if 0 <= xx < w and 0 <= yy < h and lines[yy][xx] == counter + 1
    )

total_sum = sum(
    yas(j, i, 0)
    for i, row in enumerate(lines)
    for j, e in enumerate(row)
    if e == 0
)

print(total_sum)