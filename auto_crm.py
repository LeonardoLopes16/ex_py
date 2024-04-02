import pyautogui
 
import time
from datetime import datetime

data_inicio = input("Digite a data de início (no formato DD/MM/AAAA): ")

data_fim = input("Digite a data de fim (no formato DD/MM/AAAA): ")

while True:
    
    #COLETAR DATAS
    try:
        data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
        data_fim = datetime.strptime(data_fim, "%d/%m/%Y")

    except ValueError:
        print("Formato de data inválido. Certifique-se de usar o formato DD/MM/AAAA.")

    nrt = int(input("INSIRA O NÚMERO DA NRT: "))

    # SACI
    pyautogui.click(517,26, duration=0.5)
    pyautogui.hotkey('ctrl', 'home')
        
    # SISHAB --> NRT --> ENIVIADAS
    pyautogui.moveTo(195,508,duration=0.3)
    pyautogui.moveTo(252,502,duration=0.3)
    pyautogui.click(309,510,duration=0.3)
        
    time.sleep(2)
        
        
    #colar NRT (11x"tab")+(ctrl+v)+("tab")+(write"2024")
    for _ in range(11):
        pyautogui.press('tab')
    #pyautogui.write(f" {nrt},")
    
    pyautogui.write(f'{nrt}')
    pyautogui.press('tab')
    pyautogui.write('2024')
        
    #consultar("enter")
    pyautogui.press('enter')
    time.sleep(1)
        
    #Editar Matérias (24x"tab"),("enter")
    time.sleep(1.5)
    for _ in range(24):
        pyautogui.press('tab')
    pyautogui.hotkey('enter')

    # CRM - CRM
    time.sleep(1.5)
    pyautogui.click(1434,818,duration=0.2,interval=2)

    pyautogui.click(1329,811)
    pyautogui.click(1329,811)
    pyautogui.click(1329,811)
    pyautogui.click(1329,811)
    pyautogui.click(1329,811)
    pyautogui.click(1329,811)


    for _ in range(3):
        pyautogui.press('tab')

    pyautogui.click(278,17,duration=0.3)
    time.sleep(1)
    for _ in range(1):
        pyautogui.press('tab')
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.click(517,26, duration=0.5)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('tab')

    # DATA DE INICIO
    pyautogui.write(data_inicio)
    pyautogui.press('tab')

    # HORÁRIO DE INICIO
    pyautogui.write("08:30")
    pyautogui.press('tab')

    #DATA DE TÉRMINO
    pyautogui.write(data_fim)
    pyautogui.press('tab')

    #HORÁRIO DE TÉRMINO
    pyautogui.write('17:30')
    pyautogui.press('tab')

    time.sleep(1)
    pyautogui.click(278,17,duration=0.3)
    pyautogui.press('left')
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.click(517,26, duration=0.5)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    
    for _ in range(2):
        nrt = nrt+1
        #nrt = int(input("INSIRA O NÚMERO DA NRT: "))
        
        
        # SACI
        pyautogui.click(517,26, duration=0.5)
        
        # SISHAB --> NRT --> ENIVIADAS
        pyautogui.moveTo(195,508,duration=0.3)
        pyautogui.moveTo(252,502,duration=0.3)
        pyautogui.click(309,510,duration=0.3)
        
        time.sleep(2.5)
        
        
        #colar NRT (11x"tab")+(ctrl+v)+("tab")+(write"2024")
        for _ in range(11):
            pyautogui.press('tab')
        pyautogui.write(f'{nrt}')
        pyautogui.press('tab')
        pyautogui.write('2024')
        
        #consultar("enter")
        pyautogui.press('enter')
        time.sleep(1)
        
        #Editar Matérias (24x"tab"),("enter")
        time.sleep(1.5)
        for _ in range(24):
            pyautogui.press('tab')
        pyautogui.hotkey('enter')

        # CRM - CRM
        time.sleep(1.5)
        pyautogui.click(1348,574,duration=0.3)
        for _ in range(3):
            pyautogui.press('tab')

        pyautogui.click(278,17,duration=0.3)
        time.sleep(1)
        for _ in range(1):
            pyautogui.press('tab')
        pyautogui.hotkey('ctrl','c')
        time.sleep(1)
        pyautogui.click(517,26, duration=0.5)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('tab')

        # DATA DE INICIO
        pyautogui.write(data_inicio)
        pyautogui.press('tab')

        # HORÁRIO DE INICIO
        pyautogui.write("08:30")
        pyautogui.press('tab')

        #DATA DE TÉRMINO
        pyautogui.write(data_fim)
        pyautogui.press('tab')

        #HORÁRIO DE TÉRMINO
        pyautogui.write('17:30')
        pyautogui.press('tab')

    
        pyautogui.click(278,17,duration=0.3)
        pyautogui.press('left')
        pyautogui.hotkey('ctrl','c')
    
        pyautogui.click(517,26, duration=0.5)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')

    pyautogui.click(278,17,duration=0.3)
    pyautogui.press('down')

