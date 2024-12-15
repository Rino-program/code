def tngrs(numa,numb,numc):
    def hei(a):
        a=str(a)
        if a[0]=="√":
            return int(a[1:])
        else:
            try:
                return int(a)**2#ここで二乗
            except:
                return "エラーです。√の前に数字を置かないでください。(パターン3)"
    x_index,cr=0,0
    if not numa:
        x_index+=3
    else:
        numa=hei(numa)
        if isinstance(numa,str):
            return numa
    if not numb:
        x_index+=4
    else:
        numb=hei(numb)
        if isinstance(numb,str):
            return numb
    if not numc:
        x_index+=5
    else:
        numc=hei(numc)
        if isinstance(numc,str):
            return numc
    if x_index>6 or x_index<3:
        return "エラーです。(パターン1)"
    match x_index:
        case 3:
            cr=numc-numb
        case 4:
            cr=numc-numa
        case 5:
            cr=numa+numb
        case _:
            return "エラーです。(パターン2)"
    if cr**(1/2)==int(cr**(1/2)):
        return cr**(1/2)
    else:
        return "√"+str(cr)
an,bn,cn=0,0,0
an=input("aを入力")
bn=input("bを入力")
cn=input("cを入力")
print(tngrs(an,bn,cn))