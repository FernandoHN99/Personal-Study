import pyautogui as pygui
import pyperclip as pyclip
import time

def tempo(t):
    time.sleep(t)

def positionMouse():
    tempo(5)
    return print(pygui.position())

def checkTeams():
    pygui.moveTo(110, 120)
    pygui.drag(15, 0, 0.3, button='left')
    pygui.hotkey('ctrl', 'c')
    pygui.hotkey('ctrl', 'v')
    paste_data = str(pyclip.paste())
    if(paste_data == 'Chat'):
        pyclip.copy('Null')
        return True
    else:
        return False

    # PROGRAMA PRINCIPAL

print(f"O programa começará em próximos 10 segundos")
intervaloDeCiclos = 100 #Em segundos
tempo(10)
pygui.hotkey('win', 'm')
tempo(0.7)
pygui.moveTo(568, 1046)
pygui.click()
tempo(0.2)
pygui.hotkey('win', 'up')

# while(checkTeams()):
while(True):
    pygui.moveTo(142, 85)
    pygui.click()
    pygui.moveTo(333, 120, 90)
    pygui.click()
    segundosEfetuados=0
    while(segundosEfetuados <= intervaloDeCiclos):
        print(f"Próximo ciclo em: {intervaloDeCiclos-segundosEfetuados} segundos (Ctrl + c)")
        segundosEfetuados+=1
        tempo(1)