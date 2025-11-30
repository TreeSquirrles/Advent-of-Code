input = ""
with open("AoC9/AdventOfCodeDay9.txt", "r") as text:
    input = text.read().strip()

pi = []
fi = [int(input[i]) for i in range(0,len(input), 2)]
fiCopy = list(fi)
bi = [int(input[i]) for i in range(1,len(input), 2)]

#we love excessive one liners
bi.append(0) if len(fi) > len(bi) else None

for i, block in enumerate(input):
    pi.extend([str(i // 2) if i % 2 == 0 else "."] * int(block))
    
b = len(pi)
for backcursor in range(1, len(fi)):
    d = 0
    b -= (fiCopy[-backcursor] + bi[-backcursor])
    for i in range(len(bi) - backcursor):
        d += fiCopy[i]
        if fi[-backcursor] <= bi[i]:
            bi[i] -= fi[-backcursor]
            fiCopy[i] += fi[-backcursor]
            pi[d:d+fi[-backcursor]] = [f"{len(fi) - backcursor}"] * fi[-backcursor]
            pi[b:b+fi[-backcursor]] = ["."] * fi[-backcursor]
            break
        d += bi[i]
            
print("sum:",sum(int(v)*i for i, v in enumerate(pi) if v != ".")   )

