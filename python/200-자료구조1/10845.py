import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque()


def isempty():
    if len(q) == 0:
        return 1
    else:
        return 0


for _ in range(n):
    a = sys.stdin.readline().strip()
    if a[0:4] == "push":
        q.append(int(a[5:]))
    elif a == "back":
        if isempty():
            print(-1)
        else:
            print(q[-1])
    elif a == "front":
        if isempty():
            print(-1)
        else:
            print(q[0])
    elif a == "size":
        print(len(q))
    elif a == "pop":
        if (isempty()):
            print(-1)
        else:
            print(q.popleft())
    elif a == "empty":
        print(isempty())
