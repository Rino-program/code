def tngrs(numa, numb, numc):
    def hei(a):
        a = str(a)
        if a[0] == "√":
            return int(a[1:])
        else:
            try:
                return int(a) ** 2 # ここで二乗
            except:
                if "√" in a:
                    nums =a.split("√")
                    if all(part.isdigit() for part in nums):
                        return (int(nums[1]) * (int(nums[0]) ** 2))
    x_index, cr = 0, 0
    if not numa:
        x_index += 3
    else:
        numa = hei(numa)
        if isinstance(numa, str):
            return numa
    if not numb:
        x_index += 4
    else:
        numb = hei(numb)
        if isinstance(numb, str):
            return numb
    if not numc:
        x_index += 5
    else:
        numc = hei(numc)
        if isinstance(numc, str):
            return numc
    if x_index > 6 or x_index < 3:
        return "エラーです。(パターン1)"
    match x_index:
        case 3:
            cr = numc - numb
        case 4:
            cr = numc - numa
        case 5:
            cr = numa + numb
        case _:
            return "エラーです。(パターン2)"
    if cr ** (1 / 2) == int(cr ** (1 / 2)):
        return cr ** (1 / 2)
    else:
        def ease_root(n):
            i = 2
            a = 1
            while (i ** 2) <= n:
                if n % (i ** 2) == 0:
                    n //= (i ** 2)
                    a *= i
                else:
                    i += 1
            if n == 1:
                return a
            elif a == 1:
                return f"√{n}"
            else:
                return f"{a}√{n}"
        return ease_root(cr)
an, bn, cn = input("aを入力"), input("bを入力"), input("cを入力")
print(tngrs(an, bn, cn))