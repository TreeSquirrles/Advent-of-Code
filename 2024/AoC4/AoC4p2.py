lines = []
with open("/Users/herky/Desktop/AoC/AoC4/AdventOfCodeDay4.txt", "r")  as text:
    for line in text:
        lines.append(line.strip())

w = len(lines[0])
h = len(lines)

def count(x, y):
    if lines[x][y] != 'A':
        return 0
    return 1 if sum([
        (h - 1 > x > 0) and (w - 1 > y > 0) and ((lines[x-1][y-1] == 'M' and lines[x+1][y+1] == 'S') or (lines[x-1][y-1] == 'S' and lines[x+1][y+1] == 'M')),
        (h - 1 > x > 0) and (w - 1 > y > 0) and ((lines[x+1][y-1] == 'M' and lines[x-1][y+1] == 'S') or (lines[x+1][y-1] == 'S' and lines[x-1][y+1] == 'M'))
    ]) == 2 else 0
    
c = sum(count(x, y) for x in range(h) for y in range(w))

print(c)