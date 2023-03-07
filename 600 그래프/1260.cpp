#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
const int MAX = 1001;

vector<int> graph[MAX];
bool visited[MAX];

void dfs(int sNode)
{
    visited[sNode] = true;
    cout << sNode << " ";
    for (int i = 0; i < graph[sNode].size(); i++)
    {
        int y = graph[sNode][i];
        if (!(visited[y]))
        {
            dfs(y);
        }
    }
}

void bfs(int sNode)
{
    queue<int> q;
    q.push(sNode);
    visited[sNode] = true;
    while (!q.empty())
    {
        int x = q.front();
        q.pop();
        cout << x << " ";
        for (int i = 0; i < graph[x].size(); i++)
        {
            int y = graph[x][i];
            if (!visited[y])
            {
                visited[y] = true;
                q.push(y);
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m, startNode, node1, node2;
    cin >> n >> m >> startNode;
    for (int i = 0; i < m; i++)
    {
        cin >> node1 >> node2;
        graph[node1].push_back(node2);
        graph[node2].push_back(node1);
    }
    for (int i = 1; i <= n; i++)
    {
        sort(graph[i].begin(), graph[i].end());
    }
    dfs(startNode);
    cout << endl;
    memset(visited, false, sizeof(visited));
    bfs(startNode);
    return 0;
}
