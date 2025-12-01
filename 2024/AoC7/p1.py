rules = {}
with open("input.txt", "r") as input:
    for line in input:
        stripped = line.strip()
        key, sep, value = stripped.partition(": ")
        value = value.split()
        rules[key] = value

count = 0

for key, value in rules.items():
    total = value[0]
    pivot = 0
    value = value[1:]
