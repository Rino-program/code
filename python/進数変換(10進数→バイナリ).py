def ten_two(x):
    x=int(x)
    y=[]
    while 0<x:
        y.append(x%2)
        x=x//2
    if y==[]:
        y.append(0)
    return int("".join(list(map(str, y[::-1]))))
print(ten_two(input("10進数→2進数変換器\n10進数を入力してください。")))
