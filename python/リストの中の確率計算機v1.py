from collections import OrderedDict
def count(lst):
    counter=OrderedDict()
    for item in lst:
        if item in counter:
            counter[item]+=1
        else:
            counter[item]=1
    return counter
def probability(li):
    li_sum=sum(li)
    lp=[]
    for i in li:
        lp.append(int(i/li_sum*10000)/100)
    return lp
x=[float(i) for i in input("リストを入力（,で分割）").split(",")]
xp=probability(x)
cut=count(x)
print(dict(zip(x,xp)),cut)
