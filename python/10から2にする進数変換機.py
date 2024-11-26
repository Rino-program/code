def ten_two(ten):
    li=[]
    while ten!=0:
        li.insert(0,ten%2)
        ten = ten//2
    return "".join(map(str,li))
print(int(ten_two(int(input("10進数を入力してください。(自然数のみ対応)")))))