"""
The stupidest meta solution ever

It isn't even faster than a normal comparison sorting general solution

But it's so funny that I can't not solve it this way

Leave it to the puzzle creator to create a relation space that looks the way it does.

I know "relation space" isn't the actual correct term or whatever but who cares.

Run interesting.py on the puzzle specific inputs to see something very interesting about sorted and unsorted elements. 
"""

import time

start_time = time.perf_counter()
rules = {}
pages = []
chunks = []
with open("input.txt") as text:
    chunks = text.read().strip().split("\n\n")

for rule in chunks[0].split("\n"):
    start, end = map(int, rule.strip().split("|"))
    rules.setdefault(start, set()).add(end)

for page in chunks[1].split("\n"):
    pages.append([int(a) for a in page.split(",")])

sum = 0

def out_of_place(arr, n, d):
    l = len(arr)
    if arr[l - d - 1 ] != n:
        return True
    return False
    
for i in range(len(pages)):
    nums = pages[i]
    numsl = len(nums)
    ok = False
    to_add = 0
    for n in nums:
        rule = rules.get(n)
        d = 0
        if rule: #append all elements that relate to this set
            for r in rule:
                if r in nums:
                    d += 1

        if d == len(nums)//2:
            to_add = n
        if out_of_place(nums, n, d): #if the place of the number doesn't equal the expected sorted position
            ok = True

    if ok:
        sum += to_add
        to_add = 0
        ok = False

print(sum)

end_time = time.perf_counter()

print(f"runtime {end_time - start_time}")
