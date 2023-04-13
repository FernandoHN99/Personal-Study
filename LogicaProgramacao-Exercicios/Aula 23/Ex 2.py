import numpy as np
import matplotlib.pyplot as plt
def R2(x,y,P):
    SQres = sum((y-P(x))**2)
    SQtot = sum ((y - np.average(y))**2 )
    return 1 - SQres/SQtot

N = int(input("Quantidade de pontos: "))
i = 1
Coord_x = []
Coord_y = []
while i <= N:
    x = float(input("Digite a coordenada x%i: " % i))
    y = float(input("Digite a coordenada y%i: " % i))
    Coord_x.append(x)
    Coord_y.append(y)
    i = i + 1

Grau = int(input("Ordem de ajuste: "))
Coord_x = np.array(Coord_x)    
Coord_y = np.array(Coord_y)    

P = np.poly1d(np.polyfit(Coord_x,Coord_y,Grau))
R2 = R2(Coord_x,Coord_y,P)

Maximo = max(Coord_x)
Minimo= min(Coord_x)

Dominio = np.linspace(Maximo, Minimo, num = 200)
plt.title(" Gráifco pH x tempo ")
plt.plot(Dominio, P(Dominio), "g--", linewidth = 3, label = "Modelo")
plt.plot(Coord_x,Coord_y,"ro", linewidth = 5, label = "Experimental")
plt.xlabel("Tempo")
plt.ylabel("pH da Solução")
plt.grid()
plt.legend(loc = "best")
plt.show()

print(P)
print("R²: %.2f" % R2)