import math

def split_number(num):
    num_digits = int(math.log10(num)) + 1
    midpoint = num_digits // 2
    divisor = 10 ** midpoint
    return num // divisor, num % divisor


def simulate(stoneCount, i):
    for _ in range(i):
        new_counts = {}
        for num, count in stoneCount.items():
            if num == 0:
                new_counts[1] = new_counts.get(1, 0) + count
            elif len(str(num)) % 2 == 0:
                left, right = split_number(num)
                new_counts[left] = new_counts.get(left, 0) + count
                new_counts[right] = new_counts.get(right, 0) + count
            else:
                new_num = num * 2024
                new_counts[new_num] = new_counts.get(new_num, 0) + count
        stoneCount = new_counts
    return sum(stoneCount.values())

s = simulate({0:1, 7:1, 198844:1, 5687836:1, 58:1, 2478:1, 25475:1, 894:1}, 75)
print(s)