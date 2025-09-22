import re as regex

sum = 0

textCopy = ''
y = 0
with open("/Users/herky/Desktop/AoC/AoC3/AdventOfCodeDay3.txt", "r+") as text:
    text.seek(0)
    textCopy = text.read()
    y = 1

d = regex.search("don't\(\)", textCopy)
canDo = ""
canDo += textCopy[:d.start()]
textCopy[d.end():]
i = 0

while d != None:
    if i % 2 == 0:
        d = regex.search("do\(\)", textCopy)
    else:
        d = regex.search("don't\(\)", textCopy)
        if d:
            canDo += textCopy[:d.start()]
    if d:
        textCopy = textCopy[d.end():]
    i += 1

m = regex.search("mul\([0-9]+,[0-9]+\)", canDo)

while(m != None):
    s = canDo[m.start()+4:m.end()-1].split(",")
    sum += int(s[0]) * int(s[1])
    canDo = canDo[m.end():]
    m = regex.search("mul\([0-9]+,[0-9]+\)", canDo)
    

print(sum)

    