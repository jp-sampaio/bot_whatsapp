'''
    Bot para enviar mensagem em massa no Whatsapp
'''

import pyautogui
import pyperclip
import webbrowser
from time import sleep

# Declarando a lista de telefones vazia
telefones = []

# Pegar os números de um arquivo de texto
with open('telefones.txt', 'r',) as arquivo:
    for linha in arquivo:
        # Utilizar o split para retirar o \n da quebra de linha 
        telefones.append(linha.split('\n')[0])

# Função para escrever mensagens com caracteres especiais
def escrever_mensagem(mensagem):
    pyperclip.copy(mensagem)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)

# Função que vai testar caso não encontre a imagem de abrir whatsapp passar para o próximo passo
def salvar_coordenada_imagem_centro(imagem):
    try:
        return pyautogui.locateCenterOnScreen(imagem)
    except pyautogui.ImageNotFoundException:
        return None

def duplo_tab():
    for i in range(2):
        pyautogui.press('tab')
        sleep(1)

for telefone in telefones:
    # Passo 1 - Abrir o navegador com o link do whatsapp com o número 
    webbrowser.open(f'https://wa.me/{telefone}')
    # => Tempo de 10 segundos para entrar na página
    sleep(10)
    # Passo 2 - Clicar em abrir no whatsapp desktop
    iniciar = salvar_coordenada_imagem_centro('./assets/iniciar.png')
    if iniciar is not None:
        pyautogui.click(x=iniciar[0], y=iniciar[1], duration=1)
        sleep(1)
        duplo_tab()
        pyautogui.press('enter')
    else:
        duplo_tab
        pyautogui.press('enter')

    # => Tempo de 10 segundos para entrar no aplicativo
    sleep(10) 
    # Passo 3 - Escrever a mensagem 
    pyautogui.click(x=613, y=687, duration=2)
    escrever_mensagem('Essa é apenas uma mensagem de teste da minha automação.')
    # => Tempo de 5 segundos para clicar no botão
    sleep(5)
    # Passo 4 - Pressionar o botão enter para enviar a mensagem 
    pyautogui.press('enter')
    # => Tempo de 300 para enviar a próxima mensagem 
    sleep(300)