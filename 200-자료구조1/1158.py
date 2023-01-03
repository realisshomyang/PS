from collections import deque

a, b = map(int, input().split())

dq = deque()

for x in range(1, a+1):
    dq.append(x)
ans = []
while (len(dq) != 0):
    dq.rotate(-(b-1))
    ans.append(dq.popleft())


print(str(ans).replace('[', '<').replace(']', '>'))

""" 
deque의 원형큐 성질을 생각하자!!!!!!!


"""
