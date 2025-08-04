Lista = [0]
Tamanho = int(input("Quantos elementos o vetor terá? "))
A = int(input("Valor de A: "))
B = int(input("Valor de B: "))

Lista = Lista * Tamanho

Lista = Lista[A : B + 1]

Resposta = Lista.count(0)

print("No intervalo fechado tem %i elementos" % Resposta)