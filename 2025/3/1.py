lines = []
with open("input.txt", "r") as input:
    for line in input:
        lines.append(line.strip())

one = 0

def find(s):
    p = [int(a) for a in s]
    print(p)
    np = sorted(p, reverse=True)
    return np[0], s.find(str(np[0]))

for line in lines:
    l, i = find(line[0:-1])
    sl, _ = find(line[i+1:])
    one += l * 10 + sl


print(one)
