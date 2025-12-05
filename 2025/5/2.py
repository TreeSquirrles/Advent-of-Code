"""
I hate this problem. It took forever. Just look at problem 1 to see how much over engineering I did ):.

I don't feel good about this solution at all.
I could've reached it so much faster if I hadn't though of doing a stupid thing like part 1. 

I tried to be fancy...
"""

a = []
with open("input.txt", "r") as input:
    t = input.read().strip().split("\n\n")
    r = t[0].split("\n")
    for i in range(len(r)):
        dloc = r[i].index("-")
        a.append((int(r[i][:dloc]), 0))
        a.append((int(r[i][dloc + 1:]), 1))

a.sort()

p = 0
ends = 0
start = None

for num, typ in a:
    if typ == 0:
        ends += 1
        if ends == 1:
            start = num
    else:
        ends -= 1
        if ends == 0:
            p += num - start + 1

print(p)

