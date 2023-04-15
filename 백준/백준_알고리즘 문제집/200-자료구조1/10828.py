import sys
n = int(sys.stdin.readline())
stack = []


def isempty():
    if len(stack) == 0:
        return 1
    else:
        return 0


for _ in range(n):
    a = sys.stdin.readline().strip()
    if a[0:4] == "push":
        stack.append(int(a[5:]))
    elif a == "top":
        if isempty():
            print(-1)
        else:
            print(stack[-1])
    elif a == "size":
        print(len(stack))
    elif a == "pop":
        if (isempty()):
            print(-1)
        else:
            print(stack.pop())
    elif a == "empty":
        print(isempty())
