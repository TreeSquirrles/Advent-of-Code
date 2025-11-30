lines: list[list[str]] = []
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

def print_board():
    for line in lines:
        for letter in line:
            print(letter, end='')
        print()
    print("--------------------------")


def same_direction(x, y, dir_x, dir_y):
    is_up = dir_y == -1 and dir_x == 0 and lines[y][x] == "^"
    is_down = dir_y == 1 and dir_x == 0 and lines[y][x] == "v"
    is_right = dir_y == 0 and dir_x == 1 and lines[y][x] == ">"
    is_left = dir_y == 0 and dir_x == -1 and lines[y][x] == "<"
    if is_up or is_down or is_right or is_left:  # up
        return True
    return False

def wall_or_bust(x, y, dir_x, dir_y, depth:int):
    while True:
        x += dir_x
        y += dir_y
        if not within_bounds(x, y):
            return False

        if same_direction(x, y, dir_x, dir_y):
            print(f"    spot({dir_x}{dir_y})")
            print(f"    spot({x}, {y}){lines[y][x]}")
            return True

        if lines[y][x] == "#":
            if depth > 50:
                return False
            print(f"    ({dir_x}, {dir_y})")
            if wall_or_bust(
                x - dir_x, y - dir_y, *rotate_clockwise(dir_x, dir_y), depth + 1
                ):
                return True
            else:
                return False


count = 0
traversed_tiles = 1
while True:
    guard_x += side
    guard_y += up
    print(f"current position: {guard_x}, {guard_y}")
    #print_board()

    if not within_bounds(guard_x, guard_y):
        break

    if lines[guard_y][guard_x] == "#":
        guard_x -= side
        guard_y -= up
        side, up = rotate_clockwise(side, up)
        print("hit a wall!")
        continue

    if lines[guard_y][guard_x] == ".":
        if up == -1 and side == 0:
            lines[guard_y][guard_x] = "^"
            print("going up")
        elif up == 1 and side == 0:
            lines[guard_y][guard_x] = "v"
            print("going down")
        elif up == 0 and side == 1:
            lines[guard_y][guard_x] = ">"
            print("going right")
        elif up == 0 and side == -1:
            lines[guard_y][guard_x] = "<"
            print("going left")
        traversed_tiles += 1
    
    old = ""
    if within_bounds(guard_x + side, guard_y+up):
        old = lines[guard_y + up][guard_x + side]
        lines[guard_y + up][guard_x + side] = "#"

    if wall_or_bust(guard_x, guard_y, *rotate_clockwise(side, up), 0):
        print("Woah! loopable!")
        count += 1

    if within_bounds(guard_x + side, guard_y + up):
        lines[guard_y + up][guard_x + side] = old
    

print()
print(f"Starting Pos: {start_x}, {start_y}")
print()
print(f"loopable areas: {count}")
print(f"traversed tiles: {traversed_tiles}")
