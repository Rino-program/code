def heihoukon(num):
    import math
    lia,hei,num=[],0,str(num)
    if "√" in num:
        if num[0].isdigit():
            lia=num.split("√")
            num=math.sqrt((lia[0]**2)*lia[1])
            hei=1
        elif num[0]=="√":
            li=[]
            def pnf(x):
                if x%2==0:
                    return False
                for i in range(3,int(x**(1/2))+1,2):
                    if x%i==0:
                        return False
                return True
            for i in range(2,int(num[1:])/2):
                if pnf(i):
                    