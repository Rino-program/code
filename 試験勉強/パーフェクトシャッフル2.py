# 【問題】n枚のトランプの束がある。これに対し、何回かパーフェクトシャッフルを行うと元の配列に戻る。nを好きに変えて元の配列に戻るまでの回数とnの関係を考察せよ
n = 1000

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
record = {}
for i in range(0, n + 2, 2):
    card = list(range(1, i + 1))
    count = 1
    lis = ps(card)
    while card != lis:
        lis = ps(lis)
        count += 1
    record[i] = count

# 回数を出力
print(f"{record}回")
