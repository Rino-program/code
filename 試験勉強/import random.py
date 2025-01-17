import random

card = list(map(str, list(range(10))))
print(card)

# カードを決定する。
random.shuffle(card)
num = "".join(card[:3])

print("ヌメロンゲーム。")

# 正解するまで入力を受け取り、適切な答えを返す。
while True:
    inp = input("数字を入力:")
    if len(inp) != 3:
        inp = "a"
    try:
        _ = int(inp)
    except:
        print("正しく数字を入力できていないようです。")
        continue
    print(len(inp & num.split("")))