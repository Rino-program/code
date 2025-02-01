# Microsoft Copilotからの出題(練習) ～簡易電卓 if ver～
def calculator(x):
    li = x.split()
    a, b, c = int(li[0]), li[1], int(li[2])
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    elif b == "/":
        return a / c
    elif b == "**":
        return a ** c
    elif b == "//":
        return a // c
    else:
        return "エラーです。"

print(calculator(input("計算式を入力してください(例:5 + 3)")))