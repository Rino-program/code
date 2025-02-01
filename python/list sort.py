# ランダムな値が入ったリストを生成,ソートするプログラム
import random

length = int(input("リストの長さを入力してください。"))
Minimum = int(input("値の最小値を入力してください。"))
Maximum = int(input("値の最大値を入力してください。"))
x = []
for i in range(length):
    x.append(random.randint(Minimum, Maximum))
x_sort = sorted(x)
print(f"\n元のリスト{x}\nソート後のリスト{x_sort}\nリストの長さ{len(x)}\n最小値{Minimum}\n最大値{Maximum}")