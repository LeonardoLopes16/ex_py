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
[2] RCL''')

while True:
    try:
        curso = int(input('Digite sua opção: '))
        if curso == 1:
            escolha = 'RVB'
            break
        elif curso == 2:
            escolha = 'RCL'
            break
        else:
            print('Opção inválida. Tente novamente.')
    except ValueError:
        print('Entrada inválida. Digite um número válido.')

print(f'Você escolheu: {escolha}')

#COLETAR DATAS
try:
    data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
    data_fim = datetime.strptime(data_fim, "%d/%m/%Y")

except ValueError:
    print("Formato de data inválido. Certifique-se de usar o formato DD/MM/AAAA.")

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

# SACI
pyautogui.click(517,26, duration=0.5)

# SISHAB --> NRT --> ENIVIADAS
pyautogui.moveTo(195,508,duration=0.3)
pyautogui.moveTo(252,502,duration=0.3)
pyautogui.click(309,510,duration=0.3)


# INCLUIR
pyautogui.click(1212,371,duration=1.0)

# COMISSARIO
time.sleep(1)
for _ in range(10):
    pyautogui.press('tab')
pyautogui.press('enter')
for _ in range(2):
    pyautogui.press('down')
pyautogui.press('enter')

# TREINAMENTO
pyautogui.press('tab')
pyautogui.press('enter')

if option == (1):
    for _ in range(7):
        pyautogui.press('down')
    pyautogui.press('enter')
elif option ==(2):
    for _ in range(6):
        pyautogui.press('down')
    pyautogui.press('enter')

# EQUIPAMENTO(739)
pyautogui.press('tab')
pyautogui.press('enter')

for _ in range(21):
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
if curso == (1):
    time.sleep(0.5)
    pyautogui.write('RVB I PREDIO 13 - PRAÇA CMTE LINEU GOMES PORTARIA 3 - S/N - CGH  SP')
    pyautogui.press('enter')
if curso == (2):
    time.sleep(0.5)
    pyautogui.write("RCL PREDIO 13 - PRAÇA CMTE LINEU GOMES PORTARIA 3 - S/N - CGH  SP")
    pyautogui.press('enter')




