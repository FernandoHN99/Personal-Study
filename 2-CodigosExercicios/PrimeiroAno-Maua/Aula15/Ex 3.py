tamanho = int(input("Digite o tamanho do vetor: ") )
vetor1 = list(range(1, tamanho + 1) )
print(vetor1)
input()

m = int(input("Digite o deslcamento: " ))
i = 1
while i < m:
    palavra = vetor1.pop()
    vetor1.insert(0, palavra)
    i = i + 1
    
print(vetor1)
    
    