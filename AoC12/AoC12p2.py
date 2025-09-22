lines = []
with open("AoC12/AdventOfCodeDay12.txt", "r") as text:
    lines = [line.strip() for line in text]
# with open("AoC12/test.txt", "r") as text:
#     lines = [line.strip() for line in text]
    
w, h = len(lines[0]), len(lines)

checkedGrids = {}

def r(x:int, y:int):
    a, p, letter, s = 1, 4, lines[y][x], []
    def b(x, y, w, h):
        return 0 <= x < w and 0 <= y < h

    for xx, yy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ax, ay = x+xx, y+yy
        if b(ax, ay, w, h) and lines[ay][ax] == letter:
            s.extend([[ax, ay]])
            p -= 1
            checkedGrids.setdefault((x, y), 4)
            checkedGrids[(x, y)] -= 1
        else: 
            for oox, ooy in [(x + yy, y + xx), (x - yy, y - xx)]:
                if b(oox, ooy, w, h) and lines[ooy][oox] == letter:
                    u = checkedGrids.get((oox, ooy))
                    if u and u > 0:  
                        dx, dy = ax + oox - x, ay + ooy - y # don't ask how this works
                        if not b(dx, dy, w, h) or lines[dy][dx] != letter:
                            p -= 1  
                
    for i, j in s:
        if checkedGrids.get((i, j)) == None:
            checkedGrids[(i, j)] = 4
            a, p = a + (res := r(i, j))[0], p + res[1] # we love one liners
    return (a, p)
#one liner heaven
print(sum((rr := r(x, y))[0] * rr[1] for y in range(h) for x in range(w) if (x, y) not in checkedGrids))