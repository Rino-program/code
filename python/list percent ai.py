import random

def random_list(num, num2):
    lst = [0] * num  # 指定された要素数のリストを作成し、全てに0を代入
    for _ in range(num2):
        index = random.randint(0, num - 1)  # ランダムな場所を選択
        lst[index] += 1  # 選択された場所の数字に+1
    return lst

def list_percent(num_list):
    total = sum(num_list)
    if total == 0:
        return [0] * len(num_list)  # 合計がゼロの場合、すべての要素をゼロにする
    percentages = [round((x / total) * 100, 2) for x in num_list]  # パーセントに変換し、丸める
    diff = 100 - sum(percentages)  # 誤差を計算
    percentages[0] += diff  # 誤差を最初の要素に加える
    return percentages

x = random_list(10, 1500)
y = list_percent(x)

print(f"乱数表:{x}\nパーセント:{y}\nパーセントの合計値:{sum(y)}")