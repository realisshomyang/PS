#include <iostream>
#include <vector>
using namespace std;
long ans;
struct KS
{
    int to;
    int from;
    int weight;
};
int water[301];
int min_water;
vector<KS> Edges;
int N;
int parent[301];
bool comp(KS ks1, KS ks2)
{
    return ks1.weight < ks2.weight;
}
int Find(int num)
{
    if (num == parent[num])
    {
        return num;
    }
    else
    {
        return parent[num] = Find(parent[num]);
    }
}
bool Union(int t, int f)
{
    t = Find(t);
    f = Find(f);
    if (f == t)
    {
        return false;
    }
    else
    {
        parent[t] = f;
        return true;
    }
}

int main()
{
    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        cin >> water[i];
    }
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            int tmp;
            cin >> tmp;
            KS ks;
            if (i == j)
            {
                continue;
            }
            if (i < j)
            {
                if (tmp > water[i] && tmp > water[j])
                {
                    continue;
                }
                ks.from = i;
                ks.to = j;
                ks.weight = tmp;
                Edges.push_back(ks);
            }
        }
    }
    for (int i = 1; i <= N; i++)
    {
        parent[i] = i;
    }
    sort(Edges.begin(), Edges.end(), comp);
    for (int i = 0; i < Edges.size(); i++)
    {
        int t = Edges[i].to;
        int f = Edges[i].from;
        if (Union(t, f))
        {
            ans += Edges[i].weight;
        }
    }
}