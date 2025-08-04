import numpy as np

Numerador = np.poly1d([1,-2,-1,2])
print(Numerador)

Denominador = np.poly1d([1,0,-7,6])
print(Denominador)

while Denominador(1) == 0:
    Numerador = Numerador.deriv()
    Denominador = Denominador.deriv()

Divisao = Numerador(1)/Denominador(1)
Quociente = Divisao
print()
print("O limite é: %.1f" % Quociente)