# 練習問題 1: 偶数と奇数の判定
print("偶数です"if int(input("入力:")) % 2 == 0 else "奇数です")

# 練習問題 2: リスト内の最大値と最小値
# max関数やmin関数を使えば一瞬だが楽しくないので作ります。
li = input("入力:").split(",")
max_num, min_num = li[0], li[0]
for i in li: # li[1:]の方が早いが、len(li) == 1だった場合にエラーが発生してしまうのでそのまま使う。
    if max_num < i:
        max_num = i
    elif min_num > i:
        min_num = i
print(f"最大値:{max_num}\n最小値{min_num}")

# 練習問題 3: 素数判定
from math import sqrt
n = int(input("入力:"))
x = 0
if (n == 2 and n % 2 == 0) or n == 1:
    x = 1
else:
    for i in range(3,sqrt(n) + 1,2):
        if n % i == 0:
            x = 1
print("素数です" if x == 0 else "素数ではありません")

# 練習問題 4: ファイルの読み書き
li = []
with open("sample.txt", "r") as f1:
    i = 1
    for line in f1:
        li.append("行 {i}: {len(line)}")
        i += 1
with open("result.txt", "w") as f2:
    for i in li[:len(li)-1]:
        f2.write(f"{i}\n")
    f2.write(f"{li[-1]}")

# 練習問題 5: 辞書を使った英単語カウント
import re
txt_li = re.split(r"[,\s!]+", input("入力:").lower())
tango = {}
for i in range(len(txt_li)):
    if txt_li[i] in tango:
        tango[txt_li[i]] += 1
    else:
        tango[txt_li[i]] = 1
print(tango)

# 練習問題 6: フィボナッチ数列の生成
inp_n = int(input("入力:"))
def f(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)
print(list(f(i) for i in range(inp_n)))

# 練習問題 7: 多次元リストの合計値
from ast import literal_eval as leval
li = list(map(int,leval(input("入力:"))))
li_sum = 0
for i in li:
    for j in i:
        li_sum += j
print(f"出力{li_sum}")