import sys

D = sys.stdin.read()

D = D.split("\n")[:-1]

A = []
for line in D:
    A.append(line)

G = []

point = 0
for i in range(1, len(A[-1])):
    if not A[-1][i].isspace():
        G.append([A[-1][point:i-1]])
        for l in A[-2::-1]:
            G[len(G)-1].insert(0, l[point:i-1])
        point = i

G.append([A[-1][point:]])
for l in A[-2::-1]:
    G[len(G)-1].insert(0, l[point:])

print(G)

p2 = 0

for group in G:
    op = group[-1][0]
    print(op)
    temp = 0
    ok = True
    for i in range(len(group[0])-1 , -1, -1):
        calcnum = ""
        for num in group[:-1]:
            if not num[i].isspace():
                calcnum += num[i]
        if op == "+":
            temp += int(calcnum)
        if op == "*":
            if temp == 0 and ok:
                temp = 1
                ok = False
            temp *= int(calcnum)

    print(temp)
    p2 += temp

print(p2)
