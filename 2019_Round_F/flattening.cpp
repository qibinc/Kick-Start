#include <cstdio>
#include <cstring>
#include <iostream>

int T;
int n, k, a[101], f[101][1001][101];

int main()
{
    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        scanf("%d%d", &n, &k);
        int cap_height = 0;
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
            cap_height = std::max(cap_height, a[i]);
        }
        cap_height += 1;
        memset(f, 0x7f, sizeof(f));
        for (int height = 0; height < cap_height; height++)
        {
            f[0][height][0] = 1;
        }
        f[0][a[0]][0] = 0;
        for (int i = 1; i < n; i++)
        {
            for (int changes = 0; changes <= k; changes++)
            {
                int last_rebuild_min = 1 << 30, last_rebuild_num_min = 0, last_rebuild_second_min = 1 << 30;
                for (int height = 0; height < cap_height; height++)
                {
                    if (f[i - 1][height][changes - 1] == last_rebuild_min)
                        last_rebuild_num_min++;
                    if (f[i - 1][height][changes - 1] < last_rebuild_min)
                    {
                        last_rebuild_min = f[i - 1][height][changes - 1];
                        last_rebuild_num_min = 1;
                    }
                }
                for (int height = 0; height < cap_height; height++)
                {
                    if (f[i - 1][height][changes - 1] > last_rebuild_min and f[i - 1][height][changes - 1] < last_rebuild_second_min)
                        last_rebuild_second_min = f[i - 1][height][changes - 1];
                }
                for (int height = 0; height < cap_height; height++)
                {
                    if (changes != 0)
                    {

                        if (last_rebuild_min < f[i - 1][height][changes - 1] or last_rebuild_num_min > 1)
                            f[i][height][changes] = std::min(f[i - 1][height][changes], last_rebuild_min);
                        else
                            f[i][height][changes] = std::min(f[i - 1][height][changes], last_rebuild_second_min);
                    }
                    else
                    {
                        f[i][height][changes] = f[i - 1][height][changes];
                    }
                    if (height != a[i])
                    {
                        // Rebuild
                        f[i][height][changes] += 1;
                    }
                }

            }
        }
        int ans_min = 1 << 30;
        for (int changes = 0; changes <= k; changes++)
            for (int height = 0; height < cap_height; height++)
                if (f[n - 1][height][changes] < ans_min)
                    ans_min = f[n - 1][height][changes];
        printf("Case #%d: %d\n", t, int(ans_min));
    }

    return 0;
}
