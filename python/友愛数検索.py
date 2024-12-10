def pn(num):
    lit=[]
    for j in range(2,num+1):
        numr=j
        numr_keep,t=numr,0
        for _ in range(2):
            li=[1]
            for i in range(2,int(numr**(1/2))+1):
                if numr%i==0:
                    li.append(i)
                    if i!=numr//i:
                        li.append(numr//i)
            numr=sum(li)
            if t==0:
                num_keep2=sum(li)
                t=1
        if numr_keep==numr and numr!=num_keep2 and (num_keep2,numr) not in lit:
            lit.append((numr,num_keep2))
    return lit
print(pn(int(input("回数"))))