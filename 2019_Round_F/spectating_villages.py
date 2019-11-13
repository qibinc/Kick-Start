import sys

sys.setrecursionlimit(100500)

def init():
    num_villages = int(input())
    beauty = [None] + list(map(int, input().split()))
    assert len(beauty) == num_villages + 1
    edges = [[] for _ in range(num_villages + 1)]
    for _ in range(num_villages - 1):
        u, v = list(map(int, input().split()))
        edges[u].append(v)
        edges[v].append(u)

    return num_villages, beauty, edges


def dp(node, f, beauty, edges, parent):
    for child in edges[node]:
        if child == parent:
            continue
        dp(child, f, beauty, edges, node)

    # Case: build
    score = beauty[node]
    for child in edges[node]:
        if child == parent:
            continue
        score += max(f[child][0], f[child][1], f[child][2] + beauty[child])
    f[node].append(score)

    # Case: not build, illuminated
    score = beauty[node]
    make_child_build = float("-inf")
    for child in edges[node]:
        if child == parent:
            continue
        score += max(f[child][0], f[child][1], f[child][2])
        make_child_build = max(
            make_child_build, f[child][0] - max(f[child][1], f[child][2])
        )
    # When necessary, make one of the child build with least loss
    if make_child_build < 0:
        score += make_child_build
    f[node].append(score)

    # Case: not build, not illuminated
    score = 0
    for child in edges[node]:
        if child == parent:
            continue
        score += max(f[child][1], f[child][2])
    f[node].append(score)


if __name__ == "__main__":
    T = int(input())
    for case_id in range(T):
        num_villages, beauty, edges = init()
        f = [[] for _ in range(num_villages + 1)]
        dp(1, f, beauty, edges, None)
        print("Case #{0}: {1}".format(case_id + 1, max(f[1])))
