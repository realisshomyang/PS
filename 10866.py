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
    if a[0:10] == "push_front":
        q.appendleft(int(a[11:]))
    elif a[0:9] == "push_back":
        q.append(int(a[10:]))
    elif a[0:9] == "pop_front":
        if isempty():
            print(-1)
        else:
            print(q.popleft())
    elif a[0:8] == "pop_back":
        if isempty():
            print(-1)
        else:
            print(q.pop())

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
    elif a == "empty":
        print(isempty())
