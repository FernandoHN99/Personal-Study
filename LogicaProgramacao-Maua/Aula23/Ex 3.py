import numpy as np
L = 3
q0 = 192*10**3
E = 207*10**9
I = 2.25 * 10**-4
P = 200 * 10**3
b =12

while not (b>0 and b<1):
    b = float(input("Digite o valor de proporção para b(0 a 1): " ) )
b = b * L
a = L - b

Y_Carrg = np.poly1d([1,-5*L,10*L**2,-10*L**3,0,0])
Parte_1 =  q0/(120*L*E*I)
Y_Carrg = Parte_1 * Y_Carrg

Y_Forca= np.poly1d([-1,0,L**2-b**2,0])
Parte_2 =  (P*b)/(6*L*E*I ) 
Y_Forca = Parte_2 * Y_Forca

P = Y_Forca + Y_Carrg
Raizes = P.r


for raiz in Raizes:
    if np.imag(raiz)== 0 and float (np.real(raiz)) > 0 and float( (np.real(raiz)) <= a ):
        x = float( (np.real(raiz)) )
        print("O valor de x é: %.2f m" % x )
    
