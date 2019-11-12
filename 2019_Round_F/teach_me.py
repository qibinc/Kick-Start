def init():
    n, s = map(int, input().split())
    a = []
    for _ in range(n):
        line = list(map(int, input().split()))
        assert len(line) == line[0] + 1 
        a.append(set(line[1:]))
    return n, s, a

if __name__ == "__main__":
    T = int(input())
    for case_id in range(T):
        n, s, a = init()
        ans = 0
        for i in range(n):
            for j in range(n):
                if a[i] - a[j]:
                    ans += 1

        print("Case #{0}: {1}".format(case_id + 1, ans))
