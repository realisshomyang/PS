#include <iostream>
using namespace std;
#define MAX 201
int dp[MAX][MAX];
int N, K;

int main()
{
    cin >> N >> K;
    for (int i = 1; i <= N; i++)
    {
        dp[i][1] = 1;
    }
    for (int j = 1; j <= K; j++)
    {
        dp[1][j] = j;
    }
    for (int i = 2; i <= N; i++)
    {
        for (int j = 2; j <= K; j++)
        {
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
        }
    }
    cout << dp[N][K];
}