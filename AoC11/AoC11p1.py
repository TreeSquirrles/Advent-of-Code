import math

with open("/Users/herky/Desktop/AoC/AoC11/AdventOfCodeDay11.txt", "r") as text:
    lines = [int(c) for c in text.read().strip().split(" ")]

def split(l):
    new_list = []
    for num in l:
        if num == 0:
            new_list.append(1)
        elif (w := int(math.log10(num))+1) % 2 == 0:
            d = 10**(w/2)
            new_list.extend( [num // d, num % d])
        else:
            new_list.append(num * 2024)
    return new_list


for _ in range(25):
    lines = split(lines)

print(len(lines))
