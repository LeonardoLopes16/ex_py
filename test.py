import pyautogui



pyautogui.click(278,17,duration=0.3)
pyautogui.press('tab')
local = pyautogui.hotkey('ctrl','c')

print(f'{local}')