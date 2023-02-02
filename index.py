import pyautogui
import time
# import pandas as pd
# import os

pyautogui.alert('A tarefa vai começar. Não use seu computador enquanto a tarefa não for realizada!')
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('http://127.0.0.1:5500/index.html')
pyautogui.press('enter')
time.sleep(1)


contador = 0
while contador < 1:
    contador += 1

    # clicar no campo text area pra escrever o nome da tarefa a ser executada
    pyautogui.click(330, 237)
    time.sleep(1)
    pyautogui.write('Enviar a dissertacao anexada do aluno para backup')
    time.sleep(2)

    # 1 - selecionar o arquivo (ainda na página de formulário)
    pyautogui.click(368, 359)

    # 2 - acessando a area de trabalho
    pyautogui.click(101, 151)

    # 3 - entrando na pasta: panilhas dissertacao
    pyautogui.click(1033, 158)
    pyautogui.press('enter')
    time.sleep(0.5)

    # 4 - escolhendo o arquivo...
    pyautogui.click(233, 140)
    time.sleep(0.5)

    # 5- apertando o botão de abrir 
    pyautogui.click(1750, 998)
    pyautogui.press('enter')
   

    pyautogui.click(328, 432)
    pyautogui.write('Dissertacao aprovada e enviada para backup') 
    time.sleep(0.5)

    # terceira e última parte da tarefa
    pyautogui.click(323, 565)
    pyautogui.write('Dissertacao enviada no dia 28/11/2022 as 07h15') 
    time.sleep(0.5)


    # Botão de enviar o formulário
    pyautogui.click(340, 646)
    #botão de fechar o modal  
    pyautogui.click(1178, 158)

    # pyautogui.alert('arquivo enviado para backup com sucesso!')
    pyautogui.hotkey('ctrl', 'r')
    pyautogui.click(1133, 161)


    # apagando o arquivo que já foi enviado
    pyautogui.hotkey('winleft', 'e')
    # pyautogui.click(1136, 307)
    pyautogui.click(104, 229)
    pyautogui.click(1183, 226) 
    pyautogui.press('enter')
    pyautogui.click(294, 219)
    pyautogui.hotkey('delete')
    pyautogui.hotkey('alt', 'tab')


else:
    pyautogui.alert('Tarefa finalizada com sucesso!')



# pasta = './content'

# for diretorio, subpastas, arquivos in os.walk(pasta):
#     for arquivo in arquivos:
#         print(os.path.join(diretorio, arquivo))


