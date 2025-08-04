import numpy as np
Vo = -1
while not Vo >0:
    Vo = float(input("Digite um valor para Vo (m/s): "))
    
Dominio = np.arange(0,Vo,0.01)
y = []
for x in Dominio:
    f = (9700*x)/(5*x**2+570000)
    y.append(f)

D = np.trapz(y,dx=0.01)
print("Distância percorrida pelo avião é de %.1f m" % D)