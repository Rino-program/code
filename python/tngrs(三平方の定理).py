def tngrs(numa,numb,numc):
    import math
    lia,lib,lic=[],[],[]
    if "√" in numa or "√" in numb or "√" in numc:
        if "√" in numa:
            lia=numa.split("√")
            numa=math.sqrt((lia[0]**2)*lia[1])
        if "√" in numb:
            lib=numb.split("√")
            numb=math.sqrt((lib[0]**2)*lib[1])
        if "√" in numc:
            lic=numc.split("√")
            numc=math.sqrt((lic[0]**2)*lic[1])
    x_index,cr=0,0
    if not numa:
        x_index+=3
    if not numb:
        x_index+=4
    if not numc:
        x_index+=5
    if x_index>6 or x_index<3:
        return "エラーです。(パターン1)"
    match x_index:
        case 3:
            cr=(numc**2-numb**2)
        case 4:
            cr=(numc**2-numa**2)
        case 5:
            cr=(numa**2+numb**2)
        case _:
            return "エラーです。(パターン2)"
    if cr**(1/2)==int(cr**(1/2)):
        return cr**(1/2)
    else:
        return "√"+str(cr)
an,bn,cn=0,0,0
try:
    an=int(input("aを入力"))
except:
    pass
try:
    bn=int(input("bを入力"))
except:
    pass
try:
    cn=int(input("cを入力"))
except:
    pass
print(tngrs(an,bn,cn))
