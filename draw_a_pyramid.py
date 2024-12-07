from time import sleep
import pyautogui

n = int(input())

sleep(2)

for i in range(n+1):
    for j in range(i):
        pyautogui.write("#", interval=.25)
    pyautogui.press("enter")