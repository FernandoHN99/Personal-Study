import numpy as np
import matplotlib.pyplot as plt
h = 0.428
M = 0.196
m = 0.256

coord = np.loadtxt("Movimento.txt", delimiter = ";")
X = coord[:, 0]
Y = coord[:, 1]

Distancia = np.trapz(Y,X)
d = Distancia - h 

Mi = (M*h)/m*h+(M+m)*d
print("Coeficiente de atrito: %.2f" % Mi)


plt.subplot(2,1,1)
plt.title("Velocidade X Tempo")
plt.xlabel("Tempo(s)" )
plt.ylabel("Velocidade(m/s)" )
plt.plot(X,Y,'k-')
plt.fill_between(X,Y,Color='b',alpha=0.1)
plt.grid()
plt.show()


dy = np.diff(Y)
dx = np.diff(X)
Derivada = dy/dx

#Derivada1 = Derivada
#Derivada1 = list(Derivada1)
#menor = min(Derivada1)
#onde = Derivada1.index(menor)          BONUSS

plt.subplot(2,1,2)
plt.title("Acelereção X Tempo")
plt.xlabel("Tempo(s)" )
plt.ylabel("Acelarção(m/s²)" )
plt.grid()
plt.plot(X[1:],Derivada,'k-',linewidth = 3)
#plt.plot(X[1:],Derivada,'k-',X[onde],menor,"go",linewidth = 3) BONUS
plt.show()




