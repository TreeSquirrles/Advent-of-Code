import sys

print(sys.stdin.read())

def gcd(a:int, b:int):
    if a == b:
        return a
    gcd(min(a, b), abs(a - b))

print(gcd(252, 105))
