# 【問題】n枚のトランプの束がある。これに対し、何回かパーフェクトシャッフルを行うと元の配列に戻る。nを好きに変えて元の配列に戻るまでの回数とnの関係を考察せよ
n = 50
card = list(range(1,n + 1))

# パーフェクトシャッフルの関数
def ps(li):
    n = len(li)
    list = []
    card_l, card_h = li[:(n // 2)], li[(n // 2):]
    for i in range(len(card_l)):
        list.append(card_l[i])
        list.append(card_h[i])
    return list

# 回数を調べる
count = 1
list = ps(card)
while card != list:
    list = ps(list)
    count += 1

# 回数を出力
print(f"{count}回")
