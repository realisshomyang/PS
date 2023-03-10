import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())


def bfs(s):
    cnt = 1
    q = deque([s])
    visit = [False for _ in range(n+1)]
    visit[s] = True
    while q:
        cur = q.popleft()
        for nx in graph[cur]:
            if not visit[nx]:
                visit[nx] = True
                cnt += 1
                q.append(nx)
    return cnt


graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

maxc = 1
ans = []

for i in range(1, n+1):
    cnt = bfs(i)
    if cnt > maxc:
        maxc = cnt
        ans.clear()
        ans.append(i)
    elif cnt == maxc:
        ans.append(i)

print(*ans)
