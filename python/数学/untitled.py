# 割り算の商とあまり

print("A ÷ B = ?")
A = int(input("Aを入力："))
B = int(input("Bを入力："))
print("{} ÷ {} = {} あまり {}".format(A, B, A // B, A % B))