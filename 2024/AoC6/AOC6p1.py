lines: list[list[str]] = []
with open("/Users/herky/Desktop/AoC/AoC6/input.txt", "r") as text:
    for l in text:
        line = l.strip()
        lines.append([])
        for letter in line:
            lines[len(lines)-1].append(letter)


guard_width: int = 47
guard_height: int = 45

print(lines[guard_height][guard_width])

direction_up: int = -1
direction_right: int = 0

# rotation matrix [[0 1][-1 0]]
def rotate():
    global direction_right, direction_up # oh no lsp

    new_direction_up = direction_right
    new_direction_right = -direction_up 

    direction_up = new_direction_up
    direction_right = new_direction_right 

count: int = 1;
while(True):
    guard_width += direction_right
    guard_height += direction_up
    if not (guard_width >= 0 and guard_width < len(lines[0]) and guard_height >= 0 and guard_height < len(lines)):
        break
    if lines[guard_height][guard_width] == '.':
        count += 1
        lines[guard_height][guard_width] = 'a'
    if lines[guard_height][guard_width] == '#':
        guard_width -= direction_right
        guard_height -= direction_up
        rotate()

print(count)
