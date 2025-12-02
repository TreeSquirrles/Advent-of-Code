import re
ranges = []
with open("input.txt", "r") as input:
    s = input.readline().split()[0].split(",")
    for r in s:
        a, b = r.split("-")
        ranges.append([a, b])


count = 0
pattern = re.compile(r'^(\d+)\1+$')

for r in ranges:
    for i in range(int(r[0]), int(r[1]) + 1):
        if pattern.match(str(i)):
            count += i

print(count)
