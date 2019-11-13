from collections import defaultdict

def init():
    n, s = map(int, input().split())
    a = []
    d = defaultdict(int)
    for _ in range(n):
        line = list(map(int, input().split()))
        assert len(line) == line[0] + 1 
        skills = tuple(sorted(line[1:]))
        d[skills] += 1
        a.append(skills)
    return n, s, a, d

if __name__ == "__main__":
    T = int(input())
    for case_id in range(T):
        n, s, a, d = init()
        ans = 0
        for i in range(n):
            skills = a[i]
            cannot_taught_by = 0
            for k in range(1 << len(skills)):
                skill = []
                for bit in range(len(skills)):
                    if k & (1 << bit):
                        skill.append(skills[bit])
                skill = tuple(skill)
                if skill in d:
                    cannot_taught_by += d[skill]

            ans += n - cannot_taught_by

        print("Case #{0}: {1}".format(case_id + 1, ans))
