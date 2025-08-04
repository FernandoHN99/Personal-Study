N = int(input("Digite a quantidade de chaves para o código do projeto: "))
i = 1
D = {}
L = []

while i <= N:
    Nome = input("Digite a %iº chave: " % i)
    Valor = float(input("Digite o seu tempo de excução: "))
    D[Nome] = Valor
    L.append(Nome)
    i = i + 1
L.sort()

for item in L:
    print( item + ":" , D[item] )

  