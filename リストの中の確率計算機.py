def a(li):
    li_sum=sum(li)
    lp=[]
    for i in li:
        lp.append(int(i/li_sum*10000)/100)
    return lp
x=[50,25]
print(a(x))
