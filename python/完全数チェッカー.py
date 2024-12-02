def pn(num):
    num_keep,li=num,[]
    for i in range(1,(num//2)+1):
        if num%i==0:
            li.append(i)
    if sum(li)==num:
        return True
    else:
        return False
print(pn(int(input("数を入力"))))