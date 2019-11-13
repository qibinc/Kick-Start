#include <cstdio>
#include <cstring>
#include <vector>

#define MAXN 100005
int num_villages, beauty[MAXN];
long long f[MAXN][3];

std::vector<int> edges[MAXN];

void init()
{
    scanf("%d", &num_villages);
    for (int i = 1; i <= num_villages; i++)
    {
        scanf("%d", &beauty[i]);
    }
    for (int i = 0; i < num_villages - 1; i++)
    {
        int u, v;
        scanf("%d%d", &u, &v);
        edges[u].push_back(v);
        edges[v].push_back(u);
    }
}

void dp(int node, int parent)
{
    for (auto child : edges[node])
    {
        if (child == parent)
            continue;
        dp(child, node);
    }

    // Case: build
    f[node][0] = beauty[node];
    for (auto child : edges[node])
    {
        if (child == parent)
            continue;
        f[node][0] += std::max(std::max(f[child][0], f[child][1]), f[child][2] + beauty[child]);
    }

    // Case: not build, illuminated
    f[node][1] = beauty[node];
    long long make_child_build = - (1ll << 62);
    for (auto child : edges[node])
    {
        if (child == parent)
            continue;
        f[node][1] += std::max(std::max(f[child][0], f[child][1]), f[child][2]);
        make_child_build = std::max(
            make_child_build, f[child][0] - std::max(f[child][1], f[child][2])
        );
    }
    // When necessary, make one of the child build with least loss
    if (make_child_build < 0)
        f[node][1] += make_child_build;

    // Case: not build, not illuminated
    f[node][2] = 0;
    for (auto child : edges[node])
    {
        if (child == parent)
            continue;
        f[node][2] += std::max(f[child][1], f[child][2]);
    }
}


int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        init();
        dp(1, -1);
        printf("Case #%d: %lld\n", t, std::max(std::max(f[1][0], f[1][1]), f[1][2]));
        for (int i = 1; i <= num_villages; i++)
            edges[i].clear();
    }
}