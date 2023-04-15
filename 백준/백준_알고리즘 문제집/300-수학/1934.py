import sys

n = int(input())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a*b//gcd(a, b))
