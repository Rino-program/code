import pyautogui
import keyboard

def get_mouse_position():
    x, y = pyautogui.position()
    print(f"Mouse position: ({x}, {y})")

# "f" キーが押されたときに get_mouse_position 関数を呼び出す
keyboard.add_hotkey('f', get_mouse_position)

print("Press 'f' to get the mouse position. Press 'esc' to exit.")

# プログラムが終了しないように待機
keyboard.wait('esc')