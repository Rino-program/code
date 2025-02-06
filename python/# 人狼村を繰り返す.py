# 人狼村を繰り返す
import pyautogui
import time
import keyboard
import random

print("Press 'f' to proceed. Press 'esc' to exit.")

# "f" キーが押されるまで待機
keyboard.wait('f')

print("The 'f' key was pressed. Proceeding with the program...")
for i in range(3):
    pyautogui.click(821, 263)
    pyautogui.click(724, 462)
    time.sleep(2)
    pyautogui.click(674, 494)
    time.sleep(2)
    pyautogui.click(821, 263)
    pyautogui.click(724, 462)
    time.sleep(2)
    pyautogui.click(223, 282)
    for i in range(10):
        pyautogui.press('backspace')
    pyautogui.write('test')
    pyautogui.press('#')
    pyautogui.write(str(random.randint(1, 9999)))
    pyautogui.click(113, 716)
    time.sleep(5)
    pyautogui.click(820, 95)
    time.sleep(2)
    pyautogui.click(933, 287)
    time.sleep(2)
    pyautogui.click(821, 263)
    pyautogui.click(724, 462)
    time.sleep(2)
    pyautogui.click(683, 195)
    time.sleep(3)