import numpy as np
import matplotlib.pyplot as plt

#a-)

Dominio = np.linspace(-10,10,num=1000 )

Y = []
for x in Dominio:
    Y.append(np.sin(x)/x )

plt.subplot(2,1,1 )   
plt.title("Gráfico sin(x)/x" )
plt.plot(Dominio, Y, "k-",linewidth = 3,)
plt.legend(loc='best')
plt.tight_layout()
plt.grid()
plt.show()


#b-)
plt.subplot(2,1,2 )  
Y1 = np.diff(Y)
X1 = np.diff(Dominio)
R = Y1/X1
plt.title("Gráfico Derivada" )
plt.plot(Dominio[1:], R, "k-",linewidth = 3)
plt.grid()
plt.tight_layout()
plt.show()

