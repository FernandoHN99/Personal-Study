import numpy as np
import matplotlib.pyplot as plt
Cat = 9
D = {"Casa":90 ,
     "Alimentação":100,
     "Saúde":150,
     "Transporte":70,
     "Outros": 76
     }

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
Destacar = [0,0,0,0,0.1]
plt.pie(Valores, labels = Cat, autopct="%.1f%%", explode = Destacar)
plt.axis("equal")
plt.tight_layout()
plt.show

