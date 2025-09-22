lines = []
sickDict = {}
with open("/Users/herky/Desktop/AoC/AoC8/AdventOfCodeDay8.txt", "r") as text:
    lines = [line.strip() for line in text]

for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if letter != '.':
            sickDict.setdefault(letter, []).append((x, y))

h, w = len(lines), len(lines[0])
count = 0
takenSpaces = set()

for frequency, antennas in sickDict.items():
    if len(antennas) < 2:
        continue

    for i, (x1, y1) in enumerate(antennas):
        for x2, y2 in antennas[i + 1:]:
            for nx, ny in [(x2 + (x2 - x1), y2 + (y2 - y1)), (x1 + (x1 - x2), y1 + (y1 - y2))]:
                if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in takenSpaces:
                    takenSpaces.add((nx, ny))
                    count += 1

print(count)
