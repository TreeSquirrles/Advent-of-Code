import re as regex

sum = 0
textCopy = ''
y = 0

with open("/Users/herky/Desktop/AoC/AoC3/AdventOfCodeDay3.txt", "r+") as text:
    text.seek(0)
    textCopy = text.read()
    y = 1

m = regex.search("mul\([0-9]+,[0-9]+\)", textCopy)

while(m != None):
    s = textCopy[m.start()+4:m.end()-1].split(",")
    sum += int(s[0]) * int(s[1])
    textCopy = textCopy[m.end():]
    m = regex.search("mul\([0-9]+,[0-9]+\)", textCopy)
    
print(sum)