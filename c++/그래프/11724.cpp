#include <iostream>
using namespace std;
const int MAX = 1001;
int cnt;
int N, M;
bool map[MAX][MAX];
bool visited[MAX];

void dfs(int a)
{
    visited[a] = true;
    for (int i = 1; i <= N; i++)
    {
        if (!visited[i] && map[a][i])
        {
            dfs(i);
        }
    }
}

int main()
{
    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        int node1, node2;
        cin >> node1 >> node2;
        map[node1][node2] = true;
        map[node2][node1] = true;
    }
    for (int i = 1; i <= N; i++)
    {
        if ((!visited[i]))
        {
            cnt++;
            dfs(i);
        }
    }

    cout << cnt;
}
