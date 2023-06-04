
import pyautogui as pygui
import pyperclip as pyclip
import time

def tempo(t):
    time.sleep(t)

def positionMouse():
    tempo(5)
    return print(pygui.position())
    
print(f"O programa começará em próximos 10 segundos")
intervaloDeCiclos = 100 #Em segundos
tempo(10)
while(True):
    pygui.moveTo(142, 85)
    pygui.click()
    pygui.moveTo(333, 120, 8)
    segundosEfetuados=0
    while(segundosEfetuados <= intervaloDeCiclos):
        print(f"Próximo ciclo em: {intervaloDeCiclos-segundosEfetuados} segundos (Ctrl + c)")
        segundosEfetuados+=1
        tempo(1)