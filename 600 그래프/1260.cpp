#include <iostream>
#include <queue>

using namespace std;
#define MAX 1001

int n, m, v;
int adj[MAX][MAX];
bool visited[MAX];
queue<int> q;

void DFS(int v)
{
    visited[v] = true;
    cout << v << " ";

    for (int i = 1; i<= n; i++){
        
    }
}