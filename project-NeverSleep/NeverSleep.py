import pyautogui as pygui
import time
from datetime import datetime

# Função para pausar a execução por 't' segundos
def pause(t):
    time.sleep(t)

# Função para obter e exibir a posição do mouse após uma pausa
def display_mouse_position_after_delay():
    pause(5)
    print(pygui.position())

# Função para obter e validar a entrada do usuário no formato hh:mm
def get_stop_time():
    while True:
        user_input = input("Por favor, insira o horário para parar o script no formato hh:mm: ")
        try:
            stop_time = datetime.strptime(user_input, "%H:%M").time()
            return stop_time
        except ValueError:
            print("Formato inválido! Certifique-se de que está no formato hh:mm.")

# Tempo de espera para o início do programa
INITIAL_DELAY = 10

# Intervalo de ciclos em segundos
CYCLE_INTERVAL = 60

# Duração da animação de movimento do mouse
ANIMATION_DURATION = 8

#Posição do mouse incial
INITIAL_POSITION = (142, 85)

#Posição do mouse final
FINAL_POSITION = (333, 120)

# Obtendo o horário para parar o script
stop_time = get_stop_time()

print(f"O programa começará em {INITIAL_DELAY} segundos.")
pause(INITIAL_DELAY)

# Loop principal
while True:
    # Move para a posição da primeira ação e clica
    pygui.moveTo(INITIAL_POSITION[0], INITIAL_POSITION[1])
    pygui.click()

    # Move para a posição da segunda ação com uma animação de 8 segundos
    pygui.moveTo(FINAL_POSITION[0], FINAL_POSITION[1], duration=ANIMATION_DURATION)

    current_time = datetime.now().time()
    
    # Verifica se o horário atual é maior ou igual ao horário de parada
    if current_time >= stop_time:
        print(f"O horário de parada ({stop_time}) foi atingido. O script será encerrado.")
        break

    elapsed_seconds = 0
    
    # Loop para contar o tempo de espera até o próximo ciclo
    while elapsed_seconds <= CYCLE_INTERVAL:
        remaining_time = CYCLE_INTERVAL - elapsed_seconds
        elapsed_seconds += 1
        pause(1)
