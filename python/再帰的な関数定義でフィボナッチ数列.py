# 何を作ろうかな？
# 再帰的関数を使用してフィボナッチ数列を作る
def fi(x):
    
    if x <= 1:
        return x
    else:
        return [str(fi()) + str(fi())]

print(fi(5))