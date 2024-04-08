import pyautogui

import time
from datetime import datetime

qnt = int(input("Digite a quantidade de alunos que vão ser cadastrados: "))
cont = 0
# nrt = (input('Digite a NRT: '))



# # SACI
# pyautogui.click(517,26, duration=0.5)
# pyautogui.hotkey('ctrl', 'home')
        
#     # SISHAB --> NRT --> ENIVIADAS
# pyautogui.moveTo(195,508,duration=0.3)
# pyautogui.moveTo(252,502,duration=0.3)
# pyautogui.click(309,510,duration=0.3)

# time.sleep(2)


# for i in range(11):
#     pyautogui.keyDown('tab')
#     i+1
# pyautogui.write(nrt)
# pyautogui.keyDown('tab')
# pyautogui.write('2024')
# pyautogui.keyDown('enter')

# time.sleep(1.5)
# for _ in range(25):
#     pyautogui.press('tab')
# pyautogui.hotkey('enter')

# Página excel
pyautogui.click(278, 20,duration=0.5)
pyautogui.hotkey('ctrl', 'home')


pyautogui.click(406, 412,duration=0.5)
pyautogui.hotkey('ctrl', 'c')

# Página Anac
pyautogui.click(517,26)

pyautogui.click(436, 461,duration=0.7)

pyautogui.click(478, 309)

pyautogui.click(542, 335)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(498, 396,duration=0.2)

pyautogui.click(634, 540)

pyautogui.click(278, 20)

qnt = qnt-1

while cont < qnt:
    pyautogui.keyDown('down')
    pyautogui.hotkey('ctrl', 'c')

    pyautogui.click(517, 19,duration=0.2)

    pyautogui.click(436, 461,duration=0.3)

    pyautogui.click(478, 309,duration=0.2)

    pyautogui.click(542, 335)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.click(498, 396,duration=0.1)
    

    pyautogui.click(634, 540,duration=0.1)
    pyautogui.click(634, 540)
    

    pyautogui.click(278, 20,duration=0.4)

    
    cont = cont + 1
    if qnt == cont:
        break
    
pyautogui.alert('Alunos cadastrados com sucesso!')




