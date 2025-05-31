# coding: utf-8
# 024 - Select +／- One（★2）
n, k = tuple(map(int, input().split()))
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))
s = 0
for i in range(n):
    s += abs(li_a[i] - li_b[i])
if (s - k) % 2 == 0 and s <= k:
    print("Yes")
else:
    print("No")
