import pyautogui
import time



pyautogui.alert('ATENCAO! Não use seu computador enquanto a tarefa estiver sendo realizada!')
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('http://127.0.0.1:5501/index.html')
pyautogui.press('enter')
time.sleep(1)


contador = 0
while contador <3:
    contador += 1

    # clicar no campo text area pra escrever o nome da tarefa a ser executada
    pyautogui.click(330, 237)
    time.sleep(1)
    pyautogui.write('Enviar dissertacao anexada do aluno para backup')
    time.sleep(2)


    # 1 - clicar para escolher o arquivo
    pyautogui.click(368, 359)
    time.sleep(0.5)

    # 2 - acessar a  area de trabalho
    pyautogui.click(84, 153) 

    # 3 - acessar a pasta: panilhas dissertação
    pyautogui.click(1141, 175)
    pyautogui.press('enter')

    # 4 - selecionar o arquivo
    pyautogui.click(239, 141)

    # 5 - apertar o botão: abrir
    pyautogui.click(1743, 999)

    pyautogui.click(344, 442)
    time.sleep(0.5)
    pyautogui.write('Enviar dissertacao anexada do aluno para carta de aceite')
    time.sleep(0.5)

    pyautogui.click(340, 578)
    pyautogui.write('Dissertacao enviada no dia 30/11/2022 as 07h')


    # Botão de enviar o formulário
    pyautogui.click(332, 646)
    #botão de fechar o modal  
    pyautogui.click(1155, 280)


    pyautogui.hotkey('ctrl', 'r')



    pyautogui.hotkey('winleft', 'e')
    time.sleep(1.0)
    pyautogui.click(85, 231)
    pyautogui.click(1295, 245)
    pyautogui.press('enter')
    pyautogui.click(305, 218)
    pyautogui.hotkey('delete')
    pyautogui.click(1889, 0)
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'tab')

else:
    pyautogui.alert('Tarefa finalizada com sucesso!')