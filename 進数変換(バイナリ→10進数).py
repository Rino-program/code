def two_ten(x):
    y=[]
    for i in str(x):
        y.append(i)
    y=y[::-1]
    z=0
    for i in range(len(y)):
        if y[i]=="1":
            z+=2**i
    return z
print(two_ten(input("2進数→10進数変換機\n2進数入力してください。")))
