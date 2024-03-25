import pyautogui

import time

data_inicio = input("Digite a data de início (no formato DD/MM/AAAA): ")

# Solicita ao usuário que insira a data de fim
data_fim = input("Digite a data de fim (no formato DD/MM/AAAA): ")

# Converte as datas para o formato datetime
from datetime import datetime

# ESCOLHER CURSO
print('''Escolha o Treinamento:
[1] RVB
[2] RCL
[3] CRM
''')

while True:
    try:
        curso = int(input('Digite sua opção: '))
        if curso == 1:
            escolha = 'RVB'
            break
        elif curso == 2:
            escolha = 'RCL'
            break
        elif curso == 3:
            crm = int(input("Digite o número do CRM: "))
            escolha = 'CRM'
            try:
                data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
                data_fim = datetime.strptime(data_fim, "%d/%m/%Y")

            except ValueError:
                print("Formato de data inválido. Certifique-se de usar o formato DD/MM/AAAA.")
            print('''Escolha o local do treinamento: 
            [1] SP
            [2] RIO
            [3] POA
            [4] BSB
            [5] FOR ''')
            while True:
                try:
                    local = int(input('Digite sua opção: '))
                    if local == 1:
                        escolha = 'SP'
                        break
                    elif local == 2:
                        escolha = 'RIO'
                        break
                    elif local == 3:
                        escolha = 'POA'
                        break
                    elif local == 4:
                        escolha = 'BSB'
                        break
                    elif local == 5:
                        escolha = 'FOR'
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
                except ValueError:
                    print('Entrada inválida. Digite um número válido.')

                print(f'Você escolheu: {escolha}')

                print('''Escolha o cargo:
                [1] COMISSARIO
                [2] PILOTO
                [3] COPILOTO''')
                cargo = int(input("Digite o cargo: "))


            print('''Escolha o Treinamento:
            [1] PERIÓDICO
            [2] REQUALIFICAÇÃO''')
            while True:
                    try:
                        option = int(input('Digite sua opção: '))
                        if option == 1:
                            escolha = 'PERIÓDICO'
                            break
                        elif option == 2:
                            escolha = 'REQUALIFICAÇÃO'
                            break
                        else:
                            print('Opção inválida. Tente novamente.')
                    except ValueError:
                        print('Entrada inválida. Digite um número válido.')

                        print(f'Você escolheu: {escolha}')
            for _ in range(3):
                # SACI
                pyautogui.click(517,26, duration=0.5)

                # SISHAB --> NRT --> ENIVIADAS
                pyautogui.moveTo(195,508,duration=0.3)
                pyautogui.moveTo(252,502,duration=0.3)
                pyautogui.click(309,510,duration=0.3)
                time.sleep(2.5)


                # INCLUIR
                pyautogui.click(889,381,duration=0.3)

                # CURSO DE:
                time.sleep(1)
                for _ in range(10):
                    pyautogui.press('tab')
                pyautogui.press('enter')

                # COMISSARIO
                if cargo == 1 :
                    for _ in range(2):
                        pyautogui.press('down')
                    pyautogui.press('enter')
                elif cargo == 2:
                    for _ in range(4):
                        pyautogui.press('down')
                    pyautogui.press('enter')
                elif cargo == 3:
                    for _ in range(3):
                        pyautogui.press('down')
                    pyautogui.press('enter')


                # TREINAMENTO
                pyautogui.press('tab')
                pyautogui.press('enter')
                if cargo == 1: 
                    if option == (1):
                        for _ in range(7):
                            pyautogui.press('down')
                        pyautogui.press('enter')
                    elif option ==(2):
                        for _ in range(6):
                            pyautogui.press('down')
                        pyautogui.press('enter')
                elif cargo == 2:
                    if option == (1):
                        for _ in range(5):
                            pyautogui.press('down')
                        pyautogui.press('enter')
                    elif option ==(2):
                        for _ in range(4):
                            pyautogui.press('down')
                        pyautogui.press('enter')
                elif cargo == 3:
                    if option == (1):
                        for _ in range(4):
                            pyautogui.press('down')
                        pyautogui.press('enter')
                    elif option ==(2):
                        for _ in range(1):
                            pyautogui.press('down')
                        pyautogui.press('enter')


                # EQUIPAMENTO(739)
                pyautogui.press('tab')
                pyautogui.press('enter')

                for _ in range(20):
                    pyautogui.press('down')
                pyautogui.press('enter')

                # DATA
                pyautogui.press('tab')
                pyautogui.write(data_inicio)
                pyautogui.press('tab')
                pyautogui.write(data_fim)

                # LOCALIZAÇÃO
                pyautogui.press('tab')
                pyautogui.press('enter')
                pyautogui.press('down')
                pyautogui.press('enter')

                # LOCAL 
                pyautogui.press('tab')


                if (curso == (1) and local == (1)):
                    time.sleep(0.5)
                    pyautogui.write('RVB I PREDIO 13 - PRAÇA CMTE LINEU GOMES PORTARIA 3 - S/N - CGH  SP')
                    pyautogui.press('enter')
                elif (curso == (2) and local == (1)) :
                    time.sleep(0.5)
                    pyautogui.write("RCL PREDIO 13 - PRAÇA CMTE LINEU GOMES PORTARIA 3 - S/N - CGH  SP")
                    pyautogui.press('enter')
                elif (curso == (3) and local == (1)) :
                    time.sleep(0.5)
                    pyautogui.write(f"CRM {crm} FLEX CGH (PRACA COMANDANTE LINEU GOMES , S/N — PORTARIA 3 — VILA CONGONHAS — SAO PAULO — SP)")
                    pyautogui.press('enter')
                    break
                else:
                    print('Opção inválida. Tente novamente.')
    except ValueError:
                print('Entrada inválida. Digite um número válido.')

                print(f'Você escolheu: {escolha}')





