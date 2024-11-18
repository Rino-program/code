#フィボナッチ数列(コピペ,自作じゃないです)
import sympy as sym # sympyのインポート
def Fib(n):
    x = sym.symbols('x', nonnegative=True, integer=True)
    Fib = 1 / sym.sqrt(5) * (((1+sym.sqrt(5))/2)**(n-1) - ((1-sym.sqrt(5))/2)**(n-1))
    result = Fib.subs(x, n) # Fibの式のxにnを代入
    result = sym.simplify(result) # 式の整理
    return result
Fiblist = []
for n in range(1, 50):
    Fiblist += [Fib(n)]
Fiblist.pop(0)
print(Fiblist)
