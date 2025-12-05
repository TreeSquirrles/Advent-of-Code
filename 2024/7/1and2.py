import math
rules = {}
with open("input.txt", "r") as input:
    for line in input:
        stripped = line.strip()
        key, sep, value = stripped.partition(": ")
        value = [i for i in map(int, value.split())]
        rules[int(key)] = value

count = 0

"""
Could implement tree pruning?
Would be a faster solution. 

Maybe practice that one later
"""

def permutations(a: str, b: str, n):
    out = []
    for i in range(1<<n): #create n bits, loop thru all partitions
        s = ""
        for j in range(n): #for each bit
            
            if (i & 1<<j):
                s += a
            else:
                s += b
        out.append(s)
    return out

def trimutations(a, b, c, n):
    symbols = (a, b, c)
    out = []
    for i in range(3**n): # create n qbits?
        s = ""
        for j in range (n):
            trimute_digit = (i//(3 ** j)) % 3
            s += symbols[trimute_digit]
        out.append(s)
    return out

print(trimutations("a", "b", "c", 3))
    
p1 = 0
p2 = 0
ok = False
for goal, nums in rules.items():
    for perm in permutations("1", "0", len(nums)-1):
        match = nums[0]
        for i, op in enumerate(perm):
            if int(op) == 1:
                match *= nums[i+1]
            if int(op) == 0:
                match += nums[i+1]
        if match == goal:
            p1 += goal
            p2 += goal
            ok = True
            break
    if ok:
        ok = False
        continue
    for tri in trimutations("2", "1", "0", len(nums)-1):
        match = nums[0]
        for i, op in enumerate(tri):
            if int(op) == 2:
                match = int(str(match) + str(nums[i+1]))
            if int(op) == 1:
                match *= nums[i+1]
            if int(op) == 0:
                match += nums[i+1]
        if match == goal:
            p2 += goal
            print(p2)
            break


print(p1)
print(p2)
