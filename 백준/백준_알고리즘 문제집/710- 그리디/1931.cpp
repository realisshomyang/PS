#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>

using namespace std;
int N;
vector<pair<int, int>> v;

int main()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int start, end;
        cin >> start >> end;
        v.push_back(make_pair(start, end));
    }
    sort(v.begin(), v.end());
}