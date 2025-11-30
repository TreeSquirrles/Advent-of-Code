import copy
#I know there is a better solution. I could never come up with one...
# Wait... so my old solution actually was slightly ok...
lines = []
with open("/Users/herky/Desktop/AoC/AoC6/input.txt", "r") as text:
    for l in text:
        line = l.strip()
        lines.append([])
        for letter in line:
            lines[len(lines) - 1].append(letter)

board_width = len(lines[0])
board_height = len(lines)

guard_x: int = 0
guard_y: int = 0

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "^":
            guard_x = j
            guard_y = i

start_x = guard_x
start_y = guard_y

up: int = -1
side: int = 0

"""
Since an array is ordered a bit weirdly, the correct rotation matrix is:
    __    __
| 0 -1 |
| 1  0 |
--    --
"""


def rotate_clockwise(x, y):
    temp = x
    x = -y
    y = temp
    return x, y


def within_bounds(x, y):
    in_width = x >= 0 and x < board_width
    in_height = y >= 0 and y < board_height
    return in_width and in_height


def print_board(l):
    for line in l:
        for letter in line:
            print(letter, end="")
        print()
    print("--------------------------")


def get_direction(up, side) -> str:
    if up == 1 and side == 0:
        return "d"
    if up == -1 and side == 0:
        return "u"
    if up == 0 and side == 1:
        return "r"
    if up == 0 and side == -1:
        return "l"
    return "b"


lines[guard_y][guard_x] = "a"
lines_cpy = copy.deepcopy(lines)

visited = ((guard_x, guard_y, "u"),)

counter = 1;

while True:
    guard_x += side
    guard_y += up

    if not within_bounds(guard_x, guard_y):
        break

    if lines[guard_y][guard_x] == ".":
        visited += ((guard_x, guard_y, get_direction(up, side)),)
        lines[guard_y][guard_x] = "a"
        counter += 1

    if lines[guard_y][guard_x] == "#":
        guard_x -= side
        guard_y -= up
        side, up = rotate_clockwise(side, up)


cpy_x = start_x
cpy_y = start_y
up = -1
side = 0

loops = 0
cpv = ()
for i in range(1, len(visited)):
    lines_cpy[visited[i][1]][visited[i][0]] = "#"

    while True:
        cpy_x += side
        cpy_y += up
        
        if not within_bounds(cpy_x, cpy_y):
            break

        if (cpy_x, cpy_y, get_direction(up, side)) in cpv:
            loops += 1
            print("loop found!" + str(loops))
            break
        
        if lines_cpy[cpy_y][cpy_x] == ".":
            cpv += ((cpy_x, cpy_y, get_direction(up, side)),)
            lines_cpy[cpy_y][cpy_x] = "a"

        if lines_cpy[cpy_y][cpy_x] == "#":
            cpy_x -= side
            cpy_y -= up
            side, up = rotate_clockwise(side, up)

    lines_cpy[visited[i][1]][visited[i][0]] = "."
    cpy_x = start_x
    cpy_y = start_y
    for j in range(len(cpv)):
        lines_cpy[cpv[j][1]][cpv[j][0]] = "."
    cpv = ()
    up = -1
    side = 0

print(f" loops: {loops}")
print(f" {guard_x}, {guard_y} ")
print(f"{counter}")
print(f"{len(visited)}")
