with open("/Users/herky/Desktop/AoC/AoC10/AdventOfCodeDay10.txt", "r") as text:
    lines = [[int(c) for c in line.strip()] for line in text]

w, h = len(lines[0]), len(lines)

def yas(x, y, counter, gone):
    return 1 if counter == 9 and (x, y) not in gone and not gone.add((x, y)) else sum( yas(xx, yy, lines[yy][xx], gone)for xx, yy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]if 0 <= xx < w and 0 <= yy < h and lines[yy][xx] == counter + 1 )

print(sum(yas(j, i, 0, set()) for i, row in enumerate(lines) for j, e in enumerate(row) if e == 0))