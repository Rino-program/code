def heihoukon(num):
    import math
    lia,hei,num=[],0,str(num)
    if "√" in num:
        if num[0].isdigit():
            lia=num.split("√")
            num=math.sqrt((lia[0]**2)*lia[1])
            hei=1
            return num
        elif num[0]=="√":
            li,numa=[],int(num[1:])
            def pnf(x):
                if x%2==0:
                    return False
                for i in range(3,int(x**(1/2))+1,2):
                    if x%i==0:
                        return False
                return True
            a=1
            while not pnf(numa):
                i=2
                if pnf(i):
                    if numa%i==0:
                        numa/=i
                        if i in li:
                            li.pop(li.index(i))
                            a*=i
                        else:
                            li.append(i)
                    else:
                        while not pnf(i):
                            i+=1
            li.append(numa)
            if numa in li:
                li.pop(li.index(i))
                a*=numa
            