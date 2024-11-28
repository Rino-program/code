# Microsoft Copilotからの出題(練習) ～ランダムなパスワード生成～
def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    for i in range(length):
        # システム時間を使用して擬似乱数を生成
        current_time = int(str(i + len(password))[-1])
        index = (current_time * (i + 1) + length) % len(characters)
        password += characters[index]
    return password

length = int(input("パスワードの長さを入力してください: "))
print(generate_password(length))
