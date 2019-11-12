import numpy as np


def init():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    assert len(a) == n
    return n, k, a


if __name__ == "__main__":
    T = int(input())
    for case_id in range(T):
        n, k, a = init()
        cap_height = max(a) + 1
        f = np.zeros((n, cap_height, k + 1))
        f[0] = np.inf
        f[0, :, 0] = 1
        f[0, a[0], 0] = 0
        for i in range(1, n):
            for changes in range(0, k + 1):
                last_rebuild_min = f[i - 1, :, changes - 1].min()
                last_rebuild_num_min = np.sum((f[i - 1, :, changes - 1] == last_rebuild_min))
                if (f[i - 1, :, changes - 1] != last_rebuild_min).sum() > 0:
                    last_rebuild_second_min = f[i - 1, f[i - 1, :, changes - 1] != last_rebuild_min, changes - 1].min()
                for height in range(0, cap_height):
                    if changes != 0:
                        if last_rebuild_min < f[i - 1, height, changes - 1] or last_rebuild_num_min > 1:
                            f[i][height][changes] = min(f[i - 1, height, changes], last_rebuild_min)
                        else:
                            f[i][height][changes] = min(f[i - 1, height, changes], last_rebuild_second_min)
                    else:
                        f[i][height][changes] = f[i - 1, height, changes]

                    if height != a[i]:
                        # Rebuild
                        f[i][height][changes] += 1

        print("Case #{0}: {1}".format(case_id + 1, int(f[-1].min())))
