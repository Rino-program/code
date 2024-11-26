def two_ten(two):
    x,two=0,str(two)
    for index,digit in enumerate(reversed(two)):
        if digit=="1":
            x+=2**index
    return x
print(two_ten(int(input("2進数を入力してください。(10進数にしたときの整数のみ対応)"))))