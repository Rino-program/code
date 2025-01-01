import random

def random_list(num,num2):
    lst = [0] * num  # 指定された要素数のリストを作成し、全てに0を代入
    for _ in range(num2):
        index = random.randint(0, num - 1)  # ランダムな場所を選択
        lst[index] += 1  # 選択された場所の数字に+1
    return lst

def list_percent(num_list):
    total = sum(num_list)
    if total == 0:
        return [0] * len(num_list)  # 合計がゼロの場合、すべての要素をゼロにする
    return [(x / total) * 100 for x in num_list]  # パーセントに変換

x = random_list(int(input("要素数を入力:")),int(input("回数を入力:")))
y = list_percent(x)
z = sum(y)/len(y)

print(f"乱数表:{x}\nパーセント:{y}\nパーセントの合計値:{sum(y)}")
print(f"平均値{z}\n最大値からの誤差{max(y)-z}\n最小値からの誤差{-(min(y)-z)}")