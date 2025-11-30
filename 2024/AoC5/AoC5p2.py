rules = {}
chunks = []
with open("AoC5/test.txt") as text:
    chunks = text.read().strip().split("\n\n")


for rule in chunks[0].split("\n"):
    start, end = map(int, rule.strip().split("|"))
    rules.setdefault(start, set()).add(end)
    
s = 0
for book in chunks[1].split("\n"):
    pages = list(map(int, book.split(",")))
    middle = pages[len(pages)//2]
    f = True
    seenPages = set()
        
    for page in pages:
        r = rules.get(page)
        if r and len(r & seenPages) != 0:
            f = False
            break
        seenPages.add(page)
    if f:   
        s += middle

print(s)