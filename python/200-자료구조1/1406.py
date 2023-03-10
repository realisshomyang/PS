import sys
text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

stack1 = []
stack2 = []

for x in text:
    stack1.append(x)


for _ in range(n):
    c = sys.stdin.readline().strip()
    if c[0:1] == "P":
        stack1.append(c[2:])
    elif c[0:1] == "L":
        if (len(stack1) != 0):
            stack2.append(stack1.pop())
    elif c[0:1] == "D":
        if (len(stack2) != 0):
            stack1.append(stack2.pop())
    elif c[0:1] == "B":
        if (len(stack1) != 0):
            stack1.pop()

for x in stack1:
    print(x, end="")

stack2.reverse()
for x in stack2:
    print(x, end="")
