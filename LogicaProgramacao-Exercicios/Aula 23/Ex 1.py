import numpy as np
Grau = int(input("Grau do polinômio: "))
i = 0
Coef = []
while i <= Grau:
    N = float(input("Digite o coeficiente a%.i: " % (Grau-i) ))
    Coef.append(N)
    i = i + 1

P = np.poly1d(Coef)
Raizes = P.r

Lista_real = []
Lista_imag = []
for raiz in Raizes:
    if np.imag(raiz) == 0:
        Lista_real.append(float(np.real(raiz) ))
    else:
        Lista_imag.append(raiz)
        
print("Raízes reais:" , Lista_real )
print("Raízes imaginárias:",Lista_imag )


