from collections import defaultdict

def init():
    n, m, q = map(int, input().split())
    p = list(map(int, input().split()))
    assert len(p) == m
    r = list(map(int, input().split()))
    assert len(r) == q
    return n, m, q, p, r


# def reader_cnt(n, p, reader):
#     cnt = n // reader
#     for broken_page in p:
#         if broken_page % reader == 0:
#             cnt -= 1
#     return cnt


if __name__ == "__main__":
    T = int(input())
    for case_id in range(T):
        n, m, q, p, r = init()
        cnt = 0
        reader_dict = defaultdict(int)
        for reader in r:
            reader_dict[reader] += 1
        pages_torn = [False] * (n + 1)
        for torn in p:
            pages_torn[torn] = True

        pages_cnt = [0] * (n + 1)
        for reader in reader_dict:
            cnt = reader_dict[reader]
            x = reader
            while x <= n:
                pages_cnt[x] += cnt
                x += reader

        pages_sum = 0
        for i in range(1, n + 1):
            if not pages_torn[i]:
                pages_sum += pages_cnt[i]

        print("Case #{0}: {1}".format(case_id + 1, pages_sum))
