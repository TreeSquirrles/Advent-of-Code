#have a grid
#traverse through the grid
#find a region, remove each one from the region into a separate list  
    #if number is arleady in checked list, then don't do it again
    #store number of shared borders, recursively call each one
    #number of not shared boarders = num borders - shared borders
    #go through and add perimeter up
#go the the next one that is still in the list
#rinse and repeat

lines = []
with open("AoC12/AdventOfCodeDay12.txt", "r") as text:
    lines = [line.strip() for line in text]

w, h = len(lines[0]), len(lines)

checkedGrids = set()

def r(x:int, y:int):
    a, p, letter = 1, 4, lines[y][x]
    for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= xx < w and 0 <= yy < h and lines[yy][xx] == letter:
            p -= 1
            if (xx, yy) not in checkedGrids:
                checkedGrids.add((xx, yy))
                a, p = a + (res := r(xx, yy))[0], p + res[1] # we love one liners

    return (a, p)

s = 0

for y in range(h):
    for x in range(w):
        if (x, y) not in checkedGrids:
            checkedGrids.add((x,y)) # very important
            a, p = r(x, y)
            s += a * p
        
print(s)