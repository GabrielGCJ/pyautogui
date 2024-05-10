import pyautogui
import time

# pyautogui.PAUSE = 0.5
# # Abrir e tocar musica com Spotify ---

# pyautogui.press("win")
# pyautogui.write("Spotify")
# pyautogui.press("enter")
# time.sleep(5)
# pyautogui.click(x=958, y=961)

# # # Ir para setima area de trabalho ---

# pyautogui.hotkey("win", "tab")
# time.sleep(3)
# pyautogui.click(x=1424, y=80)

# # # Abrir WhatsApp e Telegram ---

# pyautogui.press("win")
# pyautogui.write("WhatsApp")
# pyautogui.press("enter")

# pyautogui.press("win")
# pyautogui.write("Telegram")
# pyautogui.press("enter")
# time.sleep(2)

# # Ir para sexta area de trabalho ---

# pyautogui.hotkey("win", "tab")
# time.sleep(3)
# pyautogui.click(x=1199, y=91)

# # Abrir o chrome na pagina da e4dev ---

# pyautogui.press("win")
# pyautogui.write("chrome")
# pyautogui.press("enter")
# time.sleep(3)
# pyautogui.click(x=858, y=645)
# pyautogui.write("https://www.linkedin.com/mynetwork/invite-connect/connections/")
# pyautogui.press("enter")
# pyautogui.hotkey("win", "up")

# Ir para quinta area de trabalho ---

pyautogui.hotkey("win", "tab")
time.sleep(3)
pyautogui.click(x=1007, y=90)

# Abrir mensagens Js

pyautogui.click(x=1369, y=832, clicks=2, button="left")
time.sleep(2)
pyautogui.click(x=815, y=573, clicks=1, button="right")
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('enter')
time.sleep(2)

pyautogui.hotkey("win", "left")
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=1076, y=627, clicks=1, button="left")
pyautogui.hotkey("win", "right")
pyautogui.write("http://127.0.0.1:5500/mensagesJs/mensagens/index.html")
pyautogui.press("enter")
time.sleep(2)
# pyautogui.click(x=1418, y=578, clicks=1, button="right")
# pyautogui.press('up')
# pyautogui.press("enter")
# pyautogui.click(x=1400, y=165, clicks=1, button="left")