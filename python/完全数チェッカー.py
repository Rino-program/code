def pn(num):
    num_keep,li=num,[1]
    for i in range(2,int(num**(1/2))+1):
        if num%i==0:
            li.append(i)
            if i!=num//i:
                li.append(num//i)
    return sum(li)==num
print(pn(int(input("数を入力"))))