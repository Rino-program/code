import pyautogui
import time

print("マウスカーソルの座標を表示します。Ctrl+Cで終了してください。")
try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}, Y: {y}", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n終了しました。")
