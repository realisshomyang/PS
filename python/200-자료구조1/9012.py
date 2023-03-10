import sys
a = int(sys.stdin.readline())
lst = []


def isvalid(a):
    for x in a:
        if x == '(':
            lst.append('(')
        else:
            if len(lst) == 0:
                return -1
            else:
                lst.pop()
    if len(lst) == 0:
        return 1
    else:
        lst.clear()
        return -1


for _ in range(a):
    a = sys.stdin.readline().strip()
    if (isvalid(a) == 1):
        print("YES")
    else:
        print("NO")
