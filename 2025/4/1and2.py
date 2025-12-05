import time


start = time.perf_counter()
lines = []

with open("input.txt", "r") as input:
    for line in input:
        lines.append([l for l in line.strip()])

rows = len(lines)
cols = len(lines[0])

count = 0

def lessThanAmountNeighbors(x, y, amt):
    leftEdge = x == 0
    rightEdge = x == cols - 1
    
    topEdge = y == 0
    bottomEdge = y == rows - 1
    c = 0
    if not leftEdge:
        if not topEdge:
            c += 1 if lines[y-1][x-1] == "@" else 0
        if not bottomEdge:
            c += 1 if lines[y+1][x-1] == "@" else 0
        c += 1 if lines[y][x-1] == "@" else 0

    if not rightEdge:
        if not topEdge:
            c += 1 if lines[y-1][x+1] == "@" else 0
        if not bottomEdge:
            c += 1 if lines[y+1][x+1] == "@" else 0
        c += 1 if lines[y][x+1] == "@" else 0

    if not topEdge:
        c += 1 if lines[y-1][x] == "@" else 0

    if not bottomEdge:
        c += 1 if lines[y+1][x] == "@" else 0
            
    return c < amt        
        
t = 0
def once():
    p = 0
    for y in range(rows):
        for x in range(cols):
            if lessThanAmountNeighbors(x, y, 4) and lines[y][x] == "@":
                lines[y][x] = "."
                p += 1
    return p

while True:
    u = once()
    if u == 0:
        break
    t += u
print(t)
end = time.perf_counter()

print(f"runtime: {end - start} seconds")
