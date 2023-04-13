import pyautogui as pygui
import pyperclip as pyclip #somente para caractere especial
import pandas as pd
import time

def tempo(t):
    time.sleep(t)

def positionMouse():
    tempo(5)
    return print(pygui.position())

pygui.PAUSE = 0.5

#Abrindo o navegador
pygui.press('win')
pygui.write ('chrome')
pygui.press('enter')
tempo(1)

#Entrado no site
pyclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing\n')
pygui.hotkey('ctrl', 'v')
pygui.press('enter')
tempo(3)

#Baixando oo Arquivo
pygui.click(x=456, y=476, clicks=2)
tempo(1)
pygui.click(button='right')
pygui.click(x=572, y=882)
tempo(3)

#Acessando Tabela
tabela = pd.read_excel(r"C:\Users\fernando.h.neto\Downloads\Vendas - Dez.xlsx")
faturamento = tabela["Valor Final"].sum()
qtdProducts = tabela["Quantidade"].sum()


#Acessando o Email
pygui.hotkey('ctrl', 't')
pyclip.copy('https://mail.google.com/mail/u/0/#inbox')
pygui.hotkey('ctrl', 'v')
pygui.press('enter')
tempo(5)

#Escrevendo o email
corpoEmail = f"""Prezado Cliente, bom dia\n\nO faturamento foi de R$: {faturamento:,.2f}\nA Quantidade de Produtos foi de: {qtdProducts:,} \n\n\nAbs\nFernando Henriques"""

pygui.click(x=71, y=280)
tempo(1)
pygui.write('fernandohneto@gmail.com')
pygui.press('tab')
pygui.press('tab')
pygui.write('Relatório de Vendas')
pygui.press('tab')
pygui.write(corpoEmail)
pygui.press('tab')
pygui.press('enter')

# positionMouse()


 