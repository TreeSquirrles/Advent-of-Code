with open("AoC9/AdventOfCodeDay9.txt", "r") as text:
    diskMap = list(text.read())
    blocks = [[i for _ in range(int(v))] for i, v in enumerate(diskMap[::2])]
    spaces = [list("."*int(v)) for v in diskMap[1::2]]
    full = []
    for i, val in enumerate(blocks):
        full.append(val)
        if i >= len(spaces):
            continue
        full.append(spaces[i])

    completed = []
    fC = False
    while True:
        sC = False
        for i, val in enumerate(full[::-1]):
            if "." in val or len(val) == 0 or val[0] in completed:
                continue
            for j, space in enumerate(full):
                if j >= len(full) - 1 - i:
                    break
                if len(space) >= len(val) and '.' in space:
                    full[j] = full[j][len(val):]
                    full.insert(j, val)
                    full[len(full) - 1 - i] = list('.'*len(val))
                    completed.append(val[0])
                    sC = True
                    break
            if i == len(full) - 1:
                fC = True
            if sC:
                break
        if fC:
            break

    count = 0
    for i, val in enumerate(sum(full, [])):
        if val == '.':
            continue
        count += i*val
    print(count)