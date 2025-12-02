"""
May not have done it the fastest, but I am sure proud of this solution (: 
Could reach O(n) time compexity and O(1) space by not storing everything in a list but whatever
"""

instructions = []
with open("input.txt", "r") as input:
    for instruction in input:
        s = instruction.split()
        instructions.append([s[0][0], s[0][1:]])

location = 50
one = 0
two = 0


def spin(tup):
    global location, one, two

    start = location
    dir = tup[0]
    amount = int(tup[1])

    if dir == "R":
        location = location + amount
    elif dir == "L":
        start = (100 - start) % 100  # sneaky range fix
        location = location - amount

    range_modulo = amount % 100
    two += (start + range_modulo) // 100 + amount // 100

    location = location % 100

    if location == 0:
        one += 1


for i in instructions:
    spin(i)

print(one)
print(two)
