import numpy as np
import matplotlib.pyplot as plt
Cat = 9
D = {"Casa":90 ,
     "Alimentação":100,
     "Saúde":150,
     "Transporte":70,
     "Educação": 210 ,
     "Lazer":90 ,
     "Outros": 40}
while Cat != "":
    Cat = input("Digite a categoria ('Enter' para finalizar): ").title()
    if Cat == "":
        break 
    else:
        Valor = float(input("Digite o valor: "))
        if Cat not in D:
            D["Outros"] = D["Outros"] + Valor
        else:
            D[Cat]= D[Cat] + Valor


plt.title("Gastos")
Valores = list(D.values())
Cat = list(D.keys())
indice = np.arange(len(Valores))
larg = 0.9
plt.xticks(indice , Cat)
plt.bar(indice,Valores, width=larg)
plt.tight_layout()
plt.show()
