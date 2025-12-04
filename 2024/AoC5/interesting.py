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

"""
I took a look at the relations, it appears that all the relation lengths are different... woah that makes it very simple.

so, given a list of un sorted elements, find the middle element. 
"""
for i in range(len(pages)):
    print("break! ----------------")
    ok = False
    a = 0
    for n in pages[i]:
        rule = rules.get(n)
        d = []
        if rule:
            for r in rule:
                if r in pages[i]:
                    d.append(r)
            print(f"{n}: {d}")
        else:
            print(f"{n}: []")


"""
Notice how each update's pages have differing amounts of ordering!
"""
