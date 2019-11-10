from itertools import accumulate

def init():
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    assert len(a) == n and len(b) == n
    return n, h, a, b

def dfs(n, h, a, b, suffix_sum_a, suffix_sum_b, i, h_a, h_b):
    if i == n:
        if h_a >= h and h_b >= h:
            return 1
        else:
            return 0

    cnt = 0
    if h_a + suffix_sum_a[i] >= h and h_b + suffix_sum_b[i] - b[i] >= h:
        cnt += dfs(n, h, a, b, suffix_sum_a, suffix_sum_b, i + 1, h_a + a[i], h_b)
    if h_a + suffix_sum_a[i] - a[i] >= h and h_b + suffix_sum_b[i] >= h:
        cnt += dfs(n, h, a, b, suffix_sum_a, suffix_sum_b, i + 1, h_a, h_b + b[i])
    cnt += dfs(n, h, a, b, suffix_sum_a, suffix_sum_b, i + 1, h_a + a[i], h_b + b[i])
    return cnt

if __name__ == "__main__":
    T = int(input())
    for case_id in range(T):
        n, h, a, b = init()
        suffix_sum_a = list(reversed(list(accumulate(reversed(a)))))
        suffix_sum_b = list(reversed(list(accumulate(reversed(b)))))

        print("Case #{0}: {1}".format(case_id + 1, dfs(n, h, a, b, suffix_sum_a, suffix_sum_b, 0, 0, 0)))
