def tngrs(numa,numb,numc):
    x_index=0
    if not numa:
        x_index="a"
    if not numb and x_index!="a":
        x_index="b"
    if not numc and x_index!="a" and x_index!="b":
        x_index="c"
    else:
        return "エラーです。(パターン1)"
    match x_index:
        case "a":
            return (numc**2-numb**2)**(1/2)
        case "b":
            return (numc**2-numa**2)**(1/2)
        case "c":
            return (numa**2+numb**2)**(1/2)
an,bn,cn=0,0,0
try:
    an=int(input("aを入力"))
finally:
    pass
try:
    bn=int(input("bを入力"))
finally:
    pass
try:
    cn=int(input("cを入力"))
finally:
    pass
print(tngrs(an,bn,cn))