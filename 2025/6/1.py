import sys
D = sys.stdin.read()

A = []
for i, line in enumerate(D.split("\n")):
    line = line.split()
    A.append([a.strip() for a in line])

A = A[:-1]

p1 = 0

for l in range(len(A[:-1])):
    A[l] = [a for a in map(int, A[l])]

for i in range(len(A[0])):
    op = A[-1][i] 
    s = 0
    ok = True
    for n in range(len(A) - 1):
        if op == '+':
            s += A[n][i]
        if op == "*":
            if s == 0 and ok:
                s = 1
                ok = False
            s *= A[n][i]
    p1 += s

print(p1)
            
            


