# coding: utf-8
# 004 - Cross Sum
h, w = tuple(map(int, input().split()))
li = []
for i in range(h):
    li.append(list(map(int, input().split())))

x, y = [], []
for i in range(h):
    x.append(sum(li[i]))
for i in range(w):
    y.append(sum(li[j][i] for j in range(h)))

for i in range(h):
    for j in range(w):
        print(x[i] + y[j] - li[i][j], end = " ")
    print()
