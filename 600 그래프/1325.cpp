#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
vector<vector<int>> computers(100001);

int n, m;
int adj[10000][10000];

int main()
{
    scanf("%d %d", &n, &m);
    for (int i = 1; i < n + 1; i++)
    {
        for (int j = 1; j < n + 1; j++)
        {
            adj[i][j] = 0;
        }
    }

    for (int i = 1; i < m + 1; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        adj[a][b] = 1;
        adj[b][a] = 1;
    }
}
