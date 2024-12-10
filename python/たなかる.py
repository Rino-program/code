def tnkl(num):
    lit=[1,1]
    for i in range(num):
        print(lit)
        li=[1,1]
        for j in range(len(lit)-1):
            li.insert(j+1,lit[j]+lit[j+1])
        lit=li
tnkl(int(input("段数")))