def test(num):
    numkeep,li=num,[]
    for i in range(1,num):
        li.append((int(i**0.5)*100)/100)
    return li
print(test(int(input(“数字を入力”))))
