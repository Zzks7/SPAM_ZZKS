import pyautogui
from time import sleep

sleep(1)

for _ in range(100):
    pyautogui.write('Spam Zzks')
    pyautogui.press('Enter')
