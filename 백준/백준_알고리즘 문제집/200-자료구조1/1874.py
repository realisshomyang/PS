import sys
n = int(input())

lst = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
op = []
num = 1
isvalid = True
for x in lst:
    while (num <= x):
        stack.append(num)
        op.append('+')
        num += 1
    if stack[-1] == x:
        stack.pop()
        op.append('-')
    else:
        isvalid = False

if isvalid:
    for x in op:
        print(x)
else:
    print("NO")
