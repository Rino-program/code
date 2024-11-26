def ten_two(ten):
    x,li=ten,[]
    ten=abs(ten)
    while ten!=0:
        li.insert(0,ten%2)
        ten = ten//2
    li="".join(map(str,li))
    return li
print(ten_two(int(input("10進数を入力してください。(整数のみ対応)"))))