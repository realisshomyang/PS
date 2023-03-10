import sys
from collections import deque

s = sys.stdin.readline().strip()

dq = deque()


def printtmp(tmp):
    if (len(tmp)):
        str = ''.join(tmp)
        a = str.split()
        for x in range(0, len(a)):
            if x == len(a)-1:
                print(a[x][::-1], end="")
            else:
                print(a[x][::-1], end=" ")


for x in s:
    dq.append(x)
tmp = []
while (len(dq)):
    a = dq.popleft()
    if a == "<":
        printtmp(tmp)
        tmp.clear()
        print(a, end="")
        while (len(dq)):
            b = dq.popleft()
            if b == ">":
                print(b, end="")
                break
            else:
                print(b, end="")
    else:
        tmp.append(a)

printtmp(tmp)
