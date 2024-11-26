def two_ten(two):
    x,two=0,str(two)
    y=two[1:]
    minus=0
    if two[0]=="1":
        minus=1
    for index,digit in enumerate(reversed(y)):
        if digit=="1":
            x+=2**index
    if  minus==1:
        x=-x
    return x
print(two_ten(input("2進数を入力してください。(10進数にしたときの整数のみ対応,符号ビットを使用してください。)")))