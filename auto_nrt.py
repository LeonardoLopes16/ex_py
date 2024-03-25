import pyautogui

qnt = int(input("Digite a quantidade de alunos que vão ser cadastrados: "))
cont = 0
nrt = (input('Digite a NRT: '))



pyautogui.click(839, 19,duration=0.5)
for i in range(11):
    pyautogui.keyDown('tab')
    i+1

pyautogui.write(nrt)

# # Página excel
# pyautogui.click(660, 20,duration=0.5)


# pyautogui.click(406, 412,duration=0.5)
# pyautogui.hotkey('ctrl', 'c')

# # Página Anac
# pyautogui.click(839, 19,duration=0.5)

# pyautogui.click(436, 461,duration=0.7)

# pyautogui.click(478, 309,duration=0.5)

# pyautogui.click(542, 335,duration=0.5)
# pyautogui.hotkey('ctrl', 'v')

# pyautogui.click(498, 396,duration=0.2)

# pyautogui.click(634, 540,duration=0.5)

# pyautogui.click(660, 20,)

# qnt = qnt-1

# while cont < qnt:
#     pyautogui.keyDown('down')
#     pyautogui.hotkey('ctrl', 'c')

#     pyautogui.click(839, 19,duration=0.5)

#     pyautogui.click(436, 461,duration=0.7)

#     pyautogui.click(478, 309,duration=0.5)

#     pyautogui.click(542, 335,duration=0.5)
#     pyautogui.hotkey('ctrl', 'v')

#     pyautogui.click(498, 396,duration=0.2)

#     pyautogui.click(634, 540,duration=0.5)

#     pyautogui.click(660, 20,)

    
#     cont = cont + 1
#     if qnt == cont:
#         break
    
# pyautogui.alert('Alunos cadastrados com ')




