n, m = tuple(map(int, input().split()))
li_s = dict()

for i in range(1, n + 1):
    li_s[str(i)] = 0

for _ in range(m):
    l, r = tuple(map(int, input().split()))
    for i in list(range(l, r + 1)):
        li_s[str(i)] += 1

print(min(list(li_s.values())))