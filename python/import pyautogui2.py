import pyautogui
import time

print("カーソルの位置を5秒間取得します。カーソルを動かして位置を確認してください...")

# 5秒間ループしてカーソル位置を出力
for _ in range(5):
    x, y = pyautogui.position()
    print(f"カーソルの位置: ({x}, {y})")
    time.sleep(1)
