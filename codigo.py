# Teste programando em python
import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
# pyautogui.hotkey("win", "v")
pyautogui.write("chrome")
# print("Olá mundo")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=1038, y=628, clicks=2, button="left")
