# 再帰を使って階乗をしてみよう！
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))