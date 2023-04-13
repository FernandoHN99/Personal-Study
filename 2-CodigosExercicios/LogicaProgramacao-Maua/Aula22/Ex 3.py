import numpy as np
import matplotlib.pyplot as plt

coord = np.loadtxt("Mapa.txt", delimiter = ";")
coord = 6371*np.radians(coord)
x = coord[:, 0]
y = coord[:, 1] 

area = -1*((np.trapz(y,x) ))
print("A área do polígono formado é de %.1f Km²" % area)

plt.title("ÁREA")
plt.axis('equal')

plt.grid()

plt.fill(x, y, facecolor = "b" , edgecolor= "k" , linewidth = 3)
plt.show()