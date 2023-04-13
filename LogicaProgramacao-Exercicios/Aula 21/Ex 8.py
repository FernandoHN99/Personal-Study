import numpy as np
                 # 0      1     2
A = np.array( [ [ 0.6 , 0.15, 0.25 ] ,   # 0
                [ 0.2 , 0.7 , 0.1  ],    # 1        } cliente
                [ 0.6 , 0.3 , 0.1  ]  ]) # 2

Empresa = int(input("Digite o código da empresa (0, 1 ,2): " ))
Cliente = int(input("Digite o código do cliente (0, 1 ,2): " ))
Compra2 = A@A
Compra3 = Compra2 @ A

print(Compra2)
print()
print(Compra3)

print()
print()
print()

Compra2 = Compra2.T
Compra3 = Compra3.T

print("Probabilidade do cliente(%i) voltar a comprar na empresa(%i) após 1ª compra: %.f%% " % (Cliente, Empresa, Compra2[Empresa][Cliente]*100 ))
print("Probabilidade do cliente(%i) voltar a comprar na empresa(%i) após 2ª compra: %.f%% " % (Cliente, Empresa, Compra3[Empresa][Cliente]*100 ))