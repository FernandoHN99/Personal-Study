N = int(input("Quantos elementos terá o vetor? "))
Valores= []
I = 0 

while I < N:
    Valor = float(input("Digite o %iº valor do vetor 'V ALORES':  " % (I + 1) ))
    Valores.append(Valor)
    I = I + 1
    
Maior = max(Valores)
Menor = min(Valores)

print("A diferença é: %.2f " % (Maior-Menor))
