import numpy as np

Y1 = [0,20,22,39,42,45,47,45,40,39,0]
Area1 = np.trapz(Y1,dx=5)

Y2 = [ 0,34,50,52,36,0]
Area2 = np.trapz(Y2, dx=10)
print("O valor da superfície do lago é de aproximadamente %.f m²" % (Area1+Area2) )