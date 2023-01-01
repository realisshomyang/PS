import sys

a = int(sys.stdin.readline())

for _ in range(a):
    a = sys.stdin.readline().split()
    for x in a:
        print(x[::-1], end=" ")
    print("")
