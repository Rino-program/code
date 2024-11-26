def ten_two(x):
    x=int(x)
    y=[]
    while 0<x:
        y.append(x%2)
        x=x//2
    if y==[]:
        y.append(0)
    return int("".join(map(str, y[::-1])))
print(ten_two(50))