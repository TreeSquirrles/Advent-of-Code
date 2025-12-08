import sys

A = [ list(line) for line in sys.stdin.read().splitlines()]

s = A[0].index("S")

p1 = 0

gone = set()
def flowDown(x, y ):
    global p1
    gone.add((y, x));
    while A[y][x] != "^":
        if y == len(A) - 1:
            return
        A[y][x] = "|"
        y += 1
    
    if not (y, x-1) in gone or not (y, x+1) in gone:
        p1 += 1
    #A[y][x] = chr(ord("A") + p1)

    if not (y, x - 1) in gone: flowDown(x - 1, y)
    if not (y, x + 1) in gone:  flowDown(x + 1, y)

flowDown(s, 0)

for a in A:
    print(''.join(a))


print(p1)


