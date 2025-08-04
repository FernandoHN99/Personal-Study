import numpy as np
Custo_rio = float(input("Digite o custo para estender o cabo via rio: "))
Custo_terra = float(input("Digite o custo para estender o cabo via terra: "))

Dominio = np.arange(0, 3000, 1)
tudo = []
rio = []
terra = []
for x in Dominio:
    tudo.append(Custo_rio*np.sqrt(900**2+x**2) + Custo_terra*(3000-x))
    rio.append( Custo_rio*np.sqrt(900**2+x**2) )
    terra.append( Custo_terra*(3000-x) )
    
Custo_total = np.sum(tudo)
Custo_rio = np.sum(rio)
Custo_terra = np.sum(terra)

print("O Custo pelo rio é de R$%.2f" % Custo_rio)
print("O Custo pelo terra é de R$%.2f" % Custo_terra)
print("O Custo pelo total é de R$%.2f" % Custo_total)