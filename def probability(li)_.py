from collections import Counter
def probability(li):
    li_sum=sum(li)
    lp=[]
    for i in li:
        lp.append(int(i/li_sum*10000)/100)
    return lp
x=[float(i) for i in input("リストを入力（,で分割）").split(",")]
xp=probability(x)
x=Counter(x)
print(dict(zip(x,xp)),x)