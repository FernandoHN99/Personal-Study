import numpy as np

def f(x):
    if (0<= x <=0.5):
        Fx = -x*(x-1) + 2.5
    if (0.5< x <=1.35):
        Fx = 2.76
    if (1.35< x <=2.4):
        Fx = 2.76*np.cos(0.45*(x-1.35))
    if (2.4< x <=5):
        Fx = 0.08*(x-2.4)*(x-5.5)+2.46
    if(5< x <=15):
        Fx = -0.025*(x-5)*(x-12.5)+2.35
    if (15< x <=18):
        Fx = 0.05*(x-15)*(x-21)+1.73
    
    return Fx




H = 120
while not (H>=0 and H<=18):
    H = float(input("Digite a altura do líquido: " ))
  
Dominio = np.arange(0, H, 0.01)
y = [] 
for x in Dominio:
    y.append(f(x)**2)

Volume = np.pi*np.trapz(y,dx=0.01)

print("Volume do sólido: %.f ml" % Volume)

if H>15:
    print("Garrafa muito cheia")