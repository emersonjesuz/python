import pyperclip
import pyautogui
from time import sleep
pyautogui.PAUSE = 2
pyautogui.press('win')
pyautogui.write('google chrome')
pyautogui.press('enter')
sleep(15)
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('Enter')
sleep(15)
pyautogui.click(x=345, y=308, clicks=2)
sleep(5)
pyautogui.click(x=357, y=397)
pyautogui.click(x=1160, y=196)
pyautogui.click(x=909, y=591)


