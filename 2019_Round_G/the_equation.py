def init():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    assert len(a) == n
    return n, m, a

def find_k(m, a):
    for k in range(m + max(a), -1, -1):
        universe_sum = sum(map(lambda x: x ^ k, a))
        if universe_sum <= m:
            return k
    return -1


if __name__ == "__main__":
    T = int(input())
    for case_id in range(T):
        n, m, a = init()

        print("Case #{0}: {1}".format(case_id + 1, find_k(m, a)))
