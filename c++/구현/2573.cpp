#include <iostream>
const int MAX = 301;
int dx[4];
int dy[4];
int map[MAX][MAX];
bool visited[MAX][MAX];
int N, M;
int cnt;
using namespace std;

void dfs(int a, int b)
{
    visited[a][b] = true;
    for (int i = 0; i < 4; i++)
    {
        int nx, ny = 0;
        nx = a + dx[i];
        ny = b + dy[i];
        if (nx < 0 || ny < 0 || nx >= N || ny >= M)
            continue;
        if (map[nx][ny] == 0)
            continue;
        if (visited[nx][ny] == false)
        {
            visited[nx][ny] = true;
            dfs(nx, ny);
        }
    }
}

int main()
{
    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> map[i][j];
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (map[i][j] != 0 && visited[i][j] != true)
            {
                dfs(i, j);
                cnt++;
            }
        }
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cout << visited[i][j];
        }
        cout << endl;
    }
    cout << cnt;
}