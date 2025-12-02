ranges = []

with open("input.txt", "r") as input:
    s = input.readline().split()[0].split(",")
    for r in s:
        a, b = r.split("-")
        ranges.append([a, b])

"""
dumb solution, but hopefully won't take too long. 
"""

count = 0
for r in ranges:
    for i in range(int(r[0]), int(r[1]) + 1):
        string_i = str(i)
        first_half = string_i[0:int(len(string_i)/2)]
        second_half = string_i[int(len(string_i)/2):]
        if first_half == second_half:
            count += i

print(count)

"""
update: It did not take too long
"""
