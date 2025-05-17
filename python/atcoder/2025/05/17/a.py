n1 = list(map(int, input().split()))
li1 = []
for i in range(n1[2]):
    li1.append(tuple(map(int, input().split())))
n2 = int(input())
query = []
for i in range(n2):
    query.append(tuple(map(int, input().split())))
hyou = []
queue = []
for i in range(n1[0]):
    hyou.append([])
    for j in range(n1[1]):
        if (i + 1, j + 1) in li1:
            hyou[i].append(1)
        else:
            hyou[i].append(0)
for i in range(n2):
    x, y = query[i]
    n = 0
    if (x, y) not in queue:
        if x == 2:
            for j in range(n1[0]):
                if hyou[j][y - 1] == 1:
                    n += 1
                    hyou[j][y - 1] = 0
        elif x == 1:
            for j in range(n1[1]):
                if hyou[y - 1][j] == 1:
                    n += 1
                    hyou[y - 1][j] = 0
        queue.append((x, y))
    print(n)