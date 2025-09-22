with open("/Users/herky/Desktop/AoC/AoC10/AdventOfCodeDay10.txt", "r") as text:
    lines = [[int(c) for c in line.strip()] for line in text]

w, h = len(lines[0]), len(lines)

def yas(x, y, counter, gone):
    if counter == 9 and (x, y) not in gone: #base case
        gone.add((x, y))
        return 1
    return sum(
        yas(xx, yy, lines[yy][xx], gone) 
        for xx, yy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] #adj squares
        if 0 <= xx < w and 0 <= yy < h and lines[yy][xx] == counter + 1 #right number
    )

total_sum = sum(
    yas(j, i, 0, set())
    for i, row in enumerate(lines)
    for j, e in enumerate(row)
    if e == 0
)

print(total_sum)