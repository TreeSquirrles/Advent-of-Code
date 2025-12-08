import sys

A = [ list(line) for line in sys.stdin.read().splitlines()]

s = A[0].index("S")

gone = dict()
def flowDown(x, y ):
    gone[(y, x)] = 0;
    while A[y][x] != "^":
        if y == len(A) - 1:
            return 1
        A[y][x] = "|"
        y += 1

    left = 0 
    right = 0
    if (y, x-1) in gone:
        left = gone[(y, x-1)]
    else:
        left = flowDown(x-1, y)
        gone[(y, x-1)] = left
    
    if (y, x+1) in gone:
        right =  gone[(y, x+1)]
    else:
        right = flowDown(x+1, y)
        gone[(y, x+1)] = right

    return left + right

print(flowDown(s, 0))

