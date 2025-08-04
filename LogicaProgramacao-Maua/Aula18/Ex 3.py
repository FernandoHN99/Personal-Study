Frase = input("Digite uma frase: ")
D= {}
i = 0
for letra in Frase:
    if letra != " ":
        D[letra] =  Frase.count(letra)
print(D)