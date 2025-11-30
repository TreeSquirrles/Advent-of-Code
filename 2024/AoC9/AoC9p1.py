with open("AoC9/AdventOfCodeDay9.txt", "r") as text:
    input = text.read().strip()

pi = []
sum = 0

for i, block in enumerate(input):
    pi+= [str(i // 2) if i % 2 == 0 else "." for _ in range(int(block))]

j = len(pi) - 1
for i in range(len(pi)):
    if pi[i] == ".":
        while j > i:
            if pi[j] != ".":
                pi[i], pi[j] = pi[j], "."
                break
            j -= 1
    else:
        sum += i * int(pi[i])

print(sum)
