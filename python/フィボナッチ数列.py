a, b, c, d = 1, 0, [], int(input("値の個数"))
for i in range(d):
    a, b = a + b, a
    c.append(b)
print(c)