import random

card = [str(i) for i in range(10)]
print(card)

# カードを決定する。
length = int(input("桁数を入力(1-10):"))
random.shuffle(card)
num = "".join(card[:length])

print("ヌメロンゲーム。")

# 正解するまで入力を受け取り、適切な答えを返す。
count = 0
while True:
    count += 1
    inp = input("数字を入力:")
    if len(inp) != length:
        inp = "a"
    try:
        _ = int(inp)
    except:
        print("正しく数字を入力できていないようです。")
        continue
    eat = sum(1 for i in range(length) if inp[i] == num[i])
    bite = sum(1 for i in range(length) if inp[i] != num[i] and inp[i] in num)
    print(f"EAT:{eat}\nBITE:{bite}")
    if eat == len(num):
        break
print(f"成功です！\nあなたは答えを出すのに{count}回かかりました！")
