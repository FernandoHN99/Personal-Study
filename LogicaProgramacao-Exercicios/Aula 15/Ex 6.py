Grau  = int(input("Digite o grau do polinômio: " ))
i = 0
Coef = []
for coeficiente in range(Grau + 1):
    coeficiente = float(input("Digite o coeficiente a%i: " % i ))
    Coef.append(coeficiente)
    i = i + 1
     
funcao = ""
Expoente = Grau
Coef.reverse()

for c in Coef:
    parte = [Coef[Coef.index(c)], ".x**", Expoente]    
    Expoente = Expoente - 1
    
    for i in range(len(parte)):
        parte[i] = str(parte[i])
    
    if Expoente == -1:
        S = "".join(parte) 
        funcao = funcao + S
    else: 
        S = "".join(parte) + " " + "+" + " "
        funcao = funcao + S

print("P(x) = %s" % funcao)
print()


X = float(input("Digite o valor de X: " ))
Expoente = Grau
soma = 0

for c in Coef:
    Conta = c *X** Expoente
    soma = soma + Conta
    Expoente = Expoente - 1
    
print("P(%.1f) = %.1f" % (X, soma))