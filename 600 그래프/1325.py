import sys
from collections import deque
input = sys.stdin.readline


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


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
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
