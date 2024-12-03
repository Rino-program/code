# Microsoft Copilotからの出題(練習) ～ピタゴラスの三つ組の列挙～
def fpt(num):
    lit=[]
    for i in range(1,num):
        for j in range(i,num):
            for k in range(j,num):
                if i**2+j**2==k**2:
                    lit.append((i,j,k))
    return lit
print(fpt(int(input("数を入力"))))
