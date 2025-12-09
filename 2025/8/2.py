import sys
import math

cycles = []

points = [list(map(int, line.split(",")))
          for line in sys.stdin.read().splitlines()]

cpy = []

pairs = []

def dist(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]

    return round(math.sqrt(dx**2 + dy**2 + dz**2), 3)

for i in range(len(points)):
    for j in range(i+1, len(points)):
        pairs.append((i, j, dist(points[i], points[j])))

pairs.sort(key=lambda x: x[2])
p2 = 0
i = 0
while True:
    packet = pairs[i]
#    print(pairs[i])
#    print(points[pairs[i][0]])
#    print(points[pairs[i][1]])

    if points[pairs[i][0]] not in cpy:
        cpy.append(points[pairs[i][0]])
    if points[pairs[i][1]] not in cpy:
        cpy.append(points[pairs[i][1]])

    zc = set()
    oc = set()
    for cycle in cycles:
        if packet[0] in cycle:
            zc = cycle
        if packet[1] in cycle:
            oc = cycle 
    
    if zc != set() and oc == set():
        zc.add(packet[1])
    if oc != set() and zc == set():
        oc.add(packet[0])
    if zc != set() and oc != set() and zc != oc:
        cycles.remove(zc)
        cycles.remove(oc)
        cycles.append(zc.union(oc))
    if zc == set() and oc == set():
        cycles.append({packet[0], packet[1]})

    if len(cycles) == 1 and sorted(points) == sorted(cpy):
        p2 = points[pairs[i][0]][0] * points[pairs[i][1]][0]
        break
    i += 1

print(p2)
