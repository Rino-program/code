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
print(two_ten(10011))
