from math import ceil
D = {}
while True:
    Placa = input("Placa do veículo: ").upper()
    E_ou_S = input("(E)ntrada ou (S)aída: ").upper()
    
    if E_ou_S == "" and Placa == "":
        break
    else:
        while E_ou_S == "E" or E_ou_S == "S":
            if E_ou_S == "E":
                Hora = int(input("Hora de entrada(%s): " % Placa ))
                Minutos = int(input("Minuto de entrada(%s): " % Placa ))
                Hora = Hora * 60
                Horario = Hora + Minutos
                D[Placa] = Horario
                break
                
            elif E_ou_S == "S":
                if Placa in D:
                    Hora = int(input("Hora de saída(%s): " % Placa ))
                    Minutos = int(input("Minuto de saída(%s): " % Placa ))
                    Hora = Hora * 60
                    Horario = Hora + Minutos
                    
                    Permanencia = Horario - D[Placa]
                    Permanencia_H = Permanencia/60
                    Permanencia_M = Permanencia-(60*Permanencia_H)
                    
                    del D[Placa]
                    
                    if Permanencia_M == 0:
                        R = ceil(Permanencia_H)   #aredonda sempre pra cima #prof n falou
                    else:
                        R = Permanencia_H + 1
                    print("Permanência do veículo %s: %i hora(s)" % (Placa,R) )
                          
                else:
                    print("Placa não cadastrada!")               
            break