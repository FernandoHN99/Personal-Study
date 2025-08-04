def X(Tabela):
    Visc = Tabela[0][1]
    Temp = Tabela[0][0]
    for c in range(len(Tabela)):
        medida = Tabela[c]
        if medida[1] > Visc:
            Visc = medida[1]
            Temp = medida[0]
    return Temp

N = int(input("Quantos pares deseja digitar? "))
Tabela = []
i = 1
for elemento in range(N):
    T = float(input("Temperatura %i: " % i))
    V = float(input("Viscosidade %i: " % i))
    Tabela2 = [T , V]
    Tabela.append(Tabela2)
    i = i + 1

print("A temperatura para a maior viscosidade medida é de %.2f Graus" % X(Tabela))