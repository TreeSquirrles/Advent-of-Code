lines = []
with open("/Users/herky/Desktop/AoC/AoC4/AdventOfCodeDay4.txt", "r") as text:
    for l in text:
        lines.append(l.strip())
        
w = len(lines[0])
h = len(lines)

c = 0

def count(x, y):
    if (x == 0 and y == 0) or not (lines[x][y] == 'X'):
        return 0
    else:
        return sum([
            y > 2 and ''.join(lines[x][y-i] for i in range(4)) == 'XMAS',
            y < w - 3 and ''.join(lines[x][y+i] for i in range(4)) == 'XMAS',
            x > 2 and ''.join(lines[x-i][y] for i in range(4)) == 'XMAS',
            x < h - 3 and ''.join(lines[x+i][y] for i in range(4)) == 'XMAS',
            y > 2 and x > 2 and ''.join(lines[x-i][y-i] for i in range (4)) == 'XMAS',
            y > 2 and x < h - 3 and ''.join(lines[x + i][y-i] for i in range(4)) == 'XMAS',
            y < w - 3 and x > 2 and ''.join(lines[x - i][y+i] for i in range(4)) == 'XMAS',
            y < w-3 and x < h-3 and ''.join(lines[x+i][y+i] for i in range(4)) == 'XMAS'
        ])

c = sum(count(x, y) for x in range(h) for y in range(w))

print(c)

